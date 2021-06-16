N = int(input())

def make_prime_list(num):

    prime_list = []
    all_list = [ x for x in range(0, num+1) ]
    all_list[0], all_list[1] = False, False

    for i in range(len(all_list)):
        current_num = all_list[i]
        if current_num:
            prime_list.append(current_num)
            for j in range(current_num**2, num+1, current_num):
                all_list[j] = False

    return prime_list

def solution(num):
    if num == 1:
        return 0
    prime_list = make_prime_list(num)
    right, left = 0, 0
    temp_sum = 0
    ans = 0

    while True:
        if temp_sum > N:
            temp_sum -= prime_list[left]
            left += 1

        elif right == len(prime_list):
            if prime_list[-1] == num:
                ans += 1
            break

        else:
            if temp_sum == num:
                ans += 1
            temp_sum += prime_list[right]
            right += 1

    return ans

print(solution(N))
