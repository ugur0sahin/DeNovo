import numpy as np
from Toolbar.Aligners.MultiDimensional_Alignment.MSA_Rec.MSA_Protein_Profile_Compare_w_BLOSUM import diagonal_point
from Toolbar.Aligners.MultiDimensional_Alignment.MSA_Rec.generate_profile_random import generate_random_profile
import Toolbar.Aligners.MultiDimensional_Alignment.MSA_Rec.Profile_Generate as profGen
import Toolbar.Aligners.MultiDimensional_Alignment.MSA_Rec.TrackMSA_of_GlobAlignedMatrix as trackMOVE
from Toolbar.Aligners.MultiDimensional_Alignment.Multiple_Sequence_Alignment_AA.tracker_of_globally_MSA_matrix import *

def globAlignment(Prof1,Prof2,Indel):
    len_Que = len(Prof1[0][0]); len_Data = len(Prof2[0][0])
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
    #print(null_matrix)

    ## Manipulate Ic kısım
    for iterator_i in range(len_Data+1):
        for iterator_j in range(len_Que+1):
            if iterator_i !=0 and iterator_j !=0:
                ####
                el1=Prof1[0][::,iterator_j-1]; el2=Prof2[0][::,iterator_i-1]
                list_will_choose = [(null_matrix[iterator_i-1,iterator_j-1]) + diagonal_point(el1,el2),
                                    (null_matrix[iterator_i,iterator_j-1]) - Indel,
                                    (null_matrix[iterator_i-1,iterator_j]) - Indel]
                choose_max = max(list_will_choose)
                null_matrix[iterator_i,iterator_j] = choose_max

    nm=null_matrix
    return null_matrix

if __name__ == "__main__":
    ProfA, ProfB = generate_random_profile(30, 2), generate_random_profile(30, 2)
    ProfA, ProfB = [ProfA, 5], [ProfB, 5]
    # print(profile_profile_toGen_new_profile(ProfA,ProfB))
    a = profGen.sequence_to_profile('A-R-TG')
    b = profGen.sequence_to_profile('T-Q-MM')
    a=[a,1]
    b=[b,1]
    #a, b =[a, 1], [b, 1]
    print(a)
    print('\n')
    print(b)
    print('\n')
    globMAT=globAlignment(a,b,4)
    print(track_Global_Matrix(globMAT,[a,2],[b,1]))


    print(globMAT)