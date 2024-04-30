'''
프로그래머스 '숫자 짝꿍'
https://school.programmers.co.kr/learn/courses/30/lessons/131128


# 문제 설명
두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다(단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

예를 들어, X = 3403이고 Y = 13203이라면, X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 다른 예시로 X = 5525이고 Y = 1255이면 X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다(X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.


# 제한사항
3 ≤ X, Y의 길이(자릿수) ≤ 3,000,000입니다.
X, Y는 0으로 시작하지 않습니다.
X, Y의 짝꿍은 상당히 큰 정수일 수 있으므로, 문자열로 반환합니다.


# 입출력 예
X	            Y	            result
"100"	        "2345"	        "-1"
"100"	        "203045"	    "0"
"100"	        "123450"	    "10"
"12321"	        "42531"	        "321"
"5525"	        "1255"	        "552"
'''


# 시간복잡도 O(len(x)+len(y)+klogk)
def solution(X, Y):
    x_dict, y_dict = {}, {}
    
    # X와 Y의 빈도수 계산
    for num in X:
        if num in x_dict:
            x_dict[num] += 1
        else:
            x_dict[num] = 1
            
    for num in Y:
        if num in y_dict:
            y_dict[num] += 1
        else:
            y_dict[num] = 1
    
    # 교집합 원소의 최소 빈도 계산 및 결과 리스트 생성
    result = []
    for num in x_dict:
        if num in y_dict:
            min_count = min(x_dict[num], y_dict[num])
            result += [num] * min_count
    
    # 결과 정렬 (문자열 기준 내림차순)
    result.sort(reverse=True)
    
    # 최종 결과 생성
    if result:
        answer = ''.join(result)
        if answer[0] == '0':  # 첫 번째 문자가 "0"인 경우
            return "0"
        return answer
    return "-1"