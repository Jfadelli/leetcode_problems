
def lastStoneWeight(stones):
    if len(stones) ==1:
        return stones[0]
    
    
    while len(stones) > 1:
        max1 = max(stones)
        idx_max1 = stones.index(max1)
        stones.pop(idx_max1)

        max2=max(stones)
        idx_max2 = stones.index(max2)
        stones.pop(idx_max2)
        
        if max1 == max2:
            continue
        else:
            if max1>max2:
                new_val = max1-max2
                stones.append(new_val)
    return stones[0]

data = [1,3,5,7,10,23]

print(lastStoneWeight(data))
