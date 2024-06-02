array = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
]

searchno = 1

start = 0
last = len(array)
mid =(start + last)//2

while array[mid] ~= searchno:
    if array[] < searchno:
        start = mid + 1
    else:
        start = mid