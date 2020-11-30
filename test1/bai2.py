def bai2(x ,y):
    count = 0
    while y > x:
        if y % 2 == 0:
            y /= 2
        else:
            y += 1
        print(x, y)
        count += 1
    while y < x:
        y += 1
        print(x, y)
        count += 1
    return count

print(bai2(2, 5))
