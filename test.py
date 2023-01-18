def maxProfit(prices):

    # look through all trades one time. 
    # make a list of these trades.
    # check for best combination of these deltas
    # return best possible comnbination
    i,j,k,l,ans = len(prices)-1,0,0,0,0
    total_gain1 = [{
            "val":0,
            "right_num":0,
            "left_num":0,
            "right_idx": 0,
            "left_idx": 0
        }]
    total_gain2 = [{
            "val":0,
            "right_num":0,
            "left_num":0,
            "right_idx": 0,
            "left_idx": 0
        }]
    
    while i > 0:
        j = i-1
        right_num = prices[i]
        while j >= 0:  
            left_num = prices[j]
            current_gain = {
            "val": right_num - left_num,
            "right_num": right_num,
            "left_num": left_num,
            "right_idx": i,
            "left_idx": j
            }
            
            if current_gain["val"] > total_gain1[-1]["val"]:
                total_gain1.append(current_gain)
            j -= 1
        i -= 1
        
    
    k = total_gain1[-1]["left_idx"]  

    while k > 0:
        l = k-1
        right_num = prices[k]
        while l >= 0:  
            left_num = prices[l]
            current_gain = {
            "val": right_num - left_num,
            "right_num": right_num,
            "left_num": left_num,
            "right_idx": k,
            "left_idx": l
            }
            
            if current_gain["val"] > total_gain2[-1]["val"]:
                total_gain2.append(current_gain)
            l -= 1
        k -= 1
    
    total_gain1.pop(0)
    total_gain2.pop(0)
    
    for i in total_gain1:
        print(f'delta {i["val"]} \nright_idx{i["right_idx"]} \nleft_idx {i["left_idx"]}\n')
        
    for i in total_gain2:
        print(f'delta {i["val"]} \nright_idx{i["right_idx"]} \nleft_idx {i["left_idx"]}\n')
    
    try:
        val1 = int(total_gain1[-1]["val"])
        ans += val1
    except:
        val1 = 0
    
    try:
        val2 =int(total_gain2[-1]["val"])
        ans += val2
    except:
        val2 = 0
        
    print(ans)
    return(ans)

data = [3,2,6,5,0,3]

maxProfit(data)