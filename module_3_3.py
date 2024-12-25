print()
print('1.Функция с параметрами по умолчанию:')
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(b = 'привет')             # вызов с 1 аргументом + 2 по умолчанию
print_params(a = 4, c = False)         # вызов с 2 аргументами + 1 по умолчанию
print_params(a = 5, b = 'link', c = 6) # вызов с 3 аргументами
print_params()                         # вызов без аргументов
print_params(b = 25)                   # вызов работает
print_params(c = [1,2,3])              # вызов работает

print()
print('2.Распаковка параметров:')
values_list = [2, "line", False]
values_dict = {'a' : [2,3,4], 'b': 'good', 'c' : 8}
print_params(*values_list)
print_params(**values_dict)

print()
print('3.Распаковка + отдельные параметры:')
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)