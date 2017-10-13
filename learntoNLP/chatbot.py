from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

'''
https://github.com/Tongzhenguo/ChatterBot
'''
chatbot = ChatBot(
    'Ron Obvious',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus and Get a response
# chatbot.train("chatterbot.corpus.english")
# print( chatbot.get_response("Hello, how are you today?") )

# Train based on the chinesr corpus


deepThought = ChatBot("deepThought")
deepThought.set_trainer(ChatterBotCorpusTrainer)
# 使用中文语料库训练它
# deepThought.train("chatterbot.corpus.chinese")  # 语料库

print(deepThought.get_response("很高兴认识你"))
print(deepThought.get_response("嗨，最近如何?"))
print(deepThought.get_response("复杂优于晦涩")) #语出 The Zen of Python
print(deepThought.get_response("面对模棱两可，拒绝猜测的诱惑."))
print(deepThought.get_response("生命、宇宙以及世间万物的终极答案是什么?"))

# 设置自己的训练集
my_bot = ChatBot("Training demo")
my_bot.set_trainer(ListTrainer)
my_bot.train([
    "嗳，渡边君，真喜欢我?",
    "那还用说?",
    "那么，可依得我两件事?",
    "三件也依得",
])

# test
print(my_bot.get_response("真喜欢我?"))
print(my_bot.get_response("可依得我两件事?"))

