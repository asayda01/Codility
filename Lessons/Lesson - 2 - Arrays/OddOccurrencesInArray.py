def solution(A):
  
  set_1 = set()

  for value_1 in A:
      
      if value_1 not in set_1:
          set_1.add(value_1)

      else:
          set_1.remove(value_1)

  return list(set_1)[0]

"""

def solution(A):

    arr = []

    for i in A:
        
        if i in arr:
            arr.remove(i)
        else:
            arr.append(i)

    return arr[0]
     


print(solution([9, 3, 9, 3, 9, 7, 9]))

"""


"""

def solution(A):
    uniq_elem = 0
    for elm in A:
        uniq_elem = elm ^ uniq_elem
    return uniq_elem

"""