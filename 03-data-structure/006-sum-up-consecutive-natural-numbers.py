'''
Baekjoon 2018
Count the number of the cases if the sum of consecutive natural numbers is equal to n when adjusted forward and backward.

문제: 
N을 입력받아, N과 같은 연속된 자연수 합의 가짓수를 출력한다.
예로 3을 입력했으면 가짓수는 1+2, 3으로 2가지이다.

풀이:
1+1+1+1... 값을 1씩 더하거나 빼며, N과 같아지는 경우를 발견하면, 해당 가짓수를 카운트하는 것이다.
N이 자기 자신으로 합이 되는 경우는 처음부터 가짓수 1로 카운트되어 있다.
'''

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