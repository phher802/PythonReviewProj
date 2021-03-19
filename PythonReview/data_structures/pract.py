##get the max number of 11 digits id numbers of an input, and only count the ones that start with 8


pool = 314343435358111111111182222222222

#[pool[i:i + 11] for i in range(pool, len(pool), 11)]
# new_tuple = tuple(map(int, pool.split(' '), 11))
# print(new_tuple)

res = tuple(pool[x:x + 11]
    for x in range(0, len(pool), 11))
        
single_res = list(sub[0] for sub in res)

if "8" in single_res:
    print (len(single_res))
else:
    print(0)


# if single_res == 8:
#     print(tuple.count(res))
# else:
#     print(0)


# get_list = list((int(j) for i in res for j in i))
# list_res = len(get_list)
# print(list_res)
# filtered = [tid for tid in res if tid[0] == 8]
# print(filtered)
# print (new_pool)
#print(res)

