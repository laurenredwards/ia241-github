'''
lec 6
for loop
range function
'''

#for num in [1,2,3]:
    #print(num)
    #print(num+1)
    
#for num in [1,2,3]:
#    if num >1:
#        print(num)
    
#for c in 'this is lec6':
    #print(c)

#for c in 'this is lec6'.split():
    #print (c)
    
#for word in 'this is lec6'.split():
   # print(word)
    #for c in word:
       # print (c)
        
#for i in range(5):
   # print (i)
        
#for i in range(1,5):
    # print (i)
    

#for i in range(1,5):
    #print(i)
    
num_list = [213,321,123,312]

possible_max_num = num_list[0]

for num in num_list:
    if num > possible_max_num:
        possible_max_num = num
        
print(possible_max_num)



