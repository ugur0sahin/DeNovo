import numpy as np
import random as rnd
from Toolbar.Aligners.MultiDimensional_Alignment.MSA_Rec.generate_profile_random import *

# This (diagonal) function compare one to one segments of profiles
# row and colon values sorted in terms of PAM Matrix AA range 0 == A, 1 == R through int_to_ID
# diagonal point calculate profile compare output
# find_PAM_Value find proper pair in matrix of AAs

def import_PAM_Matrix(PAM_Table):
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
        for t in range(19):
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
    for iterator in range(20):
        if iterator == 19:
            New_Matrix.append(Gap_Inserted_lst)
            A=PAM_list[iterator+1]
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

def diagonal_point(row,colon):
    np.matrix(row); np.matrix(colon)
    zero_Matrix=np.zeros([len(row),len(colon)])
    PAM_tble=import_PAM_Matrix('/Users/ugurs.ahin/Desktop/DeNoVo/Toolbar/Aligners/PAM_and_BLOSOM_Matrices/PAM_table.csv')
    Gap_inserted_PAM=insert_Gap_score(PAM_tble)
    for i in range(len(row)):
        for j in range(len(colon)):
            if i>=j:
                ID1, ID2=int_to_ID(i,Gap_inserted_PAM),int_to_ID(j,Gap_inserted_PAM)
                PAM_val=int(find_PAM_Value(ID1,ID2,PAM_tble))
                coefficient=(float(row[i])*float(colon[j]))*(PAM_val)
                if coefficient == -0:
                    coefficient=0
                zero_Matrix[i,j]=coefficient
    diagonal_result=sum(zero_Matrix)
    diagonal_result=sum(diagonal_result)
    return diagonal_result

'''
def test():
    pM_lst=import_PAM_Matrix('/Users/ugurs.ahin/Desktop/DeNoVo/Toolbar/Aligners/PAM_and_BLOSOM_Matrices/PAM_table.csv')
    insert_Gap_score(pM_lst)
    #row=[0,0.25,0.25,0.5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]; colon=[0,0.5,0,0.5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #print(len(row),len(colon))
    #diagonal_result=diagonal_point(row,colon)
    #print(diagonal_result)
'''
