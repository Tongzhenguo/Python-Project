__author__ = 'YYT'
def makeStopWord(self) :
     with open("stop_word.txt", "r") as stop_file :
         self.stop_word = stop_file.read()
     self.stop_word = self.stop_word.split()
