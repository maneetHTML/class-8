n1=int(input("enter your speed 1 :"))
n2=int(input("enter your speed 2 :"))
n3=int(input("enter your speed 3 :"))
avgspeed=(n1+n2+n3)/3
print("the average speed is",avgspeed)
if n1<avgspeed:
    print("Cyclist 1 has less speed than avg speed")
elif n2<avgspeed:
    print("Cyclist 2 has less speed than avg speed")
else:
    print("Cyclist 3 has less speed than avg speed")