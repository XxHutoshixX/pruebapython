num1 = int(input("Ingresa un numero:\n"))
num2 = int(input("Ingresa otro numero:\n"))
num3 = int(input("Ingresa otro numero:\n"))

if num2<num1>num3 :
	print(num1," es mayor que ",num2," y ",num3)
elif num1<num2>num3 :
	print(num2," es mayor que ",num1," y ",num3)
	
elif num1<num3>num2 :
	print(num3," es mayor que ",num1," y ",num2)
	
else:
	print("Los numeros son iguales")
		
