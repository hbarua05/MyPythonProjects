def collatz(number):
    count=0                         # numerical accumulator
    while number>1:
        if number%2!=0:             # means its odd
            count+=1                # increase count by one for every step
            number=(3*number+1)
            print(number)           # print out the number received after each step
                
        elif number%2==0:           # means its even
            count+=1
            number=int(number/2)
            print(number)
  
    print(f'It took {count} steps to reach 1')

try:                                # keyword try and except is used to make sure user inputs correct type and values 
    number=int(input('Give me a positive whole number '))
    print(number)
    collatz(number)
except ValueError:
    print('\n\nPlease provide a positive whole number')





