def binary_search(list_to_search, target, min_limit = None, max_limit = None): # Solo funciona en listas ordenadas.
    list_ol = sorted(list_to_search)

    if min_limit == None:
        min_limit = 0
    if max_limit == None: 
        max_limit = len(list_ol) - 1

    mid_point = (min_limit + max_limit) // 2

    if max_limit < min_limit:
        return -1

    if list_ol[mid_point] == target:
        return mid_point
    elif list_ol[mid_point] < target:
        return binary_search(list_to_search, target, mid_point+1, max_limit)
    else:
        return binary_search(list_to_search, target, min_limit, mid_point-1)

    
print(binary_search([4,5,3,2,1,44,52,87,97,5434,543,21212,4412,553,10], 553))
