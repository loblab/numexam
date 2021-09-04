from question import *
import time

class Examiner:

    def __init__(self):
        templates = [
            "100 +- 100",
            "100 * 100",
            "1000 / 100",
            "1000 +- 1000"
        ]
        self.qbank = Question(templates)

    def round(self):
        question = self.qbank.question()
        print("Question: " + question)
        anwser0 = str(int(self.qbank.anwser(question)))
        retry = 0
        while True:
            t1 = time.time()
            anwser = input("  Anwser: ").strip().lower()
            t2 = time.time()
            dur = t2 - t1
            if anwser == "bye" or anwser == "quit":
                return False
            if anwser == "next" or anwser == "skip":
                return True
            elif anwser == anwser0:
                print(" CORRECT! %.1fs" % dur)
                err = 0
                return True
            else:
                err = 1
                print("   WRONG! %.1fs" % dur)
            retry += 1
        return True

    def run(self):
        while self.round():
            print("")
        print("")
        print("Bye! See you next time.")
        print("")

if __name__ == "__main__":
    ex = Examiner()
    ex.run()


