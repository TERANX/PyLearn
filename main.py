import turtle as t

RND = 360  # 360 градусов в замкнутой фигуре
sides = 4  # число сторон
figs = 8  # число фигур
f_angle = RND / figs  # угол для наклона фигур
angle = RND / sides  #
dist = 120  # дистанция
count = 0  # счетчик
fig_count = 0

while fig_count < figs:
    count = 0
    while count < sides:
        t.forward(dist)
        t.right(angle)
        count += 1
    fig_count += 1
    t.right(f_angle)

t.mainloop()

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

# Ввод данных и сильная типизация
coffee = input('Сколько стоил кофе: ')
donut = input('Сколько стоил пончик: ')
print(type(coffee))
print('Вы потратили:', int(coffee) + int(donut), 'руб.')
