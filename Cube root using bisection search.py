#CUBE ROOT USING BISECTION/BINARY SEARCH
while True:
    try:
        cube=float(input('What number do you want to find cube root of?: '))
        break
    except:
        print('Please enter numbers only!')


if cube>=1:             #Check if number is more than 1
    low=0
    high=cube
elif -1<cube<1:         #Check if magnitude of number is less than 1
    low=-1
    high=1              #Actual ans more than input but less than 1 since 
                        #magnitude of input is less than 1
    
else:                   #Check if number is negative and less than -1
    low=cube
    high=0
    
epsilon=10**(-10)      #Range within guess**3 should be of the given number
guess=(high+low)/2
steps=0                 #Counter for steps taken
while abs(guess**3-cube)>epsilon:
    if guess**3<cube:   #Remove the numbers lower than our guess since
                        #any number below guess will be lower than answer
        low=guess
    else:               #Remove the numbers lower than our guess since
                        #any number below guess will be more than answer
        high=guess
    guess=(high+low)/2
    steps+=1
print('steps: '+str(steps))
print('The cube root of '+str(cube)+' is '+str(round(guess,9)))

input()


