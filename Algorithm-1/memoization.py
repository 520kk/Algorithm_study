# 재귀함수를 이용한 피보나치수열 알고리즘 
def fibo(n):
    if n <2:
        return n
    else:
        return fibo(n -1 ) + fibo(n - 2)


# 메모이제이션 기법을 사용한 피보나치수열 알고리즘
def fib(n):
    fibList=[1, 1]
    if n==1 or n==2:
        return 1
    for i in range(2,n):
        fibList.append( fibList[i-1] + fibList[i-2] )
    return fibList



# 메모이제이션이란?
# 컴퓨터 프로그램이 동일한 계산을 반복적으로 해야 할 때,
# 이전에 계산한 값을 메모리에 저장하여
# 중복적인 계산을 제거하여 전체적인 실행 속도를 빠르게 해주는것
# 동적계획법(DP; Dynamic Programming)의 핵심이 되는 기술
