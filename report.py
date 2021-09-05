import os

class Report:

    PAGE_LINES = 50
    PAGE_WIDTH = 80

    def __init__(self, rptfn):
        self.rptfn = rptfn
        self.rptfh = open(rptfn, "w")
        self.rptln = 0
        self.rightfmt = "%%%ds\n" % self.PAGE_WIDTH

    def __del__(self):
        self.rptfh.close()

    def leftline(self, line="", stdout=False):
        self.rptln += 1
        self.rptfh.write(line + "\n")
        self.rptfh.flush()
        if stdout:
            print(line)

    def rightline(self, line="", stdout=False):
        self.rptln += 1
        self.rptfh.write(self.rightfmt % line)
        self.rptfh.flush()
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

