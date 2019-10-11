# encoding: utf-8


"""


@author: tongzhenguo

@time: 2019/10/10 下午7:48

@desc:


"""

import numpy as np
from collections import deque
import random
import tensorflow as tf
from math import sqrt


class Agent(object):
    def __init__(self, model, replay_buffer, exploration_noise, discout_factor, verbose=False):
        self.model = model
        self.replay_buffer = replay_buffer
        self.exploration_noise = exploration_noise
        self.discout_factor = discout_factor
        self.verbose = verbose

    def predict_action(self, observation):
        return self.model.predict_action(observation)

    def select_action(self, observation, p=None):
        pred_action = self.predict_action(observation)
        noise = self.exploration_noise.return_noise()
        if p is not None:
            return pred_action * p + noise * (1 - p)
        else:
            return pred_action + noise

    def store_transition(self, transition):
        self.replay_buffer.store_transition(transition)

    def init_process(self):
        self.exploration_noise.init_process()

    def get_transition_batch(self):
        batch = self.replay_buffer.get_batch()
        transpose_batch = list(zip(*batch))
        s_batch = np.vstack(transpose_batch[0])
        a_batch = np.vstack(transpose_batch[1])
        r_batch = np.vstack(transpose_batch[2])
        next_s_batch = np.vstack(transpose_batch[3])
        done_batch = np.vstack(transpose_batch[4])
        return s_batch, a_batch, r_batch, next_s_batch, done_batch

    def preprocess_batch(self, s_batch, a_batch, r_batch, next_s_batch, done_batch):
        target_actor_net_pred_action = self.model.actor.predict_action_target_net(next_s_batch)
        target_critic_net_pred_q = self.model.critic.predict_q_target_net(next_s_batch, target_actor_net_pred_action)
        y_batch = r_batch + self.discout_factor * target_critic_net_pred_q * (1 - done_batch)
        return s_batch, a_batch, y_batch

    def train_model(self):
        s_batch, a_batch, r_batch, next_s_batch, done_batch = self.get_transition_batch()
        self.model.update(*self.preprocess_batch(s_batch, a_batch, r_batch, next_s_batch, done_batch))


class Replay_Buffer(object):
    def __init__(self, buffer_size=10e6, batch_size=1):
        self.buffer_size = buffer_size
        self.batch_size = batch_size
        self.memory = deque(maxlen=buffer_size)

    def __call__(self):
        return self.memory

    def store_transition(self, transition):
        self.memory.append(transition)

    def store_transitions(self, transitions):
        self.memory.extend(transitions)

    def get_batch(self, batch_size=None):
        b_s = batch_size or self.batch_size
        cur_men_size = len(self.memory)
        if cur_men_size < b_s:
            return random.sample(list(self.memory), cur_men_size)
        else:
            return random.sample(list(self.memory), b_s)

    def memory_state(self):
        return {"buffer_size": self.buffer_size,
                "current_size": len(self.memory),
                "full": len(self.memory) == self.buffer_size}

    def empty_transition(self):
        self.memory.clear()


class DDPG_Actor(object):
    def __init__(self, state_dim, action_dim, optimizer=None, learning_rate=0.001, tau=0.001, scope="", sess=None):
        self.scope = scope
        self.sess = sess
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.learning_rate = learning_rate
        self.l2_reg = 0.01
        self.optimizer = optimizer or tf.train.AdamOptimizer(self.learning_rate)
        self.tau = tau
        self.h1_dim = 400
        self.h2_dim = 300
        # self.h3_dim = 200
        self.activation = tf.nn.relu
        self.kernel_initializer = tf.contrib.layers.variance_scaling_initializer()
        # fan-out uniform initializer which is different from original paper
        self.kernel_initializer_1 = tf.random_uniform_initializer(minval=-1 / sqrt(self.h1_dim),
                                                                  maxval=1 / sqrt(self.h1_dim))
        self.kernel_initializer_2 = tf.random_uniform_initializer(minval=-1 / sqrt(self.h2_dim),
                                                                  maxval=1 / sqrt(self.h2_dim))
        self.kernel_initializer_3 = tf.random_uniform_initializer(minval=-3e-3, maxval=3e-3)
        self.kernel_regularizer = tf.contrib.layers.l2_regularizer(self.l2_reg)

        with tf.name_scope("actor_input"):
            self.input_state = tf.placeholder(tf.float32, shape=[None, self.state_dim], name="states")

        with tf.name_scope("actor_label"):
            self.actions_grad = tf.placeholder(tf.float32, shape=[None, self.action_dim], name="actions_grad")

        self.source_var_scope = "ddpg/" + "actor_net"
        with tf.variable_scope(self.source_var_scope):
            self.action_output = self.__create_actor_network()

        self.target_var_scope = "ddpg/" + "actor_target_net"
        with tf.variable_scope(self.target_var_scope):
            self.target_net_actions_output = self.__create_target_network()

        with tf.name_scope("compute_policy_gradients"):
            self.__create_loss()

        self.train_op_scope = "actor_train_op"
        with tf.variable_scope(self.train_op_scope):
            self.__create_train_op()

        with tf.name_scope("actor_target_update_train_op"):
            self.__create_update_target_net_op()

        self.__create_get_layer_weight_op_source()
        self.__create_get_layer_weight_op_target()

    def __create_actor_network(self):
        h1 = tf.layers.dense(self.input_state,
                             units=self.h1_dim,
                             activation=self.activation,
                             kernel_initializer=self.kernel_initializer_1,
                             # kernel_initializer=self.kernel_initializer,
                             kernel_regularizer=self.kernel_regularizer,
                             name="hidden_1")

        h2 = tf.layers.dense(h1,
                             units=self.h2_dim,
                             activation=self.activation,
                             kernel_initializer=self.kernel_initializer_2,
                             # kernel_initializer=self.kernel_initializer,
                             kernel_regularizer=self.kernel_regularizer,
                             name="hidden_2")

        # h3 = tf.layers.dense(h2,
        # units=self.h3_dim,
        # activation=self.activation,
        # kernel_initializer=self.kernel_initializer,
        # kernel_regularizer=self.kernel_regularizer,
        # name="hidden_3")

        action_output = tf.layers.dense(h2,
                                        units=self.action_dim,
                                        activation=tf.nn.tanh,
                                        # activation=tf.nn.tanh,
                                        kernel_initializer=self.kernel_initializer_3,
                                        # kernel_initializer=self.kernel_initializer,
                                        kernel_regularizer=self.kernel_regularizer,
                                        use_bias=False,
                                        name="action_outputs")

        return action_output

    def __create_target_network(self):
        # get source variales and initialize
        source_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=self.source_var_scope)
        self.sess.run(tf.variables_initializer(source_vars))

        # create target network and initialize it by source network
        action_output = self.__create_actor_network()
        target_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=self.target_var_scope)

        target_init_op_list = [target_vars[i].assign(source_vars[i]) for i in range(len(source_vars))]
        self.sess.run(target_init_op_list)

        return action_output

    def __create_loss(self):
        source_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=self.source_var_scope)
        self.policy_gradient = tf.gradients(self.action_output, source_vars, -self.actions_grad)
        self.grads_and_vars = zip(self.policy_gradient, source_vars)

    def __create_train_op(self):
        self.train_policy_op = self.optimizer.apply_gradients(self.grads_and_vars,
                                                              global_step=tf.contrib.framework.get_global_step())
        train_op_vars = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES,
                                          scope=self.scope + "/" + self.train_op_scope)  # to do: remove prefix
        train_op_vars.extend(tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES, scope=self.train_op_scope))
        self.sess.run(tf.variables_initializer(train_op_vars))

    def __create_update_target_net_op(self):
        source_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=self.source_var_scope)
        target_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=self.target_var_scope)
        update_target_net_op_list = [target_vars[i].assign(self.tau * source_vars[i] + (1 - self.tau) * target_vars[i])
                                     for i in range(len(source_vars))]

        # source_net_dict = {var.name[len(self.source_var_scope):]: var for var in source_vars}
        # target_net_dict = {var.name[len(self.target_var_scope):]: var for var in target_vars}
        # keys = source_net_dict.keys()
        # update_target_net_op_list = [target_net_dict[key].assign((1-self.tau)*target_net_dict[key]+self.tau*source_net_dict[key]) \
        # for key in keys]

        # for s_v, t_v in zip(source_vars, target_vars):
        # update_target_net_op_list.append(t_v.assign(self.tau*s_v - (1-self.tau)*t_v))

        self.update_target_net_op = tf.group(*update_target_net_op_list)

    def predict_action_source_net(self, feed_state, sess=None):
        sess = sess or self.sess
        return sess.run(self.action_output, {self.input_state: feed_state})

    def predict_action_target_net(self, feed_state, sess=None):
        sess = sess or self.sess
        return sess.run(self.target_net_actions_output, {self.input_state: feed_state})

    def update_source_actor_net(self, feed_state, actions_grad, sess=None):
        sess = sess or self.sess
        batch_size = len(actions_grad)
        return sess.run([self.train_policy_op],
                        {self.input_state: feed_state,
                         self.actions_grad: actions_grad / batch_size})

    def update_target_actor_net(self, sess=None):
        sess = sess or self.sess
        return sess.run(self.update_target_net_op)

    def __create_get_layer_weight_op_source(self):
        with tf.variable_scope(self.source_var_scope, reuse=True):
            self.h1_weight_source = tf.get_variable("hidden_1/kernel")
            self.h1_bias_source = tf.get_variable("hidden_1/bias")

    def run_layer_weight_source(self, sess=None):
        sess = sess or self.sess
        return sess.run([self.h1_weight_source, self.h1_bias_source])

    def __create_get_layer_weight_op_target(self):
        with tf.variable_scope(self.target_var_scope, reuse=True):
            self.h1_weight_target = tf.get_variable("hidden_1/kernel")
            self.h1_bias_target = tf.get_variable("hidden_1/bias")

    def run_layer_weight_target(self, sess=None):
        sess = sess or self.sess
        return sess.run([self.h1_weight_target, self.h1_bias_target])


class DDPG_Critic(object):
    def __init__(self, state_dim, action_dim, optimizer=None, learning_rate=0.001, tau=0.001, scope="", sess=None):
        self.scope = scope
        self.sess = sess
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.learning_rate = learning_rate
        self.l2_reg = 0.01
        self.optimizer = optimizer or tf.train.AdamOptimizer(self.learning_rate)
        self.tau = tau
        self.h1_dim = 400
        self.h2_dim = 100
        self.h3_dim = 300
        self.activation = tf.nn.relu
        self.kernel_initializer = tf.contrib.layers.variance_scaling_initializer()
        # fan-out uniform initializer which is different from original paper
        self.kernel_initializer_1 = tf.random_uniform_initializer(minval=-1 / sqrt(self.h1_dim),
                                                                  maxval=1 / sqrt(self.h1_dim))
        self.kernel_initializer_2 = tf.random_uniform_initializer(minval=-1 / sqrt(self.h2_dim),
                                                                  maxval=1 / sqrt(self.h2_dim))
        self.kernel_initializer_3 = tf.random_uniform_initializer(minval=-1 / sqrt(self.h3_dim),
                                                                  maxval=1 / sqrt(self.h3_dim))
        self.kernel_initializer_4 = tf.random_uniform_initializer(minval=-3e-3, maxval=3e-3)
        self.kernel_regularizer = tf.contrib.layers.l2_regularizer(self.l2_reg)

        with tf.name_scope("critic_input"):
            self.input_state = tf.placeholder(tf.float32, shape=[None, self.state_dim], name="states")
            self.input_action = tf.placeholder(tf.float32, shape=[None, self.action_dim], name="actions")

        with tf.name_scope("critic_label"):
            self.y = tf.placeholder(tf.float32, shape=[None, 1], name="y")

        self.source_var_scope = "ddpg/" + "critic_net"
        with tf.variable_scope(self.source_var_scope):
            self.q_output = self.__create_critic_network()

        self.target_var_scope = "ddpg/" + "critic_target_net"
        with tf.variable_scope(self.target_var_scope):
            self.target_net_q_output = self.__create_target_network()

        with tf.name_scope("compute_critic_loss"):
            self.__create_loss()

        self.train_op_scope = "critic_train_op"
        with tf.variable_scope(self.train_op_scope):
            self.__create_train_op()

        with tf.name_scope("critic_target_update_train_op"):
            self.__create_update_target_net_op()

        with tf.name_scope("get_action_grad_op"):
            self.__create_get_action_grad_op()

        self.__create_get_layer_weight_op_source()
        self.__create_get_layer_weight_op_target()

    def __create_critic_network(self):
        h1 = tf.layers.dense(self.input_state,
                             units=self.h1_dim,
                             activation=self.activation,
                             kernel_initializer=self.kernel_initializer_1,
                             # kernel_initializer=self.kernel_initializer,
                             kernel_regularizer=self.kernel_regularizer,
                             name="hidden_1")

        # h1_with_action = tf.concat([h1, self.input_action], 1, name="hidden_1_with_action")

        h2 = tf.layers.dense(self.input_action,
                             units=self.h2_dim,
                             activation=self.activation,
                             kernel_initializer=self.kernel_initializer_2,
                             # kernel_initializer=self.kernel_initializer,
                             kernel_regularizer=self.kernel_regularizer,
                             name="hidden_2")

        h_concat = tf.concat([h1, h2], 1, name="h_concat")

        h3 = tf.layers.dense(h_concat,
                             units=self.h3_dim,
                             activation=self.activation,
                             kernel_initializer=self.kernel_initializer_3,
                             # kernel_initializer=self.kernel_initializer,
                             kernel_regularizer=self.kernel_regularizer,
                             name="hidden_3")

        # h2_with_action = tf.concat([h2, self.input_action], 1, name="hidden_3_with_action")

        q_output = tf.layers.dense(h3,
                                   units=1,
                                   # activation=tf.nn.sigmoid,
                                   activation=None,
                                   kernel_initializer=self.kernel_initializer_4,
                                   # kernel_initializer=self.kernel_initializer,
                                   kernel_regularizer=self.kernel_regularizer,
                                   name="q_output")

        return q_output

    def __create_target_network(self):
        # get source variales and initialize
        source_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=self.source_var_scope)
        self.sess.run(tf.variables_initializer(source_vars))

        # create target network and initialize it by source network
        q_output = self.__create_critic_network()
        target_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=self.target_var_scope)

        target_init_op_list = [target_vars[i].assign(source_vars[i]) for i in range(len(source_vars))]
        self.sess.run(target_init_op_list)

        return q_output

    def __create_loss(self):
        self.loss = tf.losses.mean_squared_error(self.y, self.q_output)

    def __create_train_op(self):
        self.train_q_op = self.optimizer.minimize(self.loss)
        train_op_vars = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES,
                                          scope=self.scope + "/" + self.train_op_scope)  # to do: remove prefix
        train_op_vars.extend(tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES, scope=self.train_op_scope))
        self.sess.run(tf.variables_initializer(train_op_vars))

    def __create_update_target_net_op(self):
        source_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=self.source_var_scope)
        target_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope=self.target_var_scope)
        update_target_net_op_list = [target_vars[i].assign(self.tau * source_vars[i] + (1 - self.tau) * target_vars[i])
                                     for i in range(len(source_vars))]
        # source_net_dict = {var.name[len(self.source_var_scope):]: var for var in source_vars}
        # target_net_dict = {var.name[len(self.target_var_scope):]: var for var in target_vars}
        # keys = source_net_dict.keys()
        # update_target_net_op_list = [target_net_dict[key].assign((1-self.tau)*target_net_dict[key]+self.tau*source_net_dict[key]) \
        # for key in keys]

        # for s_v, t_v in zip(source_vars, target_vars):
        # update_target_net_op_list.append(t_v.assign(self.tau*s_v - (1-self.tau)*t_v))

        self.update_target_net_op = tf.group(*update_target_net_op_list)

    def __create_get_action_grad_op(self):
        self.get_action_grad_op = tf.gradients(self.q_output, self.input_action)

    def predict_q_source_net(self, feed_state, feed_action, sess=None):
        sess = sess or self.sess
        return sess.run(self.q_output, {self.input_state: feed_state,
                                        self.input_action: feed_action})

    def predict_q_target_net(self, feed_state, feed_action, sess=None):
        sess = sess or self.sess
        return sess.run(self.target_net_q_output, {self.input_state: feed_state,
                                                   self.input_action: feed_action})

    def update_source_critic_net(self, feed_state, feed_action, feed_y, sess=None):
        sess = sess or self.sess
        return sess.run([self.train_q_op],
                        {self.input_state: feed_state,
                         self.input_action: feed_action,
                         self.y: feed_y})

    def update_target_critic_net(self, sess=None):
        sess = sess or self.sess
        return sess.run(self.update_target_net_op)

    def get_action_grads(self, feed_state, feed_action, sess=None):
        sess = sess or self.sess
        return (sess.run(self.get_action_grad_op, {self.input_state: feed_state,
                                                   self.input_action: feed_action}))[0]

    def __create_get_layer_weight_op_source(self):
        with tf.variable_scope(self.source_var_scope, reuse=True):
            self.h1_weight_source = tf.get_variable("hidden_1/kernel")
            self.h1_bias_source = tf.get_variable("hidden_1/bias")

    def run_layer_weight_source(self, sess=None):
        sess = sess or self.sess
        return sess.run([self.h1_weight_source, self.h1_bias_source])

    def __create_get_layer_weight_op_target(self):
        with tf.variable_scope(self.target_var_scope, reuse=True):
            self.h1_weight_target = tf.get_variable("hidden_1/kernel")
            self.h1_bias_target = tf.get_variable("hidden_1/bias")

    def run_layer_weight_target(self, sess=None):
        sess = sess or self.sess
        return sess.run([self.h1_weight_target, self.h1_bias_target])


class Model(object):
    def __init__(self,
                 state_dim,
                 action_dim,
                 optimizer=None,
                 actor_learning_rate=1e-4,
                 critic_learning_rate=1e-3,
                 tau=0.001,
                 sess=None):
        self.state_dim = state_dim
        self.action_dim = action_dim
        self.actor_learning_rate = actor_learning_rate
        self.critic_learning_rate = critic_learning_rate
        self.tau = tau

        # tf.reset_default_graph()
        self.sess = sess or tf.Session()

        self.global_step = tf.Variable(0, name="global_step", trainable=False)
        global_step_vars = tf.get_collection(tf.GraphKeys.GLOBAL_VARIABLES, scope="global_step")
        self.sess.run(tf.variables_initializer(global_step_vars))

        self.actor_scope = "actor_net"
        with tf.name_scope(self.actor_scope):
            self.actor = DDPG_Actor(self.state_dim,
                                    self.action_dim,
                                    learning_rate=self.actor_learning_rate,
                                    tau=self.tau,
                                    scope=self.actor_scope,
                                    sess=self.sess)

        self.critic_scope = "critic_net"
        with tf.name_scope(self.critic_scope):
            self.critic = DDPG_Critic(self.state_dim,
                                      self.action_dim,
                                      learning_rate=self.critic_learning_rate,
                                      tau=self.tau,
                                      scope=self.critic_scope,
                                      sess=self.sess)

    def update(self, state_batch, action_batch, y_batch, sess=None):
        sess = sess or self.sess
        self.critic.update_source_critic_net(state_batch, action_batch, y_batch, sess)
        action_batch_for_grad = self.actor.predict_action_source_net(state_batch, sess)
        action_grad_batch = self.critic.get_action_grads(state_batch, action_batch_for_grad, sess)
        self.actor.update_source_actor_net(state_batch, action_grad_batch, sess)

        self.critic.update_target_critic_net(sess)
        self.actor.update_target_actor_net(sess)

    def predict_action(self, observation, sess=None):
        sess = sess or self.sess
        return self.actor.predict_action_source_net(observation, sess)
