import numpy as np
from Toolbar.Aligners.PAM_and_BLOSOM_Matrices.prepare_PAM import import_PAM_Matrix, find_PAM_Value

PAM_Matrix = import_PAM_Matrix()

def Matrix_for_Protein_GlobAlignment(AA1, AA2, Indel, PAM_Matrix):
    len_Que = len(AA1)
    len_Data = len(AA2)
    # null_matrix = generate_matrix([len_Que, len_Data])

    ## Orthogonel Adjustment
    zero_list = []
    a = np.arange(0, (-Indel * len_Que) - Indel, -Indel)
    # np.asarray(a)
    zero_list.append(a)
    for i in range(-Indel, (-Indel * len_Data) - Indel, -Indel):
        p = np.zeros([len_Que + 1])
        p[0] = i
        zero_list.append(p)
    null_matrix = np.asmatrix(zero_list)

    ## Manipulate Ic kısım
    for iterator_i in range(len_Data + 1):
        for iterator_j in range(len_Que + 1):
            if iterator_i != 0 and iterator_j != 0:
                el1 = AA1[iterator_j - 1]; el2 = AA2[iterator_i - 1]
                #if not el1=='-' or el2=='-':
                for i in range(len(PAM_Matrix[-1])):
                    if PAM_Matrix[-1][i] == el1:
                        loc1 = i
                        for j in range(len(PAM_Matrix) - 1):
                            if el2 in PAM_Matrix[j]:
                                UniqueMatch = PAM_Matrix[j][loc1]
                            #else:
                            #    UniqueMatch=Indel
                list_will_choose = [(null_matrix[iterator_i - 1, iterator_j - 1]) + int(UniqueMatch),(null_matrix[iterator_i, iterator_j - 1]) - Indel,(null_matrix[iterator_i - 1, iterator_j]) - Indel]
                choose_max = max(list_will_choose)
                null_matrix[iterator_i, iterator_j] = choose_max

    ed = np.zeros([len_Data + 1, len_Que + 1])
    #ed =np.matrix(null_matrix)

    for i in range(len(AA1) + 1):
        for j in range(len(AA2) + 1):
            ed[j][i] = null_matrix[j, i]
    #print(ed.tolist())
    return ed  # export without non-matrix from

def where_is_maximum(matrix):
    max_of_matrix=np.max(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if max_of_matrix==matrix[i][j]:
                loc=[i,j]

    return loc

def start_point_Glob(matrix):
    return [len(matrix)-1, len(matrix[0])-1]

def max_f(up, left, cross):
    if cross >= up and cross >= left:
        bg=cross
    else:
        bg=max(up,left,cross)
    return bg

#To calculate score get ExtGap, Gap and PAM Matrix.
def matrix_path_global(seqx, seqy, matrix, y, x):
    mat_res=matrix.tolist()
    '''
    for i in mat_res:
        print(i)
    '''
    way = [[matrix[y][x], "start"]]
    seq1 = ''
    seq2 = ''
    length_a=x
    length_b=y
    while x != 0 and y != 0:
        up = matrix[y-1][x]
        left = matrix[y][x-1]
        cross = matrix[y-1][x-1]


        if max_f(up, left, cross) == cross:
            way.insert(0, [cross, "cross"])
            x = x - 1
            y = y - 1
            seq1 = seqx[x] + seq1
            seq2 = seqy[y] + seq2

        elif max_f(up, left, cross) == left:
            way.insert(0, [left, "left"])
            x = x - 1
            seq1 = seqx[x] + seq1
            seq2 = '-' + seq2

        elif max_f(up, left, cross) == up:
            way.insert(0, [up, "up"])
            y = y - 1
            seq1 = '-' + seq1
            seq2 = seqy[y] + seq2

    compare = ''
    pair_counter=0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            pair_counter +=1
            compare += '|'
        else:
            compare += ' '
    res = seq1 + '\n' + compare + '\n' + seq2
    if length_a>length_b:
        identity = pair_counter/length_a
    else:
        identity = pair_counter/length_b
    #print(way)
    #print(matrix.tolist())
    return res, identity, seq1 ,seq2

def calculator_score(seq1,seq2,gap_pen, extension,PAM_Matrix):
    score=0
    for i in range(len(seq1)):
        if seq1[i]=='-' and seq2[i] != '-':
            try:
                if seq1[i-1]=='-':
                    score = score -  extension
                else:
                    score =score - gap_pen
            except:
                score = score - gap_pen

        elif seq2[i] == '-' and seq1[i] != '-':
            try:
                if seq2[i-1]=='-':
                    score = score - extension
                else:
                    score = gap_pen
            except:
                score = score - gap_pen
        elif seq1[i] == '-' and seq2[i] == '-':
            score += 0
        else:
            score += find_PAM_Value(seq1[i],seq2[i],PAM_Matrix)
    return score

#def raw_score(matrix, way, PAM_Matrix, Indel, GapExt):

def generate_bisequence_aligned_calulate_score_of_prof(AA_1,AA_2,In_del,Ext, PAM_Matrix):
    result1 =Matrix_for_Protein_GlobAlignment(AA_1,AA_2,In_del,PAM_Matrix)
    loc = start_point_Glob(result1)
    res, identity, seq1, seq2 =matrix_path_global(AA_1,AA_2,result1, loc[0],loc[1])
    score = calculator_score(seq1, seq2, In_del, Ext, PAM_Matrix)

    return res, identity, score

'''
sample_1, identity, score=generate_bisequence_aligned_calulate_score_of_prof('MACWSQLRLLLWKNLTFRRRQTCQLLLEVAWPLFIFLILISVRLSYPPYEQHECHFPNKAMPSAGTLPWVQGIICNANNPCFRYPTPGEAPGVVGNFNKSIV','MAFWTQLGLLLWKNFTYRRRQTFQLLIEVAWPLFIFFILISVRLSYPPYEQHECHFPNKAMPSAGTLPWIQGIICNANNPCFRYPTPGESPGIVGNFNASIV',8,1, PAM_Matrix)
print(sample_1,identity,score)
'''
'''
sample_1, identity, score=generate_bisequence_aligned_calulate_score_of_prof('MSAATSKYR','MSAATSMMKYR',7,2,PAM_Matrix)
print(sample_1,identity,score)
'''