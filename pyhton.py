import random
n=random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
mylist=["jadeja","ashwin","rahmane","shami","dhoni","virat"]
mylist1=["jadeja","ashwin","rahmane","shami","dhoni","virat"]
print(random.choice(mylist))
#print(random.choice(mylist1))
random.shuffle(mylist)