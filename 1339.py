N = int(input())
ans = 0
my_dict = {}

for _ in range(N):
    word = input()
    for i, letter in enumerate(word):
        if letter in my_dict:
            my_dict[letter] += 10**(len(word) - i - 1)
        else: 
            my_dict[letter] = 10**(len(word) - i - 1)

dictlist = []            

for value in my_dict.values():
    dictlist.append(value)

dictlist.sort(reverse=True)

nums = [x for x in range(9, -1, -1)]

for i in dictlist:
    ans += i * nums[0]
    nums.pop(0)

print(ans)
