# 36 Циклы  While 

	i = 10                          # 10
	while i < 50:                   # 20  
		print(i)                    # 30
		i += 10                     # 40    
################################################
	while True:
    print("infile loop") # бесконечный цикл
	
	# еще пример 
	
	while True:
  answer = input(" введите yes или no ") 
  if answer == 'no':
      break
	  
## переход к следующей итерации с помощью continiue

import random
 
random_num = random.randint(1, 5) # создаем числов диапазоне от 1 до 5
while True:
    num = int(input("Guess the number from 1 to 5 ")) # предлагаем ввести число
    if num != random_num: # если переменные не соовпадают
        print("Try again...") # попытайтесь снова
        continue 
    print("Congratulation", random_num) # если совпадает, то из цикла выходим
    break

######### Задание #############
# Создайте цикл, в котором нужно попросить пользователя ввести 
# в терминале два числа 
# Выведите в терминал результат деления первого числа на второе
# спросите пользователя, хочет ли он продолжать yes / no
# если пользователь no, то выходим из цикла
# если да, то все сначала

# Совет использовать float и создать прореку на 0


while True:
    one_num = float(input(" Введите первое число "))
    one_two = float(input(" Введите второе число "))
    if one_two == 0:
        print(" ты че, на ноль делить собрался ")
        break
    else:
        result = one_num / one_two
        print("результат деления чисел равен ", result)
        continiur_cicle = input( " вы хотите продолжить yes / no ")
        if continiur_cicle == 'yes':
            print("Начинаем заново ")
            continue
        elif continiur_cicle == "no":
            break

# моя задача решена верно, но ей не хватает других проверок
# например если я введу не число, то программа прервется

					### 37
					
# Сокращенный for in  используется для создания новых последовательностей
# пример нового списка в обычном for in 
all_nums = [-3, 1, 0, 10, -20, 5]

absolute_nums = []

for num in all_nums:
    absolute_nums.append(abs(num))
# абсолютное значение, это значение, которое не учитывает знак
# мы добавляет в список элементы и конвертируем функцией abs 
print(absolute_nums)
# [3, 1, 0, 10, 20, 5]

print(all_nums)
# [-3, 1, 0, 10, -20, 5]

#####################################################################
# вариант с сокращенным for in 

all_nums = [-3, 1, 0, 10, -20, 5]

absolute_nums =  [abs(num) for num in all_nums]
print(absolute_nums)
# [3, 1, 0, 10, 20, 5]

print(all_nums)
# [-3, 1, 0, 10, -20, 5]

###### сразу сокращенный вариант for in with  if 


all_nums = [-3, 1, 0, 10, -20, 5]

positive_nums = [num for num in all_nums if num > 0]

print(positive_nums)
# [1, 10, 5]

print(all_nums)
# [-3, 1, 0, 10, -20, 5]

######### сокращения для набора ########################


my_set = {1, 10, 15}

new_set = set()

for val in my_set:
    new_set.add(val * val)

print(new_set)
#{1, 100, 225}

print(my_set)
# {1, 10, 15}

## показываю как этот вариант решить сокращенно с помощью
## for in для набора

my_set = {1, 10, 15}

new_set = {val * val for val in my_set}

print(new_set)
#{1, 100, 225}

print(my_set)
# {1, 10, 15}

###################################################################################3

# Формирование нового словаря в обычном for in
my_scores = {
    'a': 10,
    'b': 7,
    'm': 14
}

scores = {}

for key, value in my_scores.items():
    scores[key] = value * 10

print(scores)
# {'a': 100, 'b': 70, 'm': 140}
print(my_scores)
# {'a': 10, 'b': 7, 'm': 14}

# вариант с сокращеным циклом для словарей

# Формирование нового словаря в обычном for in
my_scores = {
    'a': 10,
    'b': 7,
    'm': 14
}

scores = {key: value * 10 for key, value in my_scores.items()}

print(scores)
# {'a': 100, 'b': 70, 'm': 140}
print(my_scores)
# {'a': 10, 'b': 7, 'm': 14}

############################## практика ###################################################
# Создайте словарь с несколькими ключами, значения которых должны быть типа str 

# Создайте новый словарь на основании существующего, в котором значения всех
# ключей должны быть в верхнем регистре

# результат словаря вывести в терминал

# быстро и коротко, да я гений

my_dict = {
    'name': 'Persona',
    'family': 'Mercy',
    'age': '23'
}

up_reg = {key: value.upper() for key, value in my_dict.items()}
print(up_reg)

# Создайте список с элементами типа str
# из этого списка создайте новый список, в котором останутся только строки, длина которых больше 3

# пока есть шпаргалка, я непобедим

my_list = [ 'hello','my', 'friend', 'my', 'name', 'jac']

up_list = [ num for num in my_list if len(num) > 3]
print(up_list)

############################# ГЕНЕРАТОРЫ №№№№№№№№№;#################################################

# Генераторы в For In

nums = (3, 5, 10)

squares = ( num * num for num in nums) # это не кортеж

print(squares)
# <generator object <genexpr> at 0x0000013053A845F0>
print(type(squares))
# <class 'generator'>

# еще пример#################################################################################

squares = (num * num for num in range(6))

print(squares)
# <generator object <genexpr> at 0x0000019BFF174450> 

print(type(squares))
# <class 'generator'>

for num in squares:
    print(num)
# 0
# 1
# 4
# 9
# 16
# 25

# конвертация генератора в список#################################################################################

nums = [3, 5, 10]

gen = ( num * num for num in nums) # генератор можно перевести в список
squares = list(gen)

print(squares)
# [9, 25, 100]
print(type(squares))
# <class 'list'>

###########################################################################################################################



# главное преимущество генератора это размер 
from sys import getsizeof

squares_gen = (num * num for num in range(1000000)) # при увеличение генератора 
# он в размере сильно не увеличивается  в отличие от списка

print(getsizeof(squares_gen))
# 208 # РАЗМЕР генератора

print(type(squares_gen))
# генератор
# получить данные из генератора определенной ячейки
# если был бы список, можно elem[100]
for elem in squares_gen:
    print(elem)
    if elem == 100:
        break
squares_list = [num * num for num in range(1000000)]

print(getsizeof(squares_list))
# 8448728 размер списка
print(type(squares_list))
# класс лист

			#  38 классы и объекты
			
# Создаем свой класс и вызываем его 

# класс

class Car: # при создания класса начинаем с большой буквы
    def move(self):# указание на определенный экземпляр 
        # move вызывается 
        print("Car is moving") 
    def stop(self):
        print("Car stopped")

my_car = Car() 
print(type(my_car))  # <class '__main__.Car'>

print(isinstance(my_car, Car)) #True

my_car.move() # Car is moving
my_car.stop() # Car stopped

## Создание класса с методом
### __init__


class Comment:
    def __init__(self, text):  # функция конструктор при создание нового эксземпляра
        self.text = text # это атрибут
        self.votes_qty = 0 # это атрибут

    def upvote(self, qty): # а это метод 
        self.votes_qty += qty

    def reset_votes_qty(self):
        self.votes_qty = 0  # c помощью этого метода можно обнулить переменную


my_comment = Comment("My comment")
print(my_comment.text)  # First comment
print(my_comment.votes_qty)  # 0

my_comment.upvote(5)
print(my_comment.votes_qty)  # 5
my_comment.upvote(10)
print(my_comment.votes_qty)  # 10

my_comment.reset_votes_qty()
print(my_comment.votes_qty) # 0


####### Задача ########## 

#1. Создайте класс Image 
#2. Каждого экземпляра класса image должно быть три собственных атрибута 
-  resolution 
- title 
- extensoion
#3. В классе должен быть метод resize, с помощью которого можно поменять разрешение 
#   изображенияю Вы должны просто поменять значение атрибута resolution
#4. Создайте несколько экземпляров класса image и вызовите метод resize 
