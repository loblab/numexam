#!/usr/bin/python3

from question import *
import time

class Exam:

    def __init__(self, total=10):
        templates = [
            "100 +- 100",
            "100 * 100",
            "1000 / 100",
            "1000 +- 1000 +- 1000",
            "1000 +- 1000",
        ]
        self.qbank = Question(templates)
        self.total = total

    def opendb(self):
        self.dbfile = "record.txt"
        self.dbfh = open(self.dbfile, "w")

    def closedb(self):
        self.dbfh.close()

    def record(self, question, anwser0, anwser, result, dur):
        flag = "O" if result else "X (%s)" % anwser0
        line = "%2d. %15s = %-8s %-12s %4.1fs\r\n" % (
            self.index, question,
            anwser, flag,
            dur)
        self.dbfh.write(line)

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
                self.record(question, anwser0, anwser, True, dur)
                return True
            else:
                err = 1
                self.wrong += 1
                self.record(question, anwser0, anwser, False, dur)
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
        self.opendb()
        self.index = 0
        self.correct = 0
        self.wrong = 0
        self.dur = 0
        while self.correct < self.total and self.round():
            print("")
        self.report()
        self.closedb()

if __name__ == "__main__":
    exam = Exam(20)
    exam.run()

