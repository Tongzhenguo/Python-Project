import insuranceqa_data as insuranceqa

###
# train_data = insuranceqa.load_pool_train()
# test_data = insuranceqa.load_pool_test()
# valid_data = insuranceqa.load_pool_valid()


# for x in train_data:
#     print('index %s value: %s ++%s++ %s ++$++ %s' % \
#         (  x, train_data[x]['zh'], train_data[x]['en'], train_data[x]['answers'], train_data[x]['negatives']))

# answers_data = insuranceqa.load_pool_answers()
# for x in answers_data:
#     print('index %s: %s ++$++ %s' % (x, answers_data[x]['zh'], answers_data[x]['en'] ))


### 问答对预料，基于HanLP分词
# train_data = insuranceqa.load_pairs_train()
# test_data = insuranceqa.load_pairs_test()
# valid_data = insuranceqa.load_pairs_valid()

# for x in test_data:
#     print('index %s value: %s ++$++ %s ++$++ %s' % \
#     (x['qid'], x['question'], x['utterance'], x['label']))

# vocab_data = insuranceqa.load_pairs_vocab()
# print( vocab_data['word2id']['UNKNOWN'] )
# print( vocab_data['id2word'] )
# print( vocab_data['tf'] )
# print( vocab_data['total'] )

