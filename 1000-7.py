import time

# Функция "печати" по буквам
def slow_print(text, delay=0.1):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)

# Функция точек
def tocka():
    for i in range(3):
        slow_print(". ", delay=0.5)  # три точки с паузой 0.5 сек
    return ""  # ничего не возвращаем (пустая строка)

# Основной цикл
x = 1000
while x > 0:
    y = x
    x -= 7

    # медленно печатаем выражение
    slow_print(f"{y} - 7 = {x} ", delay=0.3)

    # вызываем tocka()
    tocka()

    print()  # чтобы каждый расчёт был на новой строке
    time.sleep(0.05)

#test