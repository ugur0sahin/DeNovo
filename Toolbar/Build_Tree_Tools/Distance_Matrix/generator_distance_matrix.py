import numpy as np
from Toolbar.Aligners.Two_Dim_Alignment.Protein_Alignment import generate_aligned_bisequence_wscore as globAl_PAM


def plug_name(zero_Mat, names_correspond):
    #zero_Mat=zero_Mat.tolist()
    zero_Mat.insert(0,names_correspond)
    names_correspond.insert(0, 'x')
    for i in range(1,len(zero_Mat)):
        #for j in range(len(zero_Mat[i])):
        zero_Mat[i].insert(0,names_correspond[i])
    return zero_Mat


def generate_distance_matrix(Profile,names_correspond,indel=7,extension=2):
    zero_Mat=np.zeros([len(Profile),len(Profile)])

    for iterator_j in range(len(Profile)):
        for iterator_i in range(len(Profile)):
            result,score, identity=globAl_PAM.generate_bisequence_aligned_calulate_score_of_prof(Profile[iterator_i],Profile[iterator_j],indel,extension,globAl_PAM.PAM_Matrix)
            #A=simMat.start_point_Glob(result)
            #toscore=simMat.matrix_path_global(Profile[iterator_i],Profile[iterator_j],result,A[0],A[1])
            #score=simMat.score(toscore)
            zero_Mat[iterator_i][iterator_j]=score
    zero_Mat=zero_Mat.tolist()
    zero_Mat=plug_name(zero_Mat,names_correspond)

    return zero_Mat
