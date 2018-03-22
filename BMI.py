# -*- coding: utf-8 -*-

Height=float(input('Please enter your Height: '))
Weight=float(input('Please enter your Weight: '))

BMI = Weight/(Height*Height)

# print (BMI)

if BMI < 18.5:
	print ('Your BMI IS > Too Thin')
elif BMI >=18.5 and BMI<25:
	print ('Your BMI IS > Normal')
elif BMI >=25 and BMI<28:
	print ('Your BMI IS > Overweight')
elif BMI >=28 and BMI<32:
	print ('Your BMI IS > Fat')
elif BMI >=32:
	print ('Your BMI IS > High Fat')
