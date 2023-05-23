def find_longest_increasing_subsequence(arr, num):
    if num == 0:
        return [], 0

    dp = [1] * num
    for i in range(1,num):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    max_length = max(dp)  
    idx = dp.index(max_length)
    result = []
    for i in range(idx, -1, -1):
        if dp[i] == max_length and (not result or arr[i] < result[-1]):
            result.append(arr[i])
            max_length -= 1
            if max_length == 0:
                break

    result.reverse()
    return result, len(result)

num = int(input())

if num == 0:
    exit()
else:
    arr = list(map(int, input().split()))
    result, length = find_longest_increasing_subsequence(arr, num)
    print(length)
    print(*result)
