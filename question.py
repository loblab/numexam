import re
import random

class Question:

    def __init__(self, templates = None):
        self.p_token = re.compile(r'\d+|[\*/\+-]+|[\(\)]|\s+')
        self.p_num = re.compile(r'\d+')
        self.p_op = re.compile(r'[\*/\+-]+')
        if templates is None:
            self.templates = [
                "100 +-* 100",
                "1000 +- 1000"
            ]
        else:
            self.templates = templates

    def expression(self, template):
        tokens = self.p_token.findall(template)
        #print(tokens)
        expr = ""
        for token in tokens:
            if self.p_num.match(token):
                expr += str(random.randint(1, int(token)))
            elif self.p_op.match(token):
                expr += random.choice(token)
            else:
                expr += token
        return expr

    def anwser(self, expr):
        e1 = expr.replace('/', '//')
        e2 = expr.replace('/', '%')
        v = eval(e1)
        r = eval(e2)
        ret = str(v)
        if r > 0:
            ret += '...%d' % r
        return ret

    def valid(self, expr):
        result = eval(expr)
        if result < 0:
            return False
        return True

    def question(self, template=None):
        if template is None:
            template = random.choice(self.templates)
        while True:
            expr = self.expression(template)
            if self.valid(expr):
                return expr


