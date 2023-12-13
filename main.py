def bmi_calulator(weight,height):
    return  weight/height**2

weight=float(input("ВВедите свой вес в киллограммах: "))
height=float(input("Вваедите свой рост в сантиметрах: "))

bmi=bmi_calulator(weight,height)

if bmi<18.5:
    print(f'У вас недовес.Ваш показатель bmi={bmi}')
elif bmi>18.5 and bni<24.9:
    print(f'у вас перевес.Ваш показатель bmi={bmi}')
else:
    print(f'У вас перевес.Ваш паказатель bmi={bmi}')