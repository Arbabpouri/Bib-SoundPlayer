# in the name of god | Github : github.com/Arbabpouri | Telegram : t.me/SardarCybery

from random import randint
from winsound import Beep

class Bib:
   def __init__(self,Number) -> None:
      """
      Args:
          Number (int): Number of play
      """
      self.number = Number

   def PlayBeep(self,Freq,Time):
      """
      Args:
          Freq (int): Sound frequent
          Time (int): Time for play | MS
      """
      if isinstance(Freq,int) and isinstance(Time,int) and isinstance(self.number,int) and self.number > 0:
         print('Start')
         try:
            while self.number > 0:
               Beep(Freq,Time)
               self.number -= 1
            print('Ended')
         except KeyboardInterrupt:
            print('you got out')
         except Exception as ex:
            print(str(ex))
      else:
         print('The arguments are not correct')
   
   def PlayMusic(self):
      if isinstance(self.number,int) and self.number > 0:
         try:
            while self.number > 0:
               Beep(randint(100,1200), randint(300,500))
               self.number -= 1
            print('Ended')
         except KeyboardInterrupt:
            print('you got out')
         except Exception as ex:
            print(str(ex))
      else:
         print('Number not is int')
