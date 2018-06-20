def get_even_list(li):
    n_list = []
    for n in li:
        if n % 2 == 0:
            n_list.append(n)
    return n_list

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")