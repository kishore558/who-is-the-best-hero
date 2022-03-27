name1=input("enter your favourite hero name= ")
n1=int(input("no of hits  "))
a1=int(input("nof averages"))
m1=int(input("no of flops "))
name2=input("enter your favourite hero name= ")
n2=int(input("no of hits  "))
a2=int(input("nof averages"))
m2=int(input("no of flops "))
#for hit movie 10 points
#for average moveie 5 points
#for flop movie 2points
total1=n1*10+a1*5+m1*2
total2=n2*10+a2*5+m2*2
print("the best hero is")
print(name1)if total1>total2 else print(name2)
