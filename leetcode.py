Leetcode  марафон 
https://www.youtube.com/watch?v=Pp84Sv041xA

Первая задача
я ее не понял, она 9я в leetcode, решение пока писать не буду 

217 задача 20 минута
тут задача попроще, надо посмотреть дубликаты
автор использовал set 
 обьясняю алгоритм, возвращащаем, длина строке не равна длины набору строки

это весь алгоритм

203 задача 23 минута

вообще ее не понял

остановился на 33 минуте 

#######
338 Битовые операторы
Учитывая целое число n, верните массив ans длины n + 1 
таким образом, чтобы для каждого i (0 <= i <= n) ans[i] было числом 1 в двоичном представлении i.

Я так понимаю надо конвертировать десятичное число в двоичное
# воо,ot не понял с движением бита

class Solution:
    def countBits(self, n: int) -> List[int]:

        ans = [0]

        for i in range(1,n+1):

            cur = 0

            while i:

                cur += i & 1 # если последнее число 1, он возвращает 1
                              # если последнее число 0, он возвращает 0
                i >>= 1 # идеn сдвиг числа
            ans.append(cur)

        return ans
# аналогичное решение этой задачи 
	ans = [0] for i in range(1, n+1):ans.append(ans[i>>1]+i%2) 
	
# и это легкие задачи
	
	############################# 929
	
##	подсчет емэйлов
	
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int: # не смог скопировать код в мы code тут ошибка была

        unique = set() # set помогает считать уникальные мэйлы

        for e in emails:
            name, dom = e.split('@') # split разделяет строку

            name = name.split('+')[0] # после + емэйл игнорится, нам нужно только то что до плюса
            name = name.replace('.','')

            unique.add(f'{name}@{dom}')
        return len(unique)
		
# emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# ответ 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

####  643		 50 минута

#Вам задан целочисленный массив nums, состоящий из n элементов, и целое число k.

#Найдите непрерывный подмассив, длина которого равна k и который имеет максимальное среднее значение,
 #и верните это значение. Будет принят любой ответ с ошибкой вычисления менее 10-5.
 
 # nums = [1,12,-5,-6,50,3], k = 4
 # считаем максимальное значение массива равного 4м и сравниваем с другими
 # он в видео обьяснил, так что я понял 
 
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        q = deque([]) #  двухстороний массив, который я не понимаю

        ans = -float('inf') # когда мы ищем максимум, можно сделать его с пинус бесконечностью
 
        for num in nums:
            q.append(num) 
            if len(q) == k:
                ans = max(ans,sum(q)/k)
            if len(q) > k: 
                q.popleft() # удаляет элемент спереди 
                ans = max(ans,sum(q)/k) 
        return ans # этот код долго выполняется, поэтому он начал делать другой
		
## альтернативное решение задачи

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        q = deque([])

        ans = -float('inf')

        cnt = 0
        cur = 0
        for i in range(len(nums)): # очередь с фиксированной длиной 
            cur +=nums[i]
            cnt += 1
            if cnt == k:
                ans = max(ans, cur/k)
            if cnt > k:
                cur -= nums[i-k]
                ans= max(ans,cur/k)
        return ans
######################################################
59 минута 

######### ########### 283 move zero

нужно все нолики в массиве передвинуть в конец массива
и не создавать для этого копию массива
Input: nums = [0,1,0,3,12]

##  Код
nums = [0, 1, 0, 3, 12]
j = 0
for i in range(len(nums)):  # только так можно перебирать список
    if nums[i] != 0:
        # это вот так он переставляет местами
        nums[i], nums[j] = nums[j], nums[i]
        j += 1
print(nums)
# в принципе я понял как он это сделал, мне понравилось

#################  ############  367
#Учитывая положительное целое число num, верните true, 
#если num является идеальным квадратом, или false в противном случае.
#Идеальный квадрат - это целое число, которое является квадратом целого числа. 
#Другими словами, это произведение некоторого целого числа на само себя.
#Вы не должны использовать какие-либо встроенные библиотечные функции, такие как sqrt.

Input: num = 16
Output: true
# ИСПОЛЬЗУЕМ БИНАРНЫЙ ПОИСК, в 5 классе изучал, когда миша ответил 50
# l , r это left и right 
# не смог понять логику решения задачи
        if num == 1: # проверка на единичку, в виде исключения
            return True:
        l, r = 1, num // 2 # целочисленное деление
        while l <= r: # меньше или равен чем r бинарный поиск

            mid = (l + r) // 2 # серединка  

            sq = mid * mid

            if sq == num:
                return True 
                
            if sq < num:
                l = mid + 1 
            else:
                r = mid - 1

        return False

####  1 час 16 минут Задача  258 ### 
# Учитывая целое число, многократно складывайте все его цифры до тех пор, 
#   пока в результате не останется только одна цифра, и возвращайте ее.

# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.

# я понимаю что число надо разделить на элементы списка, но не понимаю как 

num = 38


while num >= 10:  # если одно число, мы его возвращаем

    cur = num

    new_num = 0

    while cur: # Внутренний цикл while продолжается до тех пор, пока cur не равен 0. вот что я не понял, почему так то
# но я хотя бы понял решение задачи
        cur, d = divmod(cur, 10)  # каждый раз делим на 10
        # смотри  я понял, cur = 3 d = 8
        # решил понять чему равно d, вторая строка чему равно cur
        # print(d)
        # 8     3
        # 3     0
        # 1     1
        # 1     0
        # 2     2
        new_num += d  # new_num = new_num + d
        print(new_num)

    num = new_num

print(num)

