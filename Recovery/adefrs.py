import numpy as np
from Toolbar.Aligners.PAM_and_BLOSOM_Matrices.prepare_PAM import find_PAM_Value, import_PAM_Matrix

def generate_matrix(A):
    null_matrix=np.zeros([A[0]+1,A[1]+1])
    return null_matrix

def manipulate_matrix_local_Al(Que,Data,Indel):
    len_Que=len(Que); len_Data=len(Data)
    null_matrix=generate_matrix([len_Que,len_Data])
    PAM_MAT=import_PAM_Matrix()
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

seqy1 = 'ATGATGGCTAAT'
seqx1 = 'ATCGGTAAT'

matrix = manipulate_matrix_local_Al(seqy1, seqx1 ,10)
def matrix_path(seqx, seqy, matrix, y, x):
    way = [[matrix[y][x], "start"]]
    seq1 = ''
    seq2 = ''
    while matrix[y][x] != 0:
        up = matrix[y-1][x]
        left = matrix[y][x-1]
        cross = matrix[y-1][x-1]
        if cross == 0:
            way.insert(0, [cross, "cross"])
            x = x - 1
            y = y - 1
            seq1 = seqx[x] + seq1
            seq2 = seqy[y] + seq2


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
    compare = ''
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            compare += '|'
        else:
            compare += ' '
    res = seq1 + '\n' + compare + '\n' + seq2

    print(way)
    print(matrix)
    return res

print(matrix_path(seqx1, seqy1, matrix, where_is_maximum(matrix)[0], where_is_maximum(matrix)[1]))