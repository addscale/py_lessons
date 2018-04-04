def range_gnrtr(start, stop, step=1):
    i = start
    while i < stop:
        yield i
        i += step

def map_gnrtr(func, my_list):
    for i in my_list:
        yield func(int(i))

def enumerate_gnrtr(my_list):
    i = 0
    for l in my_list:
        yield (i, l)
        i += 1

def enumerate_gnrtr(my_list):
    i = 0
    for l in my_list:
        yield (i, l)
        i += 1

def zip_gnrtr(l1, l2):
    l_len = len(l1)
    for i in range(l_len):
        yield (l1[i], l2[i])
