class Report:

    PAGE_LINES = 50
    PAGE_WIDTH = 80

    def __init__(self, rptfn):
        self.rptfh = open(rptfn, "w")
        self.rptln = 0
        self.rightfmt = "-%%%ds\r\n" % self.PAGE_WIDTH

    def __del__(self):
        self.rptfh.close()

    def leftline(self, line="", stdout=False):
        self.rptln += 1
        self.rptfh.write(line + "\r\n")
        if stdout:
            print(line)

    def rightline(self, line="", stdout=False):
        self.rptln += 1
        self.rptfh.write(self.rightfmt % line)
        if stdout:
            print(line)

    def gotoline(self, ln):
        ln %= self.PAGE_LINES
        if ln < self.rptln: # next page
            ln += self.PAGE_LINES
        while self.rptln < ln:
            self.leftline()
