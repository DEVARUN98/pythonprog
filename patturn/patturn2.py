# def patturn(raw):
#     for i in range(5,0,-1):
#         for j in range(i):
#             print("*",end="")
#         print()
# patturn(8)
a=int(input("enter initial range"))
b=int(input("enter max range"))
r=5
for i in range(a,b):
    if (i%2==0):
        for k in range(r,0,-1):
            for j in range(0,k):
                print(i,end="")
            print("")
    else:
        for l in range(r):
            for m in range(0,l+1):
                print(i,end="")
            print("")