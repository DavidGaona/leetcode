def countKAverageSubarrays(arr, n, k):
    result = 0
    cur_sum = 0

    memo = {}

    for i in range(n):

        cur_sum += arr[i] - k

        if cur_sum == 0:
            result += 1

        if cur_sum in memo:
            result += memo[cur_sum]
            memo[cur_sum] += 1
        else:
            memo[cur_sum] = 1

    # Return result
    return result


print(countKAverageSubarrays([1, 2, 3, 4, 5], 5, 4))
