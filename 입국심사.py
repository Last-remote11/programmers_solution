def solution(n, times):
    first = 1
    last = max(times)*n
    ansList = []

    while first <= last:
        
        mid = (first + last) // 2
        count = sum(map(lambda x : mid // x, times)) # count: 주어진 mid(시간) 내에 검사할 수 있는 사람 수

        if count < n: # 시간이 작음
            first = mid + 1
        elif count > n: # 시간이 큼 = mid를 줄여야
            last = mid - 1
        else:
            ansList.append(mid)
            last = mid - 1
    if len(ansList) == 0:
        return first
    else:
        return min(ansList)
