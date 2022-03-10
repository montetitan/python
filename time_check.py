import time
#import itertools
start_time = time.time()
r= []
listA = [1,2,3,4,5]
listB = [11,12,13,14,15]

# for x in listA:
# 	for y in listB:
# 		r.append((x, y))

# for x, y in itertools.product(listA, listB):
# 	r.append((x, y))

print (r)
#main()
print("--- %s seconds ---" % (time.time() - start_time))