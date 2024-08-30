### 이놈은 다른 사람들의 블로그 해답을 봐도 이해가 안되네 왜 그렇게 푸는 걸까..?
### 이 문제를 푸는 로직은 매번 값이 들어올때 마다 계산을 하는 것보다
### 모든 값들을 데이터 형태로 저장을 한 후에 이를 찾는 것이 더 빠르다는 생각인 듯 하다...

# -------------------------------------------------------------------
import sys

MAX = 1000000

savechartTemp = [1]*(MAX+1)
savechartReal = [0]*(MAX+1)
savechartReal[1] = 1


for i in range(2,(MAX+1)):
    for j in range(1,(MAX//i)+1):
        savechartTemp[j*i] = savechartTemp[j*i] + i

    savechartReal[i] = savechartReal[i-1] + savechartTemp[i]

x = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(x)]

for i in data:
    n = int(i)
    print(savechartReal[n])

# -------------------------------------------------------------------

import time
import sys

start_time = time.time()
loop = int(sys.stdin.readline().rstrip())
for i in range(loop):
    n = int(sys.stdin.readline().rstrip())
    sum_ = 0
    for i in range(1, n+1):
        # i의 배수의 개수 = i를 약수로 갖는 수
        sum_ += (n//i)*i
    print(sum_)

end_time = time.time()

print(f'코드 실행 시간: {end_time - start_time:.4f}')
