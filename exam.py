#!/usr/bin/python3

import time
import config
from question import *
from report import *

TITLE = "Number Exam"
ABOUT = "Num Exam ver 0.5, 9/6/2021, https://github.com/loblab/numexam"

class Exam:

    def __init__(self, qtypes, minitem, mintime):
        self.qbank = Question(qtypes)
        self.qtypes = qtypes
        self.minitem = minitem
        self.mintime = mintime

    def open(self):
        lt = time.localtime(time.time())
        rptfn = time.strftime("%Y%m%d-%H%M.txt", lt)
        tstr = time.strftime("%H:%M:%S %m/%d/%Y", lt)
        self.report = Report(rptfn)
        line = "%3s%-22s %-14s %20s" % (' ', TITLE, config.USER_NAME, tstr)
        self.report.leftline(line, True)
        self.report.leftline('=' * 64, True)

    def record(self, question, anwser0, anwser, result, dur):
        flag = "O" if result else "X (%s)" % anwser0
        line = "%3d. %18s = %-10s %-15s %6.1fs" % (
            self.index, question,
            anwser, flag,
            dur)
        self.report.leftline(line)

    def round(self):
        self.index += 1
        print()
        print("%8s: %d/%d" % ("No.", self.index, self.minitem))
        question = self.qbank.question()
        print("%8s: %s" % ("Question", question))
        anwser0 = self.qbank.anwser(question)
        retry = 0
        while True:
            t1 = time.time()
            while True:
                anwser = input("%8s: " % "Anwser").strip().lower()
                t2 = time.time()
                if len(anwser) < 1:
                    continue
                if anwser == "help" or anwser == "debug":
                    print("%8s: %s" % ("Debug", anwser0))
                    continue
                elif anwser == "next" or anwser == "skip":
                    return True
                elif anwser == "bye" or anwser == "quit":
                    return False
                break
            dur = t2 - t1
            self.dur += dur
            if anwser == anwser0:
                print("%8s! %.1fs" % ("CORRECT", dur))
                self.correct += 1
                self.record(question, anwser0, anwser, True, dur)
                return True
            else:
                self.wrong += 1
                self.record(question, anwser0, anwser, False, dur)
                print("%8s! %.1fs" % ("WRONG", dur))
            retry += 1
        return True

    def close(self):
        print()
        done = self.correct + self.wrong
        if self.correct > 0:
            lt = time.localtime(time.time())
            tstr = time.strftime("%H:%M:%S %m/%d/%Y", lt)
            self.report.leftline('=' * 64, True)
            avg = self.dur / self.correct
            line = "%7s:%5ds %9s: %5.1fs %28s" % ("Cost", round(self.dur), "Avg", avg, tstr)
            self.report.leftline(line, True)
            line = "%7s:%5d %10s: %3d" % ("Correct", self.correct, "Wrong", self.wrong)
            self.report.leftline(line, True)
            self.report.leftline('-' * 32, True)
            score = round(100.0 * self.correct / done)
            line = "%24s: %3d" % ("Score", score)
            self.report.leftline(line, True)
            print()

        footersize = len(self.qtypes) + 3
        self.report.gotoline(-footersize)
        self.report.rightline("[Config] exam types:")
        for qtype in self.qtypes:
            self.report.rightline(qtype + " <")
        self.report.rightline("[Config] min items: %d; min time: %ds" % (self.minitem, self.mintime))
        self.report.rightline(ABOUT)
        if self.correct >= self.minitem:
            self.report.print()

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


