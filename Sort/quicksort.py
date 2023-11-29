def quicksort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a[0]
        less_than = [element for element in a[1:] if element <= pivot]
        greater_than = [element for element in a[1:] if element > pivot]
        return quicksort(less_than) + [pivot] + quicksort(greater_than)


my_a = [3, 9, 8, 10, 14, 12, 1]
sorted_array = quicksort(my_a)
print(sorted_array)
