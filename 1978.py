import time


def main():
    loop = int(input())
    num_list = list(map(int, input().split()))
    count = 0
    for i in num_list:
        if i == 1:
            continue
        i_divisor = 0
        for j in range(2, i+1):
            if i % j == 0:
                i_divisor += 1
        if i_divisor == 1:
            count += 1
    print(count)


start_time = time.time()

main()

end_time = time.time()

print(f'코드 실행 시간: {end_time - start_time:.4f}')
