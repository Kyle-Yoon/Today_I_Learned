'''
프로그래머스 '야근지수'
https://school.programmers.co.kr/learn/courses/30/lessons/12927

# 문제 설명
회사원 Demi는 가끔은 야근을 하는데요, 야근을 하면 야근 피로도가 쌓입니다. 
야근 피로도는 야근을 시작한 시점에서 남은 일의 작업량을 제곱하여 더한 값입니다. 
Demi는 N시간 동안 야근 피로도를 최소화하도록 일할 겁니다.Demi가 1시간 동안 작업량 1만큼을 처리할 수 있다고 할 때, 
퇴근까지 남은 N 시간과 각 일에 대한 작업량 works에 대해 야근 피로도를 최소화한 값을 리턴하는 함수 solution을 완성해주세요.


# 제한 사항
works는 길이 1 이상, 20,000 이하인 배열입니다.
works의 원소는 50000 이하인 자연수입니다.
n은 1,000,000 이하인 자연수입니다.


# 입출력 예
works	        n	    result
[4, 3, 3]	    4	      12
[2, 1, 2]	    1	      6
[1,1]	        3	      0
'''

시간복잡도 O(nlogn)
import heapq

def solution(n, works):
    works = list(map(lambda x: -x, works))    # 최대힙을 구현하기 위한 트릭
    heapq.heapify(works)    # works 리스트를 heapify
    for _ in range(n):    # n번 반복
        max_work = heapq.heappop(works)    # 가장 큰 작업을 꺼내서 작업량을 1만큼 빼고 다시 heappush
        if max_work < 0:
            max_work += 1
        heapq.heappush(works, max_work)
    return sum(map(lambda x: x**2, works))    # 우선순위큐 각 요소를 제곱해서 더한 값을 반환