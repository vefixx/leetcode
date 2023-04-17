class Solution(object):
    def singleNumber(self, nums):
        result_num = [] #список result_num, далее в него поместим наше одинокое число и выведем
        new_num = 0 #в этой переменной мы будем выводить какое число у нас одинокое
        for i in nums:
            new_num = nums.count(i) #считаем сколько раз у нас встречаются числа с помощью count()
            if new_num == 1: #далее если в списке есть число, которое встречается 1 раз, то мы     
                result_num.append(i)#мы его добавляем в наш список
        if len(result_num) == 1: #если в списке есть хотя бы одно такое число, то возвращаем его
            return result_num[0]
        else: #иначе ничего не возвращаем
            return None
        
