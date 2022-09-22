def SelectionSort(n):
    if n == len(arr)-1:
        print(arr)
        return
    m = n
    for i in range(n, len(arr)):
        if arr[m] > arr[i]:
            m = i
    arr[m], arr[n] = arr[n], arr[m]
    SelectionSort(n+1)


arr = [45, 22, 1435, 234, 35, 61, 39, 6745, 143, 5679, 2345]
SelectionSort(0)