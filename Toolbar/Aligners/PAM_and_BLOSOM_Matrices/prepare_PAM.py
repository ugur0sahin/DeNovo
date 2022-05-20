import numpy as np

def import_PAM_Matrix(PAM_Table='/Users/ugurs.ahin/Desktop/DeNoVo/Toolbar/Aligners/PAM_and_BLOSOM_Matrices/PAM_table.csv'):
    f=open(PAM_Table,'r')
    file=f.readlines()
    PAM_list=[]
    for i in file:
        line1=i.rstrip('\n')
        line=line1.split(';')
        PAM_list.append(line)
    return PAM_list

def insert_Gap_score(PAM_list):
    PAM_Matrix=np.matrix(PAM_list)
    Gap_Inserted_lst =['Gap']
    for i in range(19):
        interest=PAM_Matrix[i,0]
        summation=0
        for t in range(20):
            search=PAM_Matrix[t, 0]
            if  search!= interest:
                summation += find_PAM_Value(interest,search,PAM_list)
        Gap_Inserted_lst.append(str(summation/19))
    summation=0

    for iterator_for_diagonel in range(1,len(PAM_Matrix)-1):
        A=PAM_Matrix[iterator_for_diagonel-1,iterator_for_diagonel]
        summation += int(A)
    end = summation/20
    Gap_Inserted_lst.append(str(end))

    New_Matrix=[]
    for iterator in range(21):
        if iterator == 20:
            New_Matrix.append(Gap_Inserted_lst)
            A=PAM_list[iterator]
            A.append('Gap')
            New_Matrix.append(A)
        else:
            New_Matrix.append(PAM_list[iterator])
    return New_Matrix



def find_PAM_Value(Id1,Id2,PAM_Matrix):
    found=0
    for i in range(len(PAM_Matrix)):
        for j in range(len(PAM_Matrix[i])):
            #print(PAM_Matrix[-1][i], PAM_Matrix[j][0])
            if PAM_Matrix[-1][j]==Id1 and PAM_Matrix[i][0]==Id2:
                #print(PAM_Matrix[-1][j],PAM_Matrix[i][0] )
                if not PAM_Matrix[i][j] =='0':
                    found=float(PAM_Matrix[i][j])
                elif not PAM_Matrix[j-1][i+1] == '0':
                    found=float(PAM_Matrix[j-1][i+1])
                else:
                    found = 0
                break
        if found != 0:
            break
    return found

def int_to_ID(int,PAM_tble):
    PAM_lineer_lst=PAM_tble[-1][1:]
    return PAM_lineer_lst[int]

def get_PAM_elements(A='/Users/ugurs.ahin/Desktop/DeNoVo/Toolbar/Aligners/PAM_and_BLOSOM_Matrices/PAM_table.csv'):
    PAM_list=import_PAM_Matrix(PAM_Table=A)
    PAM_list=np.matrix(PAM_list)
    AA_Val=PAM_list[::,0]
    AA_Val[-1]='-'
    AA_Val=AA_Val.transpose()
    return AA_Val