# 2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 각 자릿수가 모두 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.
while True:
    try:
        in_num = int(input())
    except:
        break

    multiple = 1
    count = 1
    while True:
        if multiple % in_num != 0:
            multiple += 10 ** count
            count += 1
        else:
            break

    print(count)


# 이전 제출 코드에서 문제였던 점은 내가 len(str(multiple))을 통해 자릿수를 구하려고한 것이 문제임을 알 수 있었다.
# 이를 통해 구할때 지속해서 시간 오류가 발생했다.


# while True:
#     try:
#         finding = True
#         in_num = int(input())
#         multiple = 1
#         while finding:
#             if multiple % in_num != 0:
#                 multiple += 10**len(str(multiple))
#             else:
#                 finding = False
#                 print(len(str(multiple)))
#     except:
#         break
