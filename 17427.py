import time

start_time = time.time()

n = int(input())

sum_ = 0
for i in range(1, n+1):
    # i의 배수의 개수 = i를 약수로 갖는 수
    sum_ += (n//i)*i

print(sum_)

end_time = time.time()

print(f'코드 실행 시간: {end_time - start_time:.4f}')


# num = int(input())
# divisor = []
# for i in range(num, 0, -1):
#     for j in range(i, 0, -1):
#         if i % j == 0:
#             divisor.append(j)
# print(sum(divisor))


# 처음에 작성한 코드는 이중 for문을 사용하기에
# 시간 복잡도가 높은 코딩이여서 시간제한 조건을 만족하지 못한다.

# 정답은 N의 배수는 N을 항상 약수로 갖는다는 논리를 이용해서 N이하의 자연수 중에서 i를 약수로 갖는 개수는 N/i개이다
# g(N) = 1*N/1 + 2*N/2 + ... + N*N/N
