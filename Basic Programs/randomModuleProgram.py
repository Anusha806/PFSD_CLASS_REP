'''
import random
n=random.randbytes(4)
print(n)

print(random.randrange(1,100))

print(random.randint(100,200))
mylist = ("Anu","12345","Agu")
mylist1 = ["Anu","12345","Agu"]
mylist2 = {"Anu","12345","Agu"}
print(random.choice(mylist1))#does not work for set

random.shuffle(mylist1)#does not work for set and tuple


'''


import string
import random
s=4
ran=' '.join(random.sample(string.ascii_uppercase + string.digits,k=s))
s1=4
ran1=''.join(random.sample(string.digits,k=6))
print(ran)
print(ran1)