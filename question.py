import re
import math
import random
import config

class Pattern:
    token = re.compile(r'\d+|[\*/\+-]+|[\(\)]|\s+')
    num = re.compile(r'\d+')
    op = re.compile(r'[\*/\+-]+')

class Question:

    def __init__(self, expr):
        self.expr = expr

    def valid(self):
        try:
            result = eval(self.expr)
        except:
            return False
        if result < 1 and result != 0:
            return False
        if result > config.MAX_ANWSER:
            return False
        return True

    def anwser(self):
        if self.expr.find('/') < 0:
            v = eval(self.expr)
            return str(v)
        e1 = self.expr.replace('/', '//')
        e2 = self.expr.replace('/', '%')
        v = eval(e1)
        r = eval(e2)
        ret = str(v)
        if r > 0:
            ret += '...%d' % r
        return ret

    def numlen(matched):
        item = matched.group('num')
        return str(len(item))

    def type1(self):
        s = self.expr.replace(' ', '')
        s = re.sub('(?P<num>\d+)', Question.numlen, s)
        return s

    def type(self):
        nums = Pattern.num.findall(self.expr)
        #print(nums)
        ops = Pattern.op.findall(self.expr)
        tr = str.maketrans({'+': '+-', '-': '+-'})
        s = set(map(lambda x: x.translate(tr), ops))
        ops2 = list(s)
        ops2.sort()
        ncount = len(nums)
        nsize = max(list(map(len, nums)))
        sops = ''.join(ops2)
        r = "%d.%d%s" % (ncount, nsize, sops)
        return r

class Generator:

    def __init__(self, templates = None):
        if templates is None:
            self.templates = [
                "99 +-* 99",
                "999 / 99",
                "999 +- 999"
            ]
        else:
            self.templates = templates

    def expression(self, template):
        tokens = Pattern.token.findall(template)
        #print(tokens)
        expr = ""
        for token in tokens:
            if Pattern.num.match(token):
                maxv = int(token)
                if config.STRICT_LEN:
                    minv = 10 ** math.floor(math.log(maxv, 10))
                else:
                    minv = 1
                expr += str(random.randint(minv, maxv))
            elif Pattern.op.match(token):
                expr += random.choice(token)
            else:
                expr += token
        return expr

    def question(self, template=None):
        if template is None:
            template = random.choice(self.templates)
        while True:
            expr = self.expression(template)
            q = Question(expr)
            if q.valid():
                return q

