# Number exam for kids （小学生算术练习题）

Auto generate number question and auto check

小学算术题，自动出题，自动批改。可配置题型，每次练习题的数目和练习时间。
做错的当场重做，直到做对为止。

- Features: supports customizing question types, exam time and item amount
- Platform: Windows/Linux/MacOS, Python 3.x
- Ver: 0.3
- Updated: 9/5/2021
- Created: 9/4/2021
- Author: loblab

![Session of number exam](https://raw.githubusercontent.com/loblab/numexam/master/screenshot.png)

## Usage

- [Install Python 3.x](https://www.python.org/downloads/)
- Modify config.py
- Run "python3 exam.py"

## 使用说明

- 首先你必须有Python 3.x的环境，[从这里安装](https://www.python.org/downloads/)
- 根据你的需要，修改配置文件config.py，在这里你可以配置练习题的数量，练习时间，题目类型等
- 运行 "python3 exam.py"
- 结束后，在当前目录下会生成报告文件，相当于完整的试卷及结果，参考[sample-report.txt](sample-report.txt)

## 配置文件说明

- USER_NAME = "Kitty" 学生姓名，可写中文
- MAX_ANWSER = 9999 出的题目的答案的最大值，也就是答案不会超过4位数
- EXAM_ITEMS = 5 每次至少做5道题结束
- EXAM_TIME = 120 每次至少做满120秒，即2分钟
- EXAM_TYPES = ...  题型配置，详见下面说明

### 题型配置

下面是一些题目模板。模板中的数代表上限，运算符可以为加减乘除(+-*/)。

题目模板中可以有括号和空格，这些都会原样保留。

- "100 * 100": 两位数（以内）乘法，所以也会出现1位数 ，下同
- "100 +- 100": 两位数加减法
- "10000 / 100": 4位数除以2位数
- "1000 +- 1000": 3位数加减法
- "1000 +- 1000 +- 1000": 3个3位数的加减法
- "1000 +-*/ (200 +-* 100)": 3位数 加减乘除 (200以内的数 加减乘 100以内的数 的结果）

## 答题

答案没有分数，小数，负数。

除法答案中余数的表示：

商...余数  （3个小数点，中间没有空格）

不小心直接按了回车不要紧，会忽略。

## 得分

因为错题会要求当场重做，直到做对为止，所以会累计做错的次数。
最后的得分是：

做对的次数 / 做对和做错的次数之和 * 100

而每道题的平均时间则以做对的题数来平均。

## History

- 0.3 (9/5/2021): Support time control, fine tune, add README
- 0.2 (9/5/2021): Support text report
- 0.1 (9/4/2021): Initial version, supports auto question and auto check

