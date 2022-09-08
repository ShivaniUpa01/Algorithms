import sys

def selection_sort(arr_list):
    n = len(arr_list)
    for curr in range(n-1):
        min_value = sys.maxsize
        min_index = -1
        for i in range(curr, n):
            if arr_list[i] < min_value:
                min_value = arr_list[i]
                min_index = i
            arr_list[curr], arr_list[min_index] = arr_list[min_index], arr_list[curr]
        print (arr_list)


if __name__ == "__main__":

    a_List = []
    insert = int(input("Define the length of list : "))
    count = 0
    print("Enter input to tht Array List : ")
    while count < insert:
        ele = int(input())
        a_List.append(ele)
        count += 1
    selection_sort(a_List)

