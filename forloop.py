#nums = [1,4,9,16,25,36,49,64,81,100]
#for val in nums:
    #print(val)


#Q2
# search for a number x for a tuple using loop

nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,9)
x = 9
idx = 0
for el in nums:
    if( el == x):
        print(" number found at idx",idx)
    idx += 1

