def majority_elements(nums):
    if not nums:
        return []

    # Initialize candidates and their counters
    candidate1, candidate2 = None, None
    count1, count2 = 0, 0

    # Voting process
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # Count occurrences of candidates to determine if they meet the criteria
    count1, count2 = 0, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    result = []
    n = len(nums)

    if count1 > n // 3:
        result.append(candidate1)
    if count2 > n // 3:
        result.append(candidate2)

    return result

# Example usage:
nums = [3, 3, 3, 2, 2, 1, 1, 1]
result = majority_elements(nums)
print("Elements appearing more than ⌊ n/3 ⌋ times:", result)

