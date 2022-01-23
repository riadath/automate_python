import re,numpy

file_in = open("in.txt")
eq_list,var_list,constant_values,matrix,var_values = [],[],[],[],{}       
t,t_str = 0,""

while t_str != "" or t == 0:
    t = 1
    # t_str = input()
    t_str = file_in.readline()
    t_str = t_str.replace(" ","")
    if t_str != "":
        if t_str[0] != '-':
            t_str = '+' + t_str
        eq_list.append(t_str)

#retrieving variable names from the equations
pattern = re.compile(r'(\d+|[+-]\d*|-?\d*\.\d+)([a-zA-Z]+\d*)')
for t_str in eq_list:
    matches = pattern.finditer(t_str)
    for i in matches:
        var_list.append(i.group(2))

#duplicate removal and lexicographical sorting     
var_list = list(dict.fromkeys(var_list))
var_list.sort()

#retrieving coefficient values from the equations
mat_size = len(eq_list)
for var in var_list:    
    var_values[var] = []
    pattern = re.compile(r'((\d+)|([+-]\d*)|(-?\d*\.\d+))(%s)'%var)
    for t_str in eq_list:
        matches = pattern.finditer(t_str)
        for i in matches:
            temp_val = i.group(1)
            if temp_val == '-':
                temp_val = '-1'
            if temp_val == '+' or temp_val == "":
                temp_val = '1'
                    
            if temp_val[0] == '+':
                temp_val = temp_val[1:len(temp_val)]
            var_values[var].append(temp_val)
            
        if len(var_values[var]) == 0:
            var_values[var].append('0')
for key in var_values.keys():
    while len(var_values[key]) < mat_size:
        var_values[key].append('0')

#retrieving constant values from the equations
pattern = re.compile(r'=((-?\d*\.\d+)|(\d+)|(-\d+))')
for t_str in eq_list:
    matches = pattern.finditer(t_str)
    for i in matches:
        constant_values.append(i.group(1))
        

t_var ='[' + ' '.join([str(elem) for elem in var_list]) + ']'
print(t_var)

for i in range(0,mat_size):
    t_list = []
    for j in var_list:
        t_list.append(float(var_values[j][i]))
        print(var_values[j][i],end="    ")
    t_list.append(float(constant_values[i]))
    matrix.append(t_list)
    print(constant_values[i])



#rearranging the rows depeding on the number of leading zeros
def sort_rows():
    for i in range(0,mat_size - 1):
        for j in range(0,mat_size - i - 1):
            pos_J,pos_J1 = 100000,100000
            for k in range(0,len(matrix[j])-1):
                if matrix[j][k] != 0:
                    pos_J = k
                    break
            for k in range(0,len(matrix[j + 1])-1):
                if matrix[j + 1][k] != 0:
                    pos_J1 = k
                    break
            if pos_J > pos_J1:
                matrix[j],matrix[j + 1] = matrix[j + 1],matrix[j]

for i in range(0,mat_size):
    #make leading zeros
    for j in range(0,i):
        mult = matrix[i][j]
        for k in range(0,len(matrix[i])):
            matrix[i][k] -= (matrix[j][k] * mult)
        sort_rows()
    #make the first non zero value 1
    div = 0
    for k in range(0,len(matrix[i])):
        if div != 0:
            matrix[i][k] /= div
        if matrix[i][k] != 0 and div == 0:
            div = matrix[i][k]
            matrix[i][k] = 1
        sort_rows()
        

print("Row Echelon Form : \n" + t_var)
for i in matrix:
    for j in i:
        print(round(j,2),end="    ")
    print("",end="\n")


for i in range(0,mat_size - 1):
    for j in range(i + 1,mat_size):
        mult = matrix[i][j]
        for k in range(0,len(matrix[i])):
            matrix[i][k] -= (matrix[j][k] * mult)
         

print("Reduced Row Echelon Form : \n" + t_var)
for i in matrix:
    for j in i:
        print(round(j,2),end="    ")
    print("",end="\n")

