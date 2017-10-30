
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = map(int, line.split())
    k = int(sys.stdin.readline().strip())

    s = list(values)
    lens = len(s)
    max_len = 0

    for ln in range(1, lens + 1):
        for i in range(0, lens - ln + 1):
            j = i + ln - 1
            if i == j and s[i] % k == 0:
                if max_len !=0:
                    max_len = 1
            tem_sum = sum(s[i:j + 1])
            if tem_sum % k == 0:
                max_len = ln
    print(max_len)