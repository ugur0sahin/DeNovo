import numpy as np
from Toolbar.Aligners.MultiDimensional_Alignment.Multiple_Sequence_Alignment_AA.calculator_across_diagonel_point import diagonal_point
def max_glob(lst):
    if lst[0]>=lst[1] and lst[0]>=lst[2]:
        return lst[0]
    else:
        return max(lst)

def globAlignment_for_profiles(Prof1,Prof2,Indel):
    len_Que = Prof1[0].shape; len_Data = Prof2[0].shape
    #null_matrix = generate_matrix([len_Que, len_Data])

    ## Orthogonel Adjustment
    zero_list=[]
    a=np.arange(0,(-Indel*len_Que[1])-Indel,-Indel)
    #np.asarray(a)
    zero_list.append(a)
    for i in range(-Indel,(-Indel*len_Data[1])-Indel,-Indel):
        p=np.zeros([len_Que[1]+1])
        p[0]=i
        zero_list.append(p)
    null_matrix=np.asmatrix(zero_list)
    #print(null_matrix)

    ## Manipulate Ic kısım
    for iterator_i in range(len_Data[1]+1):
        for iterator_j in range(len_Que[1]+1):
            if iterator_i !=0 and iterator_j !=0:
                ####
                el1=Prof1[0][::,iterator_j-1]; el2=Prof2[0][::,iterator_i-1]
                list_will_choose = [(null_matrix[iterator_i-1,iterator_j-1]) + diagonal_point(el1,el2),
                                    (null_matrix[iterator_i,iterator_j-1]) - Indel,
                                    (null_matrix[iterator_i-1,iterator_j]) - Indel]
                choose_max = max_glob(list_will_choose)
                null_matrix[iterator_i,iterator_j] = choose_max

    return null_matrix
