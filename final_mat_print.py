import re

def print_mat(var_list,matrix):
    print('[' + ' '.join([str(elem) for elem in var_list]) + ']')
    for i in matrix:
        for j in i:
            print(round(j,2),end="    ")
        print("",end="\n")

def augmented_matrix(input_list): 
    eq_list,var_list,constant_values,var_values,mat_size,matrix = [],[],[],{},0,[]
    for str in input_list:
        str = str.replace(" ","").strip()
        if str != "":
            mat_size += 1
            if str[0] != '-':
                str = '+' + str
            eq_list.append(str)
            
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
    for var in var_list:    
        var_values[var] = []
        pattern = re.compile(r'((\d+)|([+-]\d*)|(-?\d*\.\d+))(%s)'%var)
        for t_str in eq_list:
            matches = pattern.finditer(t_str)
            match_size = len(pattern.findall(t_str))
            for i in matches:
                temp_val = i.group(1)
                if temp_val == '-':
                    temp_val = '-1'
                if temp_val == '+' or temp_val == "":
                    temp_val = '1'       
                if temp_val[0] == '+':
                    temp_val = temp_val[1:len(temp_val)]
                var_values[var].append(temp_val)
            if match_size == 0:
                var_values[var].append(0)
            if len(var_values[var]) == 0:
                var_values[var].append('0')
    #retrieving constant values from the equations
    pattern = re.compile(r'=((-?\d*\.\d+)|(\d+)|(-\d+))')
    for t_str in eq_list:
        matches = pattern.finditer(t_str)
        for i in matches:
            constant_values.append(i.group(1))
    
    print(eq_list,var_list,var_values)

    for i in range(0,mat_size):
        t_list = []
        for j in var_list:
            t_list.append(float(var_values[j][i]))
        t_list.append(float(constant_values[i]))
        matrix.append(t_list)
    return var_list,matrix


#taking input
file_in = open("in.txt")
inp_list,t_str = [],"#"
while t_str != "" or t_str == "#":
    # t_str = input()
    t_str = file_in.readline()
    inp_list.append(t_str)

var_list,matrix = augmented_matrix(inp_list)

print("Augmented Matrix")
print_mat(var_list,matrix)       