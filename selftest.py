#!/usr/bin/python3

import os
import time
import random
import config
from question import *
from exam import *

def test1():
    q = Question("50 / 40")
    print(q.anwser())
    q = Question("40 / 50")
    print(q.anwser())

def test2():
    rptfile = "20210905-2235.txt"
    os.startfile(rptfile, "print")

def test3():
    print('=' * 64)
    print("%7s:%5ds %9s: %5.1fs %28s" % (
        "Cost", 1896, "Avg", 75.8,
        "18:32:09 09/06/2021"))
    print("%7s:%5d %10s: %3d" % (
        "Correct", 25, "Wrong", 7))
    print('-' * 32)
    print("%24s: %3d" % ("Score", 94))

def test4():
    q = Question("500 / 40")
    print(q.expr)
    print(q.type())

def test5():
    templates = [
        "99 +-* 99",
        "999 / 99",
        "999 +- 999",
        "999 +-* 999 +-* 999",
    ]
    g = Generator(templates)
    c = Counter()
    for _ in range(1000):
        q = g.question()
        print(q.expr)
        r = random.choice([True, False, True])
        c.count(q, r)
    rows = c.summary()
    for row in rows:
        print(row)

test5()

