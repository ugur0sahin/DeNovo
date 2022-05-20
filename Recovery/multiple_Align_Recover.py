import numpy as np
from Toolbar.Aligners import generator_matrix_global_alignment_NA as globAl_PAM
from Recovery import similarityMatrix as simMat


def add_names(zero_Mat, names_correspond):
    #zero_Mat=zero_Mat.tolist()
    zero_Mat.insert(0,names_correspond)
    names_correspond.insert(0, 'x')
    for i in range(1,len(zero_Mat)):
        #for j in range(len(zero_Mat[i])):
        zero_Mat[i].insert(0,names_correspond[i])
    return zero_Mat


def evo_dist(Profile,names_correspond):
    zero_Mat=np.zeros([len(Profile),len(Profile)])

    for iterator_j in range(len(Profile)):
        for iterator_i in range(len(Profile)):
            result=globAl_PAM.globAlignment(Profile[iterator_i],Profile[iterator_j],4,4,4)
            A=simMat.start_point_Glob(result)
            toscore=simMat.matrix_path_global(Profile[iterator_i],Profile[iterator_j],result,A[0],A[1])
            score=simMat.score(toscore)
            zero_Mat[iterator_i][iterator_j]=score
    zero_Mat=zero_Mat.tolist()
    zero_Mat=add_names(zero_Mat,names_correspond)

    return zero_Mat




A=['HSap','PPan','Rattus','Gallus']
result=evo_dist(['MACWSQLRLLLWKNLTFRRRQTCQLLLEVAWPLFIFLILISVRLSYPPYEQHECHFPNKAMPSAGTLPWVQGIICNANNPCFRYPTPGEAPGVVGNFNKSIV', 'MACWPQLRLLLWKNLTFRRRQTCQLLLEVAWPLFIFLILISVRLSYPPYEQHECHFPNKAMPSAGTLPWVQGIICNANNPCFRYPTPGEAPGVVGNFNKSIV', 'MACWPQLRLLLWKNLTFRRRQTCQLLLEVAWPLFIFLILISVRLSYPPYEQHECHFPNKAMPSAGTLPWVQGIICNANNPCFRYPTPGEAPGGNFNKSIV', 'MAFWTQLGLLLWKNFTYRRRQTFQLLIEVAWPLFIFFILISVRLSYPPYEQHECHFPNKAMPSAGTLPWIQGIICNANNPCFRYPTPGESPGIVGNFNASIV'],A)
print(np.matrix(result))

#print(result.tolist())
