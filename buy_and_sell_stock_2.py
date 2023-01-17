
def maxProfit(prices):
    print(prices)
    def solve_delta(pr):
        p1, p2, results = 0,0, {}
        # print('printing list of solved trades: higher delta is better')
        while p1 < len(pr):
            
            p2 = p1
            while p2 < len(pr):
                delta = pr[p2]-pr[p1]
                if delta > 0:
                    # print(f'step{p2}-{p1}  delta: {delta}')
                    start = p1
                    end = p2 
                    results[f'{start}{end}']={"start": start, "end": end, "delta" :delta, "id":f'{start}{end}'}

                p2+= 1
            p1 += 1
        return results


    solve_delta_results = solve_delta(prices)

    def comparison_engine(solve_delta_results):
        p1, p2, sdr, real_pairs = 0, 0, solve_delta_results, []
        # compare deltas of pairs and check if the keys overlap
        pair_stack = []
        ids = []
        for i in sdr:
            ids.append(i)
        print(ids)

        while p1 < len(ids):
            p2 = p1
            print(ids[p1])
            curr_id = ids[p1]
            curr_start = int(sdr[curr_id]['start'])
            curr_end = int(sdr[curr_id]['end'])
            curr_delta = int(sdr[curr_id]['delta'])
            print(curr_delta,curr_end, curr_start,curr_id)
            while p2 < len(ids):
                next_id = ids[p2]
                next_start = int(sdr[next_id]['start'])
                next_end = int(sdr[next_id]['end'])
                next_delta = int(sdr[next_id]['delta'])
                print(next_delta,next_end, next_start,next_id)
                if curr_delta > next_delta:
                    print('there')
                    p2 += 1
                elif next_delta < curr_delta:
                    print('here')
                    if curr_start <= next_start & next_start >= curr_end & next_end <= curr_start:
                        print('m'+curr_id)
                        real_pairs.append(curr_id)
                        p2 += 1

                p2 += 1
            p1 += 1

            # print(real_pairs)
            # create a stack of valid pairs
            # look at the delta and if it' something put it into the stack

    comparison_engine(solve_delta_results)

prices = [7,1,5,3,6,4]
maxProfit(prices)
