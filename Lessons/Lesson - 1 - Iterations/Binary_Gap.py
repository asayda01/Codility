def solution(N):
    
    bin1 = str(   bin(N)   )  [2:]       # to remove “0b” part
    bin_group = False
    high_zero = 0
    zero_counter = 0
    
    for i in bin1:
        
        if i == "1":
            
            if high_zero < zero_counter:
                high_zero = zero_counter
                
            bin_group = True
            zero_counter = 0
            
        elif bin_group:
            zero_counter += 1
            
    return high_zero
