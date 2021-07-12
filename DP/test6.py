def test(nums):
    ans = 1
    memo = [1]*len(nums)
    for curr_idx in range(0, len(nums)):
        for prev_idx in range(0, curr_idx):
            if(nums[prev_idx] < nums[curr_idx]):
                memo[curr_idx] = max(memo[curr_idx], memo[prev_idx]+1)
                ans = max(ans, memo[curr_idx])
    print(memo)
    print(ans)
    return ans


arr = [2, 5, 6, 2, 4]

test(arr)
