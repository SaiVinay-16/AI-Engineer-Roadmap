li=[20,15,60,50,11]
lar=li[0]
sec_lar=-1
for i in range(len(li)):
    if li[i]>lar:
        sec_lar=lar
        lar=li[i]
    elif li[i]<lar and li[i]>sec_lar:
        sec_lar=li[i]
print(sec_lar)