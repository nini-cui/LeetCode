def customers_with_same_account(rel_lst):
    for i in rel_lst:
        print(i)



if __name__ == "__main__":
    rel_lst = [
        # ac #customer
        (1, 'A'),
        (2, 'B'),
        (1, 'C'),
        (3, 'C'),
        (2, 'E'),
        (4, 'F'),
        (5, 'G'),
        (2, 'A'),
    ]
    customers_with_same_account(rel_lst)

    [['A', 1, 2], ['B', 2], ['C', 1, 3], ['E', 2], ]