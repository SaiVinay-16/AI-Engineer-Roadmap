import random
li=["Apple","Mango","Pomegranate","Guava","Grapes"]
print("Original list :",li)
new_list=li.copy()
random.shuffle(new_list)
print("Shuffled list :",new_list)