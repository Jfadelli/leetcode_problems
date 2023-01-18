
def numberOfWeakCharacters(properties):
    print('running')
    # double for loop through array, comparing iA > jA & iD > jD
    # if item is greater than both attributes of other idx's than 
    
    #Search for highest Attack and Defense Values
    
    p = properties
    max_attack = 0
    max_attack_idx = 0
    max_defense = 0
    max_defense_idx = 0
    i = 0
    while i < len(p):
        if p[i][0] > max_attack:
            max_attack_idx = i
            max_attack = p[i][0]
        if p[i][1] > max_defense:
            max_defense_idx = i
            max_defense = p[i][1]
        i += 1
    print(f'Max attack idx = {max_attack_idx} \nMax attack val = {max_attack}')
    print(f'Max defense idx = {max_defense_idx} \nMax defense val = {max_defense}')
    
    weak_char_count = 0
    i = 0

    while i < len(p):
        curr_attack, curr_defense = p[i][0], p[i][1]

        # if curr_attack < max_attack and curr_defense < max_defense:
        if curr_attack < max_attack:
            if curr_defense < p[max_defense_idx][1]:
                weak_char_count += 1
        if curr_defense < max_defense:
            if curr_attack < p[max_attack_idx][1]:
                weak_char_count += 1
        i += 1
    return weak_char_count

        
        
# data = [[1,5],[10,4],[4,3]]
data = [[5,5],[6,3],[3,6]]
            
print(numberOfWeakCharacters(data))