def plus_equals_meaning(x, y):
    # x += y
    res = x.__iadd__(y)
    x = res

    # x[0]
    res = x[0].__iadd__(y)  # calls __getitem__
    x[0] = res   # calls __setitem__

    # x.val += y
    res = x.val.__iadd__(y)
    x.val = res


def plus_equal_may_change_pointer():
    # For Immutable it changes the pointer
    x = 1
    print(id(x))
    x += 1
    print(id(x), "changed")

    # For Mutable It does inplace operation
    l = [1,2]
    print(id(x))
    l += [3]
    print(id(l), "not changed")


def append_to_list(l):
    l += [8,9,10]

# amazing obs 
l = [1,2,3]
l += [4,5]
append_to_list(l)
print(l)  # [1, 2, 3, 4, 5, 8, 9, 10]

