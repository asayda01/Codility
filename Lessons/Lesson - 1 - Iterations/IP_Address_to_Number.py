def ip_to_num(ip):
    
    str1 = ip.split(".")
    
    first =  bin(int(str1[0]))[2:].zfill(8)
    second = bin(int(str1[1]))[2:].zfill(8)
    third =  bin(int(str1[2]))[2:].zfill(8)
    forth =  bin(int(str1[3]))[2:].zfill(8)
    
    lst_str = first + second + third + forth
    len_A = len( str ( int(lst_str, 2) ) )
    return int(lst_str, 2)


def num_to_ip(num):
    len_A = len( str ( int(str(num), 32) ) )
    return int(str(num), 32)


ip = '192.168.1.1'
print ( num_to_ip( ip_to_num(ip) )  )