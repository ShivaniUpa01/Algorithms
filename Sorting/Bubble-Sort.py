def bubble_sort(input_list):
    n = len(input_list)

    for pass_ele in range(n-1):
        for curr in range(n - 1 - pass_ele):
            if input_list[curr] > input_list[curr + 1]:
                input_list[curr], input_list[curr + 1] = input_list[curr + 1], input_list[curr]
        print(input_list)
    return input_list


if __name__ == "__main__":
    given_list = [5, 9, 3, 2, 1]
    print(bubble_sort(given_list))