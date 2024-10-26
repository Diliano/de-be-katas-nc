def sum_consecutive_duplicates(nums):
    result = []

    if nums:
        previous = nums[0]
        duplicate_sum = nums[0]

        for num in nums[1:]:
            if num == previous:
                duplicate_sum += num
            else:
                result.append(duplicate_sum)
                previous = num
                duplicate_sum = num

        result.append(duplicate_sum)

    return result


def reduce_consecutives(nums):
    reduced = sum_consecutive_duplicates(nums)

    if reduced == nums:
        return reduced
    else:
        return reduce_consecutives(reduced)
