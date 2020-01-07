import random

def is_sorted(data) -> bool:
    """Determine whether the data is sorted."""
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            return False
    return True

def bogosort(data) -> list:
    """Shuffle data until sorted."""
    próby = 0
    while not is_sorted(data):
        random.shuffle(data)
        próby += 1
        print(próby, end = '\r')
    return data
nums = list(range(9))
random.shuffle(nums)
print('started\n' + str(nums))
nums = bogosort(nums)
print('\nsorted\n' + str(nums))
