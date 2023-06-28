# Baekjoon 2018
# n을 입력받아, n과 같은 연속된 자연수 합(sum)을 나타내는 가짓수를 출력한다.
# 연속된 수는 시작 인덱스(start_index)와 종료 인덱스(index)를 지정하여 표현한다.
# 합이 n에 모자라면, 끝에 자연수(end_index)를 하나 더 더하고, 끝에 더할 자연수(end_index)를 1 늘린다.
# 합이 n을 넘으면, 앞의 자연수(start_index)를 하나 제외하고, 앞에서 제외할 자연수(start_index)를 1 늘린다.
# 합이 n이 되면 카운트하고(가짓수 집계), 끝에 더할 자연수(end_index)를 1 늘린다.
# 끝에 더할 자연수(end_index)가 n과 같아지기 직전까지 처리를 반복한다.
# 요약하면, n과 연속된 자연수의 합이 같아질 때까지 연속된 자연수 배열을 앞뒤로 범위 조절하여, 같아지는 경우를 발견하면, 해당 가짓수를 카운트하는 것이다.

n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n:
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index

print(count)