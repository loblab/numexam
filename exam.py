#!/usr/bin/python3

from question import *
import time

class Exam:

    def __init__(self, total=10):
        templates = [
            "100 +- 100",
            "100 * 100",
            "1000 / 100",
            "1000 +- 1000"
        ]
        self.qbank = Question(templates)
        self.total = total

    def round(self):
        self.index += 1
        print("     No.: %d/%d" % (self.index, self.total))
        question = self.qbank.question()
        print("Question: " + question)
        anwser0 = self.qbank.anwser(question)
        retry = 0
        while True:
            t1 = time.time()
            anwser = input("  Anwser: ").strip().lower()
            t2 = time.time()
            dur = t2 - t1
            self.dur += dur
            if len(anwser) < 1:
                continue
            if anwser == "bye" or anwser == "quit":
                return False
            if anwser == "next" or anwser == "skip":
                return True
            elif anwser == anwser0:
                print(" CORRECT! %.1fs" % dur)
                err = 0
                self.correct += 1
                return True
            else:
                err = 1
                self.wrong += 1
                print("   WRONG! %.1fs" % dur)
            retry += 1
        return True

    def report(self):
        print("")
        done = self.correct + self.wrong
        if done > 0:
            print("   Cost: %5.1fs, Average: %5.1fs" % (self.dur, self.dur / done))
            print("Correct: %3d,      Wrong: %3d" % (self.correct, self.wrong))
            print("  Score: %3d" % (100.0 * self.correct / done + 0.5))
            print("")
        print("Bye! See you next time.")
        print("")

    def run(self):
        self.index = 0
        self.correct = 0
        self.wrong = 0
        self.dur = 0
        while self.correct < self.total and self.round():
            print("")
        self.report()

if __name__ == "__main__":
    exam = Exam()
    exam.run()


