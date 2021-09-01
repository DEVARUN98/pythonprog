# lst=[2,4,6]
# total=sum(lst)
# #op=[total-num for num in lst]
# #print(op)
# print(list(map(lambda num:sum(lst)-num,lst)))
lst=[1,2,3,4,5,6,7,8,9]
lst1=[2,3,5,6,8,9]
common=[]
for i in lst:
    if i  in lst1:
        common.append(i)
print(common)

