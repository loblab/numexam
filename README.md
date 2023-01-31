# Number exam for kids （小学生算术练习题）

Auto generate number question and auto check

小学算术题，自动出题，自动批改，自动打印。可配置题型、每次练习题的数目和练习时间。
做错的当场重做，直到做对为止。

- Features: supports customizing question types, exam time and item amount
- Platform: Windows/Linux/MacOS, Python 3.x
- Ver: 0.8
- Updated: 8/14/2022
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

- USER_NAME = "Kitty" 学生姓名。最好用英文或拼音（用中文会影响对齐）
- MAX_ANWSER = 9999 出的题目的答案的最大值，也就是答案不会超过4位数
- EXAM_ITEMS = 5 每次至少做5道题结束
- EXAM_TIME = 120 每次至少做满120秒，即2分钟
- STRICT_LEN = True 严格的位数，两位数是10~99 （不包括一位数）
- EXAM_TYPES = ...  题型配置，详见下面说明

### 题型配置

下面是一些题目模板。模板中的数代表上限，运算符可以为加减乘除(+-*/)。

题目模板中可以有括号和空格，这些都会原样保留。

- "99 * 99": 两位数乘法
- "99 +- 99": 两位数加减法
- "9999 / 99": 4位数除以2位数
- "999 +- 999": 3位数加减法
- "999 +- 999 +- 999": 3个3位数的加减法
- "999 +-*/ (199 +-* 99)": 3位数 加减乘除 (200以内的数 加减乘 100以内的数 的结果）

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

- 0.9 (1/31/2023): Support strict num range, i.e. 999 stands for 100~999, not 1~999
- 0.8 (8/14/2022): Use icons/symbols for correct/wrong/question
- 0.7 (9/11/2021): Question type and statistics by type; code refactor
- 0.6 (9/7/2021): Compact footer
- 0.5 (9/5/2021): Support printer (tested on Windows)
- 0.4 (9/5/2021): Change template, use 99 for 2-digit number (instead of 100)
- 0.3 (9/5/2021): Support time control, fine tune, add README
- 0.2 (9/5/2021): Support text report
- 0.1 (9/4/2021): Initial version, supports auto question and auto check

