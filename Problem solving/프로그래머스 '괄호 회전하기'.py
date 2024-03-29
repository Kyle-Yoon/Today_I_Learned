'''
프로그래머스 '괄호 회전하기'


# 문제 설명
다음 규칙을 지키는 문자열을 올바른 괄호 문자열이라고 정의합니다.

(), [], {} 는 모두 올바른 괄호 문자열입니다.
만약 A가 올바른 괄호 문자열이라면, (A), [A], {A} 도 올바른 괄호 문자열입니다. 
예를 들어, [] 가 올바른 괄호 문자열이므로, ([]) 도 올바른 괄호 문자열입니다.
만약 A, B가 올바른 괄호 문자열이라면, AB 도 올바른 괄호 문자열입니다. 
예를 들어, {} 와 ([]) 가 올바른 괄호 문자열이므로, {}([]) 도 올바른 괄호 문자열입니다.

대괄호, 중괄호, 그리고 소괄호로 이루어진 문자열 s가 매개변수로 주어집니다. 
이 s를 왼쪽으로 x (0 ≤ x < (s의 길이)) 칸만큼 회전시켰을 때,
s가 올바른 괄호 문자열이 되게 하는 x의 개수를 return 하도록 solution 함수를 완성해주세요.


# 제한 사항
s의 길이는 1 이상 1,000 이하입니다.


# 입출력 예
    s           result
"[](){}"	      3
"}]()[{"	      2
"[)(]"	          0
"}}}"	          0
'''

# 시간복잡도 O(n ** 2)
def solution(s):
    answer = 0
    
    # 닫는 괄호가 나왔을 때 열린 괄호랑 짝을 이루는지 검사하는 딕셔너리 선언
    close_dict = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    if len(s) == 1:    # s의 길이가 1이면 올바른 괄호 문자열이 아니므로 0 리턴
        return 0
    
    for x in range(len(s)):    # s를 회전하기 위한 인덱스. s의 길이만큼 회전(0칸 회전도 포함)
        tmp_s = s[x:] + s[:x]    # 회전한 s
        stack = []    # 괄호검사를 위한 스택선언
        
        for idx, element in enumerate(tmp_s):    # 회전한 s의 각 요소를 검사
            if element in '({[':    # 열린 괄호면 stack에 추가
                stack.append(element)
            else:    # 닫힌 괄호를 만났을 때, 스택에 요소가 하나도 없거나 열린괄호랑 종류가 일치하지 않으면 해당 회전 문자열은 종료
                if not stack or stack.pop() != close[element]:
                    break
        if not stack and idx + 1 == len(s):    # 회전한 s의 요소를 전부 순회했을 때, 스택이 비어있으면 올바른 괄호 문자열 개수에 1 추가
            answer += 1
    
    return answer