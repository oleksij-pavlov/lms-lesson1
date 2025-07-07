def common_elements():
    range_num_3 = {x for x in range(100) if x % 3 == 0}
    range_num_5 = {x for x in range(100) if x % 5 == 0}
    return range_num_3 & range_num_5

