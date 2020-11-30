def bai2(x ,y):
    if x > y:
        return "x < y"

    count = 0

    if x == y:
        return count

    while(True):
        print(x, y)
    
        if x * 2 == y or x - 1 == y:
            count += 1
            break
        else:
            if x * 2 > (x - 1) * 2 and x * 2 > y and (x - 1) * 2 > y:
                x -= 1
            elif x < y:
                x *= 2
            else:
                x -= 1
            count += 1

    return count

print(bai2(2, 5))
