import numpy.core.fromnumeric as np1
import numpy as np


def generate_matrix(A):
    null_matrix=np.zeros([A[0]+1,A[1]+1])
    return null_matrix

def manipulate_matrix_local_Al(Que,Data,Indel,MM,M):
    len_Que=len(Que); len_Data=len(Data)
    null_matrix=generate_matrix([len_Que,len_Data])
    for iterator_i in range(len_Data):
        for iterator_j in range(len_Que):
            if Que[iterator_j] == Data[iterator_i]:
                list_will_choose=[(null_matrix[iterator_j][iterator_i])+M,
                                  (null_matrix[iterator_j+1][iterator_i])-Indel,
                                  (null_matrix[iterator_j][iterator_i+1])-Indel,0]

                choose_max=max(list_will_choose)
                null_matrix[iterator_j+1][iterator_i+1]=choose_max

            else:
                list_will_choose = [(null_matrix[iterator_j][iterator_i]) - MM,
                                    (null_matrix[iterator_j+1][iterator_i]) - Indel,
                                    (null_matrix[iterator_j][iterator_i+1]) - Indel,0]
                choose_max = max(list_will_choose)
                null_matrix[iterator_j + 1][iterator_i + 1] = choose_max
    return null_matrix


def where_is_maximum(matrix):
    max_of_matrix=np.max(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if max_of_matrix==matrix[i][j]:
                loc=[i,j]

    return loc

def backtrack(A):
    location=where_is_maximum(A)
