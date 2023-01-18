def maxProfit(prices):

    # look through all trades one time. 
    # make a list of these trades.
    # check for best combination of these deltas
    # return best possible comnbination
    
    total_gains = [{
            "val":0,
            "right_num":0,
            "left_num":0,
            "right_idx": 0,
            "left_idx": 0
        }]
    i = 0
    while i < len(prices):
        j = i+1
        left_num = prices[i]
        while j < len(prices):

            right_num = prices[j]
            current_gain = {
                "val": right_num - left_num,
                "right_num": right_num,
                "left_num": left_num,
                "right_idx": i,
                "left_idx": j
            }
            total_gains.append(current_gain)
            j += 1
        i += 1
    
    total_gains.pop(0)
    print(total_gains["vals"])

    # best_trade = []
    # best_trade.append(total_gains[0])
    # print(best_trade)
    # for i in total_gains:
    #     print(int(i["val"]))
    #     print(f'HERE -> {int(best_trade[0]["val"])}')
    #     if int(i["val"]) > int(best_trade[0]["val"]):
    #         print('ye')
            
    #         best_trade.append(i)


    # for i in total_gains:
    #     curr_best = 0
    #     num1 = int(i["val"])
    #     idx1= i["left_idx"]
    #     for j in total_gains:
    #         num2 = int(j["val"])
    #         idx2 = i["right_idx"]
    #         if num2 > num1:
    #             curr_best = num2
    # print(curr_best)



    # find the two greatest deltas that do not have interfering index


    
    # for i in total_gains:
    #     print(f'delta {i["val"]} \nright_idx{i["right_idx"]} \nleft_idx {i["left_idx"]}\n')
    


test_case = [3,2,6,5,0,3]

maxProfit(test_case)