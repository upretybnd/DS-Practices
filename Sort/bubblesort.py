def bubblesort(a):
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


my_a = [64, 87, 45, 12, 758]
bubblesort(my_a)
print("sorted array", my_a)
