#!/usr/bin/python3

import time
import config
from question import *

class Exam:

    def __init__(self, types, total=10):
        self.qbank = Question(types)
        self.types = types
        self.total = total

    def open(self):
        lt = time.localtime(time.time())
        dbfile = time.strftime("%Y%m%d-%H%M.txt", lt)
        self.dbfh = open(dbfile, "w")
        self.writeline("  Number Exam")
        self.writeline('-' * 32)
        tstr = time.strftime("%H:%M:%S %m/%d/%Y", lt)
        self.writeline("   Name: %s" % config.USER_NAME)
        self.writeline("  Start: %s" % tstr)
        self.writeline('=' * 64)

    def close(self):
        self.dbfh.close()

    def writeline(self, line, stdout=False):
        self.dbfh.write(line + "\r\n")
        if stdout:
            print(line)

    def record(self, question, anwser0, anwser, result, dur):
        flag = "O" if result else "X (%s)" % anwser0
        line = "%3d. %18s = %-10s %-15s %5.1fs" % (
            self.index, question,
            anwser, flag,
            dur)
        self.writeline(line)

    def round(self):
        self.index += 1
        print("     No.: %d/%d" % (self.index, self.total))
        question = self.qbank.question()
        print("Question: " + question)
        anwser0 = self.qbank.anwser(question)
        retry = 0
        while True:
            t1 = time.time()
            while True:
                anwser = input("  Anwser: ").strip().lower()
                t2 = time.time()
                if len(anwser) < 1:
                    continue
                if anwser == "help" or anwser == "debug":
                    print("   Debug: %s" % anwser0)
                    continue
                elif anwser == "next" or anwser == "skip":
                    return True
                elif anwser == "bye" or anwser == "quit":
                    return False
                break
            dur = t2 - t1
            self.dur += dur
            if anwser == anwser0:
                print(" CORRECT! %.1fs" % dur)
                self.correct += 1
                self.record(question, anwser0, anwser, True, dur)
                return True
            else:
                self.wrong += 1
                self.record(question, anwser0, anwser, False, dur)
                print("   WRONG! %.1fs" % dur)
            retry += 1
        return True

    def report(self):
        print()
        done = self.correct + self.wrong
        if self.correct > 0:
            self.writeline('=' * 64)
            lt = time.localtime(time.time())
            tstr = time.strftime("%H:%M:%S %m/%d/%Y", lt)
            self.writeline(" Finish: %s" % tstr)
            self.writeline("   Cost: %5.1fs      Avg: %5.1fs" % (self.dur, self.dur / self.correct), True)
            self.writeline("Correct: %3d       Wrong: %3d" % (self.correct, self.wrong), True)
            self.writeline(' ' * 16 + '-' * 32)
            self.writeline("                   Score: %3d" % (100.0 * self.correct / done + 0.5), True)
            print()
        print("Bye! See you next time.")
        print()

    def run(self):
        self.open()
        self.index = 0
        self.correct = 0
        self.wrong = 0
        self.dur = 0
        while self.correct < self.total and self.round():
            print()
        self.report()
        self.close()

if __name__ == "__main__":
    exam = Exam(config.EXAM_TYPES, config.EXAM_TOTAL)
    exam.run()


