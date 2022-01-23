import re
eq_list,var_list,constant_values,var_values = [],[],[],{}       

t,t_str = 0,""
while t_str != "" or t == 0:
    t = 1
    t_str = input()
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
    for j in var_list:
        print(var_values[j][i],end=" ")
    print(constant_values[i])
               
            






