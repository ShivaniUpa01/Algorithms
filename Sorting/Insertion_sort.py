def insertion_sort(in_list):
    n = len(in_list)
    for curr in range(1, n):
        for i in range(0, curr):
            if in_list[i] > in_list[curr]:
                in_list[i], in_list[curr] = in_list[curr], in_list[i]
        print(in_list)
    return in_list


if __name__ == "__main__":
    given_list = [5, 2, 9, 7, 1, 3]
    print(insertion_sort(given_list))
