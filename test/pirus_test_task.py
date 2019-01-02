# Пирус Анастасия
#  1. найти два простых пятизначных числа
#  2. найти их произведение
#  3. если это число палиндром - записать в массив
#  4. найти максимальный элемент массива

#  Поиск простого числа реализован с помощью алгоритма Решето Эратосфена 
import numpy as np

def find_prime(n):
    prime_array = list(range(n)) #создали массив всех чисел от 10000 до n
    prime_array[1] = 0    # единица не считается простым числом, на ее место ставим 0
    i = 2 #т.к первые два уже нули, то начинаем проверку с 3- го элемента
    while i<n:
        if prime_array[i] != 0: #если элемент массива не нулевой то
            pair_num = i*2 #увеличиваем данный элемент в два раза
            while pair_num<n: #на место составных чисел пишем нули
                prime_array[pair_num] = 0
                pair_num = pair_num +i
        i += 1
    prime = [] #массив для хранения всех простых чисел в промежутке
    for i in prime_array:
        if prime_array[i] != 0:
            prime.append(prime_array[i])#заполняем массив не нулевыми элементами в массиве с простыми числами
    return prime #возвращаем массив

# Нахождение произведения комбинации чисел в массиве и проверка является ли число на палиндромом
def check_polimdrom(array):
    polindrom = []
    for i,num1 in enumerate(array):
        for num2 in array[i+1:]:
            #multiplication = num1*num2
            if str(num1*num2) == str(num1*num2)[::-1]: # сравниваем число и число записанное наоборот, если они совпадают, то
                idx_n1, idx_n2 = i, i+1
                polindrom.append([num1*num2, num1,num2])    #записываем в матрицу значения чисел и их произведение                  
    return max(polindrom)

if __name__ == "__main__":
    prime = [p for p in find_prime(10**5) if p>10**4]
    multi_prime, number1, number2 = check_polimdrom(prime)

    print('First number is: {0}\nSecond number is: {1}\nMaximume multiplication is: {2}'.format(number1,number2,multi_prime))
    
     
    
     
