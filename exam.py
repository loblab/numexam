#!/usr/bin/python3

import time
import config
from question import *
from report import *

TITLE = "  Number Exam"
ABOUT = "Num Exam ver 0.4, 9/5/2021, https://github.com/loblab/numexam"

class Exam:

    def __init__(self, qtypes, minitem, mintime):
        self.qbank = Question(qtypes)
        self.qtypes = qtypes
        self.minitem = minitem
        self.mintime = mintime

    def open(self):
        lt = time.localtime(time.time())
        rptfn = time.strftime("%Y%m%d-%H%M.txt", lt)
        self.report = Report(rptfn)
        self.report.leftline(TITLE)
        self.report.leftline('-' * 32)
        tstr = time.strftime("%H:%M:%S %m/%d/%Y", lt)
        self.report.leftline("   Name: %s" % config.USER_NAME, True)
        self.report.leftline("  Start: %s" % tstr, True)
        self.report.leftline('=' * 64)

    def record(self, question, anwser0, anwser, result, dur):
        flag = "O" if result else "X (%s)" % anwser0
        line = "%3d. %18s = %-10s %-15s %5.1fs" % (
            self.index, question,
            anwser, flag,
            dur)
        self.report.leftline(line)

    def round(self):
        self.index += 1
        print()
        print("     No.: %d/%d" % (self.index, self.minitem))
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

    def close(self):
        print()
        done = self.correct + self.wrong
        if self.correct > 0:
            self.report.leftline('=' * 64)
            lt = time.localtime(time.time())
            tstr = time.strftime("%H:%M:%S %m/%d/%Y", lt)
            self.report.leftline(" Finish: %s" % tstr, True)
            self.report.leftline("   Cost: %5.1fs      Avg: %5.1fs" % (self.dur, self.dur / self.correct), True)
            self.report.leftline("Correct: %3d       Wrong: %3d" % (self.correct, self.wrong), True)
            self.report.leftline('-' * 32)
            self.report.leftline("                   Score: %3d" % (100.0 * self.correct / done + 0.5), True)
            print()

        footersize = len(self.qtypes) + 3
        self.report.gotoline(-footersize)
        self.report.rightline("[Config] exam types:")
        for qtype in self.qtypes:
            self.report.rightline(qtype + " <")
        self.report.rightline("[Config] min items: %d; min time: %ds" % (self.minitem, self.mintime))
        self.report.rightline(ABOUT)

        print("Bye! See you next time.")
        print()

    def run(self):
        self.open()
        self.index = 0
        self.correct = 0
        self.wrong = 0
        self.dur = 0
        while self.correct < self.minitem or self.dur < self.mintime:
            if not self.round():
                break
        self.close()

if __name__ == "__main__":
    exam = Exam(config.EXAM_TYPES, config.EXAM_ITEMS, config.EXAM_TIME)
    exam.run()


