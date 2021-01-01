def string_to_cents(string: str) -> int:
    nums = string.split('.')
    if len(nums) > 1:
        return int(nums[0]) * 100 + int(nums[1])
    else:
        return int(nums[0]) * 100


def cents_to_string(cents: int) -> str:
    d = cents // 100
    c = cents % 100
    return str(d) + '.' + str(c)
