# Stuff for k8mil
import random
print('Flexing on Kejmil')
grzes = 0
execu = 0
def GetUpperMedian(nums):
    x = int(len(nums) * 3/4)
    return nums[x]
while True:
    try:
        dane = random.sample(range(1, 1000), random.randint(100, 200))
    except:
        dane = random.sample(range(1, 10000), random.randint(2, 20))
    dane.sort()
    res = []
    for x in dane:
        if not len(res) == 0:
            tempRes = list()
            for i in res:
                num = i+x
                if not num in res:
                    tempRes.append(num)
            res.extend(tempRes)
        res.append(x)
        if len(res) > 80:
            res.sort()
            tempRes = res.copy()
            for num in tempRes:
                if num > GetUpperMedian(res):
                    res.remove(num)

    res.sort()
    x = res[0]
    n = 0
    while True:
        if x != res[n]:
            break
        else:
            n += 1
            x += 1
    if x == res[0] + 1:
        grzes += 1
    execu += 1
    print(str(grzes/execu) + '\t' + str(execu), end='\r')
