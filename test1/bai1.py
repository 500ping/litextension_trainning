# 8^3 = 6561 cases
import numpy

check_num = '123456789'
list_operators = ['', '+', '-']
num_with_operator = []
list_result = []

for i in check_num:
    num_with_operator.append([f'{i}', f'{i}+', f'{i}-'])

# [['1', '1+', '1-'], ['2', '2+', '2-'], ['3', '3+', '3-'], ['4', '4+', '4-'], ['5', '5+', '5-'], ['6', '6+', '6-'], ['7', '7+', '7-'], ['8', '8+', '8-']]
num_with_operator = num_with_operator[:-1]

a = [[0,1,2]] * 8 # [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
L_a = [list(x) for x in numpy.array(numpy.meshgrid(*a)).T.reshape(-1,len(a))] # [[0,0,0,0,0,0,0,0], [0,1,0,0,0,0,0,0], ...] 

for e_L_a in L_a:
    i0,i1,i2,i3,i4,i5,i6,i7 = e_L_a
    expression = ''
    expression += num_with_operator[0][i0] + num_with_operator[1][i1] + num_with_operator[2][i2]
    expression += num_with_operator[3][i3] + num_with_operator[4][i4] + num_with_operator[5][i5]
    expression += num_with_operator[6][i6] + num_with_operator[7][i7] + check_num[-1]
        
    total = eval(expression) # Caculate the String like '1+2-3"
    if total == 100:
        list_result.append(expression)

print(list_result)
