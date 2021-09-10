from typing import Any, Sequence

def max_of(a: Sequence) -> Any: # 매개변수 a의 자료형은 sequence이다. 반환하는 것은 임의의 자료형이 Any이다.
    maximum = a[0]              # sequence형에는 리스트(list)형, 바이트 배열(bytearry)형, 문자열(str)형, 튜플형, 바이트열(bytes)형이 있다.
    for i in range(1, len(a)): # 호출하는 쪽이 넘겨주는 실제 인수의 자료형은 뮤터블인 리스트, 이뮤터블인 튜플, 문자열등 시퀀스 자료형이라면 무엇이든 상관없다.
        if a[i] > maximum:     # 인수의 원소를비교 연산자 >로 비교할 수 있다면 다른 형(int, float)이 섞여 있어도 된다. 
            maximum = a[i]
        return maximum

if __name__ == '__main__': # __name__ :  모듈 이름을 나타내는 변수name__ :  모듈 이름을 나타내는 변수
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요.:'))
    x = [None] * num # 리스트 원소값 None를 num개 만큼 생성.
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요.:'))
        
    print(f'최댓값은 {max_of(x)}입니다.')
