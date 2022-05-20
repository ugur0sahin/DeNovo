import numpy as np
from Toolbar.Aligners.PAM_and_BLOSOM_Matrices.prepare_PAM import find_PAM_Value, import_PAM_Matrix

def generate_matrix(A):
    null_matrix=np.zeros([A[0]+1,A[1]+1])
    return null_matrix

def manipulate_matrix_local_Al(Que,Data,Indel,PAM_path):
    len_Que=len(Que); len_Data=len(Data)
    null_matrix=generate_matrix([len_Que,len_Data])
    PAM_MAT=import_PAM_Matrix(PAM_Table=PAM_path)
    for iterator_i in range(len_Data):
        for iterator_j in range(len_Que):
            list_will_choose=[(null_matrix[iterator_j][iterator_i])+find_PAM_Value(Que[iterator_j],Data[iterator_i],PAM_MAT),
                              (null_matrix[iterator_j+1][iterator_i])-Indel,
                              (null_matrix[iterator_j][iterator_i+1])-Indel,0]

            choose_max=max(list_will_choose)
            null_matrix[iterator_j+1][iterator_i+1]=choose_max

    return null_matrix

def where_is_maximum(matrix):
    max_of_matrix=np.max(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if max_of_matrix==matrix[i][j]:
                loc=[i,j]

    return loc

def backtrack(matrix, seqx, seqy):
    location=where_is_maximum(matrix)
    leny = len(matrix)
    lenx = len(matrix[0])
    y = location[0]
    x = location[1]
    way = [[matrix[location[0]][location[1]], "start"]]
    seq1 = ''
    seq2 = ''
    for i in range(y, leny-1, 1):
        seq2 += seqy[i]
        seq1 += '-'
    while x != 0 and y != 0:
        up = matrix[y - 1][x]
        left = matrix[y][x - 1]
        cross = matrix[y - 1][x - 1]
        if up == 0 and left == 0 and cross == 0:
            way.insert(0, [cross, "cross"])
            x = x - 1
            y = y - 1
            seq1 = seqx[x] + seq1
            seq2 = seqy[y] + seq2
            break
        elif max(up, left, cross) == cross:
            way.insert(0, [cross, "cross"])
            x = x - 1
            y = y - 1
            seq1 = seqx[x] + seq1
            seq2 = seqy[y] + seq2

        elif max(up, left, cross) == left:
            way.insert(0, [left, "left"])
            x = x - 1
            seq1 = seqx[x] + seq1
            seq2 = '-' + seq2

        elif max(up, left, cross) == up:
            way.insert(0, [up, "up"])
            y = y - 1
            seq1 = '-' + seq1
            seq2 = seqy[y] + seq2
    a = ''
    for i in range(len(seqy)-len(seq2)):
        a += seqy[i]
        seq1 = '-' + seq1
    seq2 = a + seq2

    compare = ''
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            compare += '|'
        else:
            compare += ' '
    res = seq1 + '\n' + compare + '\n' + seq2
    return res

def score(res):
    res = res.split("\n")
    del res[1]
    match = 0
    for i in range(len(res[1])):
        if res[0][i] == res[1][i]:
            match += 1
    return (match/len(res[0]))

def End_Local_Alignment(seqx,seqy,Indel=7,PAM='/Users/ugurs.ahin/Desktop/DeNoVo/Toolbar/Aligners/PAM_and_BLOSOM_Matrices/PAM_table.csv'):
    matrix=manipulate_matrix_local_Al(seqx,seqy,Indel,PAM)
    A=backtrack(matrix,seqy,seqx)
    end_score=score(A)
    return A, end_score

