while True:
    try:
        num_num = int(input())
        in_num = list(map(int, input().split()))  # 받은 값 리스트로 저장
        print(min(in_num)*max(in_num))
    except:
        break

# 결과는 맞았는데 실행시간이 36ms로 상대적으로 길게 느껴졌다.
# 이를 단축할 수 있으면 좋을듯
