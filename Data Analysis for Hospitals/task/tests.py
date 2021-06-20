from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult

df_result = '''   hospital gender   age  height  weight  ...  ultrasound mri xray children months
0   general      m  33.0    1.64    66.0  ...           0   0    0      0.0    0.0
1   general      m  48.0    1.93   106.0  ...           t   0    0      0.0    0.0
2   general      f  23.0    1.54    63.0  ...           0   0    0      0.0    0.0
3   general      m  27.0    1.94   103.0  ...           t   0    0      0.0    0.0
4   general      f  22.0    1.76    74.0  ...           0   0    f      0.0    0.0
5   general      m  46.0    1.90    96.0  ...           0   0    0      0.0    0.0
6   general      f  68.0    1.80    85.0  ...           f   0    0      0.0    0.0
7   general      m  35.0    1.57    61.0  ...           0   0    0      0.0    0.0
8   general      f  50.0    1.86    86.0  ...           0   0    f      0.0    0.0
9   general      m  25.0    1.79    82.0  ...           0   0    0      0.0    0.0
10  general      m  27.0    1.85    86.0  ...           0   0    0      0.0    0.0
11  general      m  57.0    1.86    95.0  ...           f   0    0      0.0    0.0
12  general      m  29.0    1.88   100.0  ...           0   0    f      0.0    0.0
13  general      f  18.0    1.70    80.0  ...           0   0    0      0.0    0.0
14  general      f  47.0    1.80    83.0  ...           f   0    0      0.0    0.0
15  general      f  51.0    1.87   103.0  ...           0   0    0      0.0    0.0
16  general      f  56.0    1.56    57.0  ...           0   0    t      0.0    0.0
17  general      f  38.0    1.62    71.0  ...           0   0    0      0.0    0.0
18  general      f  32.0    1.72    77.0  ...           0   0    0      0.0    0.0
19  general      f  69.0    1.72    80.0  ...           0   0    f      0.0    0.0

[20 rows x 14 columns]'''


class EDATest(StageTest):
    def generate(self):
        return [TestCase()]

    def check(self, reply, attach):
        lines = reply.split('\n')
        lines_with_digit = [i for i in lines if len(i) > 0 and i[0].isdigit()]
        columns = lines[0].split(' ')
        if 'Unnamed: 0' in columns:
            return CheckResult.wrong(feedback='Holy-moly! you\'ve printed \'Unnamed: 0\' column')
        if len(lines_with_digit) != 20:
            return CheckResult.wrong(feedback='There should be 20 lines of data, found ' + str(len(lines_with_digit)))
        if df_result not in reply:
            return CheckResult.wrong(feedback="Seems like your answer is incorrect. Look at the example")
        return CheckResult.correct()


if __name__ == '__main__':
    EDATest('analysis').run_tests()
