# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for cur_index in range(smallest_index, len(arr)):
             if arr[smallest_index] > arr[cur_index]:
                arr[smallest_index],arr[cur_index] = arr[cur_index],arr[smallest_index]
        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    length = len(arr)
    for i in range(length):
        for a in range(0, length -i -1):
            if arr[a] > arr[a+1]:
                arr[a],arr[a+1] = arr[a+1],arr[a]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr