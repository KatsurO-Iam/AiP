from typing import final

f = open('file.txt', 'w')
f.write('hello\n')
f.write('world\n')

#\<один символ> - экранирование
#\n - endl, перевод строки
#\t - TAB
#\' - '
#\" - "
#\\ - \


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    res = {}
    for i in range(len(nums)):
        x = nums[i]
        need = target - x

        if need in res:
            return [res[need], i]
        res[x] = i

print(twoSum([3,2,4], 6))
