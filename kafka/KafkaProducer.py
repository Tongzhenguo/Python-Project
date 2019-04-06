# encoding: utf-8


"""


@author: tongzhenguo


@time: 2018/12/7 上午9:38


@desc:


"""
import os
import time
from pykafka import KafkaClient


class KafkaTest(object):
    """
    测试kafka常用api
    """

    def __init__(self, host="192.168.237.129:9092"):
        self.host = host
        self.client = KafkaClient(hosts=self.host)

    def producer_partition(self):
        """
        生产者分区查看，主要查看生产消息时offset的变化
        :return:
        """
        topic = self.client.topics["test_topic".encode()]
        partitions = topic.partitions
        print (u"查看所有分区 {}".format(partitions))

        earliest_offset = topic.earliest_available_offsets()
        print(u"获取最早可用的offset {}".format(earliest_offset))

        # 生产消息之前看看offset
        last_offset = topic.latest_available_offsets()
        print(u"最近可用offset {}".format(last_offset))

        # 同步生产消息
        p = topic.get_producer(sync=True)
        p.produce(str(time.time()).encode())

        # 查看offset的变化
        last_offset = topic.latest_available_offsets()
        print(u"最近可用offset {}".format(last_offset))

    def producer_designated_partition(self):
        """
        往指定分区写消息，如果要控制打印到某个分区，
        需要在获取生产者的时候指定选区函数，
        并且在生产消息的时候额外指定一个key
        :return:
        """

        def assign_patition(pid, key):
            """
            指定特定分区, 这里测试写入第一个分区(id=0)
            :param pid: 为分区列表
            :param key:
            :return:
            """
            print("为消息分配partition {} {}".format(pid, key))
            return pid[0]

        topic = self.client.topics["test_topic".encode()]
        p = topic.get_producer(sync=True, partitioner=assign_patition)
        p.produce(str(time.time()).encode(), partition_key=b"partition_key_0")

    def async_produce_message(self):
        """
        异步生产消息，消息会被推到一个队列里面，
        另外一个线程会在队列中消息大小满足一个阈值（min_queued_messages）
        或到达一段时间（linger_ms）后统一发送,默认5s
        :return:
        """
        topic = self.client.topics["kafka_test".encode()]
        last_offset = topic.latest_available_offsets()
        print("最近的偏移量 offset {}".format(last_offset))

        # 记录最初的偏移量
        old_offset = last_offset[0].offset[0]
        p = topic.get_producer(sync=False, partitioner=lambda pid, key: pid[0])
        p.produce(str(time.time()).encode())
        s_time = time.time()
        while True:
            last_offset = topic.latest_available_offsets()
            print("最近可用offset {}".format(last_offset))
            if last_offset[0].offset[0] != old_offset:
                e_time = time.time()
                print('cost time {}'.format(e_time - s_time))
                break
            time.sleep(1)

    def get_produce_message_report(self):
        """
        查看异步发送消报告,默认会等待5s后才能获得报告
        """
        topic = self.client.topics["kafka_test".encode()]
        last_offset = topic.latest_available_offsets()
        print("最近的偏移量 offset {}".format(last_offset))
        p = topic.get_producer(sync=False, delivery_reports=True, partitioner=lambda pid, key: pid[0])
        p.produce(str(time.time()).encode())
        s_time = time.time()
        delivery_report = p.get_delivery_report()
        e_time = time.time()
        print ('等待{}s, 递交报告{}'.format(e_time - s_time, delivery_report))
        last_offset = topic.latest_available_offsets()
        print("最近的偏移量 offset {}".format(last_offset))


if __name__ == '__main__':
    pwd = os.path.split(os.path.realpath(__file__))[0]
    kafka_ins = KafkaTest()
    # kafka_ins.producer_partition()
    # kafka_ins.producer_designated_partition()
    # kafka_ins.async_produce_message()
    kafka_ins.get_produce_message_report()
