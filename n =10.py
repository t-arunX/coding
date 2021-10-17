n =5
for i in range(n):
    for i in range(n//2-i):
        print(end=" ")
    for j in range(i):
        print("*", end=" ")
    for i in range(n//2-i):
        print(end=" ")
    print("\n")  
