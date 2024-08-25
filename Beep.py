from random import randint
from winsound import Beep

class Bib:
    def __init__(self, number: int) -> None:
        """
        Initialize the Bib class with the number of plays.

        Args:
            number (int): Number of plays.
        """
        self.number = number

    def play_beep(self, freq: int, time: int) -> None:
        """
        Play a beep sound a specified number of times.

        Args:
            freq (int): Sound frequency.
            time (int): Duration for which the sound plays (in milliseconds).
        """
        if isinstance(freq, int) and isinstance(time, int) and isinstance(self.number, int) and self.number > 0:
            print('Start')
            try:
                while self.number > 0:
                    Beep(freq, time)
                    self.number -= 1
                print('Ended')
            except KeyboardInterrupt:
                print('You exited the program.')
            except Exception as ex:
                print(str(ex))
        else:
            print('The arguments are not correct.')

    def play_music(self) -> None:
        """Play random music by generating random frequencies and durations."""
        if isinstance(self.number, int) and self.number > 0:
            try:
                while self.number > 0:
                    Beep(randint(100, 1200), randint(300, 500))
                    self.number -= 1
                print('Ended')
            except KeyboardInterrupt:
                print('You exited the program.')
            except Exception as ex:
                print(str(ex))
        else:
            print('Number is not an integer.')

if __name__ == "__main__":
    obj = Bib(20)
    obj.play_music()
