#Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

print('введите номер четверти от 1 до 4 - ')
a = int(input())
if a == 1:
    print('диапазон возможных координат точек в этой четверти x > 0 и y > 0')
elif a == 2:
    print('диапазон возможных координат точек в этой четверти x > 0 и y < 0')
elif a == 3:
    print('диапазон возможных координат точек в этой четверти x < 0 и y < 0')
elif a == 4:
    print('диапазон возможных координат точек в этой четверти x < 0 и y > 0')
else:
    print('вы ввели неверное число')