from functools import reduce
li=[1,2,3,4,5,-1,-2,-3]
neg_remove=list(filter(lambda x:x>=0,li))
print(neg_remove)
sq_filtered=list(map(lambda x:x*x,neg_remove))
print(sq_filtered)
total_sum=reduce(lambda temp,x:temp+x,sq_filtered)
print(total_sum)