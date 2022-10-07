import os
from pathlib import Path

class Report:

    PAGE_LINES = 50
    PAGE_WIDTH = 80

    def __init__(self, rptfn):
        rptdir = Path('report')
        rptdir.mkdir(parents=True, exist_ok=True)
        self.rptfn = rptdir / rptfn
        self.rptfh = open(self.rptfn, "w", encoding="utf-8")
        self.rptln = 0
        self.rightfmt = "%%%ds\n" % self.PAGE_WIDTH

    def __del__(self):
        self.rptfh.close()

    def write(self, line):
        self.rptfh.write(line) #.encode('utf8'))
        self.rptfh.flush()

    def leftline(self, line="", stdout=False):
        self.rptln += 1
        self.write(line + "\n")
        if stdout:
            print(line)

    def rightline(self, line="", stdout=False):
        self.rptln += 1
        self.write(self.rightfmt % line)
        if stdout:
            print(line)

    def gotoline(self, ln):
        ln %= self.PAGE_LINES
        if ln < self.rptln: # next page
            ln += self.PAGE_LINES
        while self.rptln < ln:
            self.leftline()

    def print(self):
        try:
            os.startfile(self.rptfn, "print")
        except:
            print("FAILED to print report %s" % self.rptfn)
        else:
            print("Printing report %s ..." % self.rptfn)

