a, b = 10, 5  # объявил переменные

print(a, '+', b, '=', a + b)
print(a, '-', b, '=', a - b)
print(a, '*', b, '=', a * b)
print(a, '/', b, '=', a / b)
print(a, '//', b, '=', a // b)
print('Остаток от деления', a, 'на', b, '=', a % b)
print(a, 'в степени', b, '=', a ** b)

a += 1  # инкремент
a -= 1  # декримент

#Ввод данных и сильная типизация
coffee = input('Сколько стоил кофе: ')
donut = input('Сколько стоил пончик: ')
print(type(coffee))
print('Вы потратили:', int(coffee) + int(donut), 'руб.')
