import re,pprint,copy
from string import printable
pp = pprint.PrettyPrinter(indent = 4)

def print_mat(var_list,matrix):
    print('[' + ' '.join([str(elem) for elem in var_list]) + ']')
    for i in matrix:
        for j in i:
            print(round(j,2),end="    ")
        print("",end="\n")
    print("\n")

def augmented_matrix(input_list): 
    eq_list,var_list,constant_values,var_values,mat_size,matrix = [],[],[],{},0,[]
    for t_str in input_list:
        t_str = t_str.replace(" ","").strip()
        if t_str != "":
            mat_size += 1
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
                if temp_val == '-0':
                    temp_val = '0'
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

def row_echelon(matrix):    
    for i in range(len(matrix)):
        lead = 0
        for j in range(len(matrix[i]) - 1):
            if matrix[i][j] == 0:
                lead += 1
            else:
                break
        lead_mn,lead_idx = lead,-1
        for k in range(i + 1,len(matrix)):
            t_lead = 0
            for j in range(len(matrix[k]) - 1):
                if matrix[k][j] == 0:
                    t_lead += 1
                else :
                    break
            if t_lead < lead_mn:
                lead_mn = t_lead
                lead_idx = k
        if lead_idx != -1:
            matrix[i],matrix[lead_idx] = matrix[lead_idx],matrix[i]
        div,div_idx = 0,-1
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0 and div == 0:
                div = matrix[i][j]
                div_idx = j
            if div:
                matrix[i][j] /= div
        if div == 0:
            continue
        for j in range(i + 1,len(matrix)):
            if matrix[j][div_idx] != 0:
                mult = matrix[j][div_idx]
                for k in range(len(matrix[j])):
                    matrix[j][k] -= (mult * matrix[i][k])
        
    return matrix    
                  
def reduced_row_echelon(matrix):
    matrix = row_echelon(matrix)

    for i in range(len(matrix)):
        pos = -1
        for k in range(len(matrix[i])):
            if matrix[i][k] != 0:
                pos = k
                break
        if pos != -1:
            for j in range(i):
                if matrix[j][pos] != 0:
                    mult = matrix[j][pos]
                    for k in range(len(matrix[j])):
                        matrix[j][k] -= (mult * matrix[i][k])
    return matrix

def mat_solution(var_list,matrix):
    matrix = reduced_row_echelon(matrix)
    t_matrix = []
    t_list = []
    
    for k in range(0,len(var_list) + 1):
        t_list.append(0.0)
    for i in range(len(matrix)):
        if matrix[i][i] == 1 or len(matrix) == len(var_list):
            t_matrix.append(matrix[i])
        else:
            t_matrix.append(t_list)
            t_matrix.append(matrix[i])
    matrix = t_matrix
    # pp.pprint(matrix)
    soln_list = {}
    for i in range(len(matrix)):
        flag,t_list = False,[]
        for k in range(len(matrix[i])-1):
            if matrix[i][k] != 0.0:
                flag = True
            if k != i and matrix[i][k] != 0.0 :
                t_list.append((var_list[k],-1 * matrix[i][k]))
        soln_list[var_list[i]] = (t_list,matrix[i][len(matrix[i]) - 1],flag);

    # pp.pprint(soln_list)
    
    printable_soln = {}
    for it in var_list:
        if soln_list[it][2] == False:
            printable_soln[it] = it
        else:
            if len(soln_list[it][0]) == 0:
                printable_soln[it] = str(round(soln_list[it][1],2))
            else:
                t_str = ""
                for jt in soln_list[it][0]:
                    if jt[1] > 0 and t_str != "":
                        t_str += '+'
                    t_str += str(round(jt[1],2))+jt[0] + " "
                if soln_list[it][1] != 0.0:
                    if soln_list[it][1] > 0 and t_str != "":
                        t_str += '+'
                    t_str += str(round(soln_list[it][1],2))
                printable_soln[it] = t_str
                
    print("___________Solution___________\n")
    for it in printable_soln.keys():
        print(it + " = " + printable_soln[it])


def main():
    file_in = open("in.txt")
    inp_list,t_str = [],"#"
    while t_str != "" or t_str == "#":
        # t_str = input()           #uncomment this line for console input
        t_str = file_in.readline()  #and comment this line for console input
        inp_list.append(t_str)
    var_list,g_matrix = augmented_matrix(inp_list)
    
    print("___________Augmented Matrix___________\n")
    print_mat(var_list,g_matrix)          
    print("___________Row Echelon Form___________\n")
    print_mat(var_list,row_echelon(copy.deepcopy(g_matrix)))
    print("___________Reduced Row Echelon Form___________\n")
    print_mat(var_list,reduced_row_echelon(copy.deepcopy(g_matrix)))
    mat_solution(var_list,copy.deepcopy(g_matrix))



main()