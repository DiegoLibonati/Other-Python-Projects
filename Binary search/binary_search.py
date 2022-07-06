def binary_search(list_to_search, target, min_limit = None, max_limit = None): # Solo funciona en listas ordenadas.
    if min_limit == None:
        min_limit = 0
    if max_limit == None: 
        max_limit = len(list_to_search) - 1

    mid_point = (min_limit + max_limit) // 2

    if max_limit < min_limit:
        return -1

    if list_to_search[mid_point] == target:
        return mid_point
    elif list_to_search[mid_point] < target:
        return binary_search(list_to_search, target, mid_point+1, max_limit)
    else:
        return binary_search(list_to_search, target, min_limit, mid_point-1)

    
print(binary_search([1,2,3,4,5,6,7,8,9,10], 10))
