def solve(numBottles: int, numExchange: int) -> int:
    ret = 0
    empty = 0
    toDrink = numBottles
    while toDrink > 0:
        ret += toDrink
        empty += toDrink
            
        toDrink = int(empty / numExchange)
        empty %= numExchange
    return ret

print(solve(9, 3))
print(solve(15, 4))

