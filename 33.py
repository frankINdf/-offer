#把数组排成最小的数
def cmp(a, b):
    return int(str(a)+str(b)) - int(str(b)+str(a))


def print_mini(nums):
    if not nums:
        return
    print int(''.join([str(num) for num in sorted(nums, cmp=cmp)]))


if __name__ == '__main__':
    test = []
    print_mini(test)
