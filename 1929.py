
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
