def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')

#You can also use for on numbers using the range function
for i in range(1, 6):
    print(i)

#prints 1-5
#Note that the second of these two numbers is not included in the list 
#that is output by Python (meaning range(1, 6) counts from 1 to 5, but 
#does not include the number 6). That is because "range" is half-open, 
#and by that we mean it includes the first value, but not the last.