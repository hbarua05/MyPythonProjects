t= float(input("What is the temperature? "))
source= input("What units is the temperature in? ")
target= input("To what units do you want to convert it to? ")

if source == "Kelvin":
    Celsius= t - 273.15
elif source == "Celsius":
    Celsius= t
elif source == "Fahrenheit":
    Celsius= (t-32)*5/9
elif source == "Rankine":
    Celsius= (t-491.67)*5/9
elif source == "Delisle":
    Celsius= 100-t*2/3
elif source == "Newton":
    Celsius= t*100/33
elif source == "Reaumur":
    Celsius= t*5/4
elif source == "Romer":
    Celsius= (t-7.5)*40/21
else:
    print("Please enter a valid unit!!")

if target == "Kelvin":
    print(Celsius + 273.15)
elif target == "Celsius":
    print(Celsius)
elif target == "Fahrenheit":
    print(Celsius*9/5 + 32)
elif target == "Rankine":
    print((Celsius + 273.15)*9/5)
elif target == "Delisle":
    print((100-Celsius)*3/2)
elif target == "Newton":
    print(Celsius*33/100)
elif target == "Reaumur":
    print(Celsius*4/5)
elif target == "Romer":
    print(Celsius*21/40 + 7.5)
else:
    print("Please enter a valid unit!!")


