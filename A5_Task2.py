#Demonstrate List Slicing

Original_list=[]
for i in range(1,11):
    Original_list.append(i)
print(Original_list)
Ext_list=Original_list[:5]
print("Extracted first five elements: ",Ext_list)
Rev_list=Ext_list[::-1]
print("Reversed Extracted elements: ",Rev_list)