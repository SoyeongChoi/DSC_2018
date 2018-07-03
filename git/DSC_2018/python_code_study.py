>> colors = ["a","b","c","d"]
>> result = ""
>> for s in colors:
...   result += s
>> result
'abcd'

     ( = )

>> colors = ["a","b","c","d"]
>> result = ""
>> result = ''.join(colors)
>> result
'abcd'


>> result = " ".join(colors)
'a b c d'
>> result = ",".join(colors)
'a,b,c,d'
>> example = 'python,jquery,javascript'
>> a, b, c = example.split(",")
>> a
'python'


-List Comprehensions
(1)
>>> temp = []
>>> for i in range(10):
...  temp.append(i)
...
>>> print(temp)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

	( = )

>>> result = [i for i in range(10)]
>>> print(result)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

(2)
>>> word_1 = "Hello"
>>> word_2 = "World"
>>> result = [i+j for i in word_1 for j in word_2]
>>> result
['HW', 'Ho', 'Hr', 'Hl', 'Hd', 'eW', 'eo', 'er', 'el', 'ed', 'lW', 'lo', 'lr', 'll', 
'ld', 'lW', 'lo', 'lr', 'll', 'ld', 'oW', 'oo', 'or', 'ol', 'od']

-> [i+j for i in word_1 for j in word_2]
(=)   for i in word_1:
	for j in word_2:

(3)
>>> case_1 = ["A","B","C"]
>>> case_2 = ["D","E","A"]
>>> result = [i+j for i in case_1 for j in case_2]
>>> result
['AD', 'AE', 'AA', 'BD', 'BE', 'BA', 'CD', 'CE', 'CA']

 (( 2-dimetional List))
>>> result = [[i+j for i in case_1] for j in case_2]
>>> result
[['AD', 'BD', 'CD'], ['AE', 'BE', 'CE'], ['AA', 'BA', 'CA']]

-> [[i+j for i in case_1] for j in case_2]
 for i in case_1 :

