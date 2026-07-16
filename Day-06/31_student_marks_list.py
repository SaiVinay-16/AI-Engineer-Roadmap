li=[98,46,33,78,85]
print(max(li))
print(min(li))
print(sum(li)/len(li))
pass_count=0
fail_count=0
for i in li:
    if i>=35:
        pass_count+=1
    else:
        fail_count+=1
print("Pass count:",pass_count)
print("Fail count:",fail_count)