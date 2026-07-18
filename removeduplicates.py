dup_list = [1,2,3,4,5,6,7,7,6,5,434,534,2,2,1,3,45,7,8,9]
final_list=[]
c=[]
for i in dup_list:
    if i not in final_list:
        final_list.append(i)
print(final_list)
