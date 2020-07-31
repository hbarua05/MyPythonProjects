#p(x)=x^2-k=0. The root of polynomial gives us the sqrt of k
#The code uses the  Newton-Raphson method. It uses the iterative formula:
#guess=guess – p(guess)/p’(guess)
k=float(input('Find SQRT of...'))
diff=0.0000000001
guess=k-1
while abs(guess**2-k)>=diff:
    guess=guess-(((guess**2)-k)/(2*guess))
print('Square root of '+str(k)+' is '+str(guess))
input()
