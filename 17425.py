import time

start_time = time.time()

# ------------------------------------------------------

reap = int(input())
for i in range(reap):
    n = int(input())

    sum_ = 0
    for i in range(1, n+1):
        # i의 배수의 개수 = i를 약수로 갖는 수
        sum_ += (n//i)*i

    print(sum_)

# ------------------------------------------------------
end_time = time.time()

print(f'코드 실행 시간: {end_time - start_time:.4f}')
