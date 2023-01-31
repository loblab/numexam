#!/usr/bin/python3

import time
import config
from question import *
from report import *

TITLE = "Number Exam"
ABOUT = "Num Exam ver 0.9, 1/31/2023, https://github.com/loblab/numexam"

class Counter:
    COLS = 3

    def __init__(self):
        self.etype = {}
        self.ctype = {}

    def count(self, question, result):
        qtype = question.type()
        try:
            self.ctype[qtype] += 1
        except:
            self.ctype[qtype] = 1
            self.etype[qtype] = 0
        if not result:
            self.etype[qtype] += 1

    def summary(self):
        lines = []
        line = ""
        items = 0
        for key in self.ctype:
            total = self.ctype[key]
            err = self.etype[key]
            ok = total - err
            score = round(100.0 * ok / total)
            ss = "%3d(%d/%d)" % (score, err, total)
            line += "%8s:%-12s" % (key, ss)
            items += 1
            if items % self.COLS == 0:
                lines.append(line)
                line = ""
        if len(line) > 0:
            lines.append(line)
        return lines

class Exam:
    CORRECT = '✅'
    WRONG = '❌'
    L_CORRECT = len(CORRECT)
    L_WRONG = len(WRONG)

    def __init__(self, qtypes, minitem, mintime):
        self.generator = Generator(qtypes)
        self.qtypes = qtypes
        self.minitem = minitem
        self.mintime = mintime

    def open(self):
        print(ABOUT)
        print()
        lt = time.localtime(time.time())
        rptfn = time.strftime("%Y%m%d-%H%M.txt", lt)
        tstr = time.strftime("%H:%M:%S %m/%d/%Y", lt)
        self.report = Report(rptfn)
        line = "%3s%-22s %-14s %20s" % (' ', TITLE, config.USER_NAME, tstr)
        self.report.leftline(line, True)
        self.report.leftline('=' * 64, True)

    def record(self, question, anwser0, anwser, result, dur):
        flag = self.CORRECT if result else "%s (%s)" % (self.WRONG, anwser0)
        line = "%3d. %18s = %-10s %-14s %6.1fs" % (
            self.index, question.expr,
            anwser, flag,
            dur)
        self.report.leftline(line)
        self.counter.count(question, result)

    def round(self):
        self.index += 1
        print()
        print("%8s: %d/%d" % ("No.", self.index, self.minitem))
        question = self.generator.question()
        print("%8s: %s" % ("Question", question.expr))
        anwser0 = question.anwser()
        retry = 0
        while True:
            t1 = time.time()
            while True:
                anwser = input("%8s: " % "???").strip().lower()
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
                print(f'%{8-self.L_CORRECT}s! %.1fs' % (self.CORRECT, dur))
                self.correct += 1
                self.record(question, anwser0, anwser, True, dur)
                return True
            else:
                self.wrong += 1
                self.record(question, anwser0, anwser, False, dur)
                print(f'%{8-self.L_WRONG}s! %.1fs' % (self.WRONG, dur))
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
            line = "%8s:%5ds %9s: %5.1fs %27s" % ("Cost", round(self.dur), "Avg", avg, tstr)
            self.report.leftline(line, True)
            line = f'%{8-self.L_CORRECT}s:%5d %{10-self.L_WRONG}s: %3d' % (self.CORRECT, self.correct, self.WRONG, self.wrong)
            self.report.leftline(line, True)
            self.report.leftline('-' * 32, True)
            score = round(100.0 * self.correct / done)
            line = "%25s: %3d" % ("Score", score)
            self.report.leftline(line, True)
            print()

        rows = self.counter.summary()
        rows.append(ABOUT)
        footersize = len(rows)
        self.report.gotoline(-footersize)
        for r in rows:
            self.report.rightline(r)

        #if self.correct >= self.minitem:
        #    self.report.print()

        print("Bye! See you next time.")
        print()

    def run(self):
        self.open()
        self.index = 0
        self.correct = 0
        self.wrong = 0
        self.dur = 0
        self.counter = Counter()
        while self.correct < self.minitem or self.dur < self.mintime:
            if not self.round():
                break
        self.close()

if __name__ == "__main__":
    exam = Exam(config.EXAM_TYPES, config.EXAM_ITEMS, config.EXAM_TIME)
    exam.run()


