
import sys
import time


def main():
    n, m = map(int, input().split())
    count = 0
    for i in range(n, m+1):
        if i == 1:
            continue
        i_divisor = 0
        for j in range(2, i+1):
            if i % j == 0:
                i_divisor += 1
        if i_divisor == 1:
            print(i)


start_time = time.time()

main()

end_time = time.time()

print(f'코드 실행 시간: {end_time - start_time:.4f}')

start_time = time.time()

# ------------------------------------------------------

MN_list = sys.stdin.readline().rstrip()
# MN_list 0보다 크고 1보다 작은 소수를 모두 출력해야함

# ------------------------------------------------------
end_time = time.time()

print(f'코드 실행 시간: {end_time - start_time:.4f}')
