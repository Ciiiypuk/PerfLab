import sys

def min_moves_to_one_elements(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    moves = sum(abs(num - median) for num in nums)
    return moves
nums = []
if len(sys.argv) ==1 or len(sys.argv)>2:
    print('Ошибка!!! \nОжидаю 1 параметр!')
with open(sys.argv[1], "r") as file:
    for line in file:
        nums.append(int(line))
print(min_moves_to_one_elements(nums))