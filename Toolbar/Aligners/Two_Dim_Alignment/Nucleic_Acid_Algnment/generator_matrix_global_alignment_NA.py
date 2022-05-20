import numpy as np

def globAlignment(Que,Data,Indel,MM,M):
    len_Que = len(Que); len_Data = len(Data)
    #null_matrix = generate_matrix([len_Que, len_Data])

    ## Orthogonel Adjustment
    zero_list=[]
    a=np.arange(0,(-Indel*len_Que)-Indel,-Indel)
    #np.asarray(a)
    zero_list.append(a)
    for i in range(-Indel,(-Indel*len_Data)-Indel,-Indel):
        p=np.zeros([len_Que+1])
        p[0]=i
        zero_list.append(p)
    null_matrix=np.asmatrix(zero_list)

    ## Manipulate Ic kısım
    for iterator_i in range(len_Data+1):
        for iterator_j in range(len_Que+1):
            if iterator_i !=0 and iterator_j !=0:
                el1=Que[iterator_j-1]; el2=Data[iterator_i-1]
                if el1 == el2:
                    list_will_choose = [(null_matrix[iterator_i-1,iterator_j-1]) + M,
                                        (null_matrix[iterator_i,iterator_j-1]) - Indel,
                                        (null_matrix[iterator_i-1,iterator_j]) - Indel]
                    choose_max = max(list_will_choose)
                    null_matrix[iterator_i,iterator_j] = choose_max
                else:
                    list_will_choose = [(null_matrix[iterator_i - 1,iterator_j - 1]) - MM,
                                        (null_matrix[iterator_i,iterator_j - 1]) - Indel,
                                        (null_matrix[iterator_i - 1,iterator_j]) - Indel]
                    choose_max = max(list_will_choose)
                    null_matrix[iterator_i,iterator_j] = choose_max
    ed=np.zeros([len_Data+1,len_Que+1])

    for i in range(len(Que)+1):
        for j in range(len(Data)+1):
            ed[j][i]=null_matrix[j,i]
    return ed #export without non-matrix from numpy


