qwerty = [4,5,6]

def average(nums):
    counter = 0
    for i in nums:
        counter += i
    average = counter/len(nums)
    return average


print(average(qwerty))
