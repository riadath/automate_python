import re,pprint
pp = pprint.PrettyPrinter(indent = 4)

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
    
    # print(eq_list,var_list,var_values)

    for i in range(0,mat_size):
        t_list = []
        for j in var_list:
            t_list.append(float(var_values[j][i]))
        t_list.append(float(constant_values[i]))
        matrix.append(t_list)
    return var_list,matrix

def sort_rows(matrix):
    mat_size = len(matrix)
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
    return matrix

def row_echelon(matrix):
    matrix = sort_rows(matrix)
    for i in range(0,len(matrix)):
        for j in range(0,i):
            mult = matrix[i][j]
            for k in range(0,len(matrix[i])):
                matrix[i][k] -= (matrix[j][k] * mult)
        div = 0
        for k in range(0,len(matrix[i])):
            if div != 0:
                matrix[i][k] /= div
            if matrix[i][k] != 0 and div == 0:
                div = matrix[i][k]
                matrix[i][k] = 1
    matrix = sort_rows(matrix)
    return matrix
            
def reduced_row_echelon(matrix):
    matrix = row_echelon(matrix);
    for i in range(0,len(matrix) - 1):
        for j in range(i + 1,len(matrix)):
            mult = matrix[i][j]
            for k in range(0,len(matrix[i])):
                matrix[i][k] -= (matrix[j][k] * mult)
    matrix = sort_rows(matrix)
    return matrix

def mat_solution(var_list,matrix):
    matrix = reduced_row_echelon(matrix)
    var_num = len(matrix[0]) - 1;
    for i in range(len(matrix),var_num):
        t_list = []
        for k in range(0,var_num + 1):
            t_list.append(0.0)
        matrix.append(t_list)
    
    sol_list = {}
    for i in range(0,len(matrix)):
        flag,t_list = False,[]
        for k in range(0,len(matrix[i])-1):
            if matrix[i][k] != 0.0:
                flag = True
            if k != i and matrix[i][k] != 0.0 :
                t_list.append((var_list[k],-1 * matrix[i][k]))
        sol_list[var_list[i]] = (t_list,matrix[i][len(matrix[i]) - 1],flag);
    
    pp.pprint(sol_list)
    
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
print("Row Echelon Form")
print_mat(var_list,row_echelon(matrix))
print("Reduced Row Echelon Form")
print_mat(var_list,reduced_row_echelon(matrix))

mat_solution(var_list,matrix)
