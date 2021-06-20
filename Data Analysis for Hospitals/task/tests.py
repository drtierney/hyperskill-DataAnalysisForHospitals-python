from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult

df_result = '''   hospital gender   age  height  weight  ...  ultrasound  mri xray children months
0   general    man  33.0    1.64    66.0  ...         NaN  NaN  NaN      NaN    NaN
1   general    man  48.0    1.93   106.0  ...           t  NaN  NaN      NaN    NaN
2   general  woman  23.0    1.54    63.0  ...         NaN  NaN  NaN      NaN    NaN
3   general    man  27.0    1.94   103.0  ...           t  NaN  NaN      NaN    NaN
4   general  woman  22.0    1.76    74.0  ...         NaN  NaN    f      NaN    NaN
5   general    man  46.0    1.90    96.0  ...         NaN  NaN  NaN      NaN    NaN
6   general  woman  68.0    1.80    85.0  ...           f  NaN  NaN      NaN    NaN
7   general    man  35.0    1.57    61.0  ...         NaN  NaN  NaN      NaN    NaN
8   general  woman  50.0    1.86    86.0  ...         NaN  NaN    f      NaN    NaN
9   general    man  25.0    1.79    82.0  ...         NaN  NaN  NaN      NaN    NaN
10  general    man  27.0    1.85    86.0  ...         NaN  NaN  NaN      NaN    NaN
11  general    man  57.0    1.86    95.0  ...           f  NaN  NaN      NaN    NaN
12  general    man  29.0    1.88   100.0  ...         NaN  NaN    f      NaN    NaN
13  general  woman  18.0    1.70    80.0  ...         NaN  NaN  NaN      NaN    NaN
14  general  woman  47.0    1.80    83.0  ...           f  NaN  NaN      NaN    NaN
15  general  woman  51.0    1.87   103.0  ...         NaN  NaN  NaN      NaN    NaN
16  general  woman  56.0    1.56    57.0  ...         NaN  NaN    t      NaN    NaN
17  general  woman  38.0    1.62    71.0  ...         NaN  NaN  NaN      NaN    NaN
18  general  woman  32.0    1.72    77.0  ...         NaN  NaN  NaN      NaN    NaN
19  general  woman  69.0    1.72    80.0  ...         NaN  NaN    f      NaN    NaN

[20 rows x 14 columns]'''


class EDATest(StageTest):
    def generate(self):
        return [TestCase()]

    def check(self, reply, attach):
        lines = reply.split('\n')
        lines_with_digit = [i for i in lines if len(i) > 0 and i[0].isdigit()]
        columns = lines[0].split(' ')
        if 'Unnamed: 0' in columns:
            return CheckResult.wrong(
                'Holy-moly! you\'ve printed \'Unnamed: 0\' column')

        if len(lines_with_digit) != 20:
            return CheckResult.wrong(
                'There should be 20 lines of data, found ' + str(len(lines_with_digit)))

        if df_result not in reply:
            return CheckResult.wrong(
                "Seems like your answer is incorrect")

        return CheckResult.correct()


if __name__ == '__main__':
    EDATest('analysis').run_tests()
