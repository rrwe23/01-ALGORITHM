# https://www.acmicpc.net/problem/1100
import sys

sys.stdin = open("7_하얀칸.txt")

# * 문제 : 최대공약수, 최소공배수 구하기
# * 접근
#     * 두 수의 곱 / gcd => lcm
'''

# a, b = map(int, input().split())

# for i in range(min(a, b), 0, -1):
#     if a % i == 0 and b % i == 0:           #용택
#         gcd = i
#         break

# print(gcd)
# print(a*b // gcd)


# # 처음 시간 초과 경우
# # 최대공약수 (GCD)
# for i in range(min(a, b), 0, -1):
#     if a % i == 0 and b % i == 0:
#         GCD = i
#         break
# # 최소공배수 (LCM)
# for i in range(max(a, b), (a * b) + 1):       
#     if i % a == 0 and i % b == 0:
#         LCM = i
#         break

