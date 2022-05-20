import numpy as np

from Toolbar.Aligners.MultiDimensional_Alignment.Multiple_Sequence_Alignment_AA.generator_profile import *
'''
def import_PAM_Matrix(PAM_Table):
    f=open(PAM_Table,'r')
    file=f.readlines()
    PAM_list=[]
    for i in file:
        line1=i.rstrip('\n')
        line=line1.split(';')
        PAM_list.append(line)
    return PAM_list
def sequence_to_profile(sequence):
    one_seq_profile=np.zeros([21,len(sequence)])
    PAM_tble = import_PAM_Matrix('/Users/ugurs.ahin/Desktop/DeNoVo/Toolbar/Aligners/Protein_Alignment/PAM_table.csv')
    for i in range(len(sequence)):
        zero_col=np.zeros([21,1])
        cp=True
        for ite1 in range(len(PAM_tble[0])):
            if PAM_tble[ite1][0]==sequence[i]:
                zero_col[ite1,::]=1
                cp=False
                break
        one_seq_profile[::,i]=zero_col[::,0]

        if cp:
            one_seq_profile[20,i]=1

    return one_seq_profile
'''
'''
def biprofile_to_profile(profileA,profileB):
    if len(profileA[0]) != len(profileB[0]):
        print("lengths of profiles are not equal!")
    else:
        #Image = np.concatenate((profileA[-1], profileB[-1]),axis=0)
        #Image = np.append(profileA,profileB)
        print(profileA[-1])
        print(profileB[-1])
        New_Prof=np.zeros([21, len(profileB[0][0])])
        for i in range(len(profileA[0][0])):
            col_of_prof1, col_of_prof2 = profileA[0][::,i], profileB[0][::,i]
            int_col_profA, int_col_profB = [],[]
            for flt1 in col_of_prof1:
                int_val_col_1 = flt1*profileA[1]
                int_col_profA.append(int_val_col_1)
            for flt2 in col_of_prof2:
                int_val_col_2 =flt2*profileB[1]
                int_col_profB.append(int_val_col_2)

            averaged_col=[]
            for sum_iterator in range(len(int_col_profA)):
                averaged_col.append((int_col_profA[sum_iterator] + int_col_profB[sum_iterator])/(profileA[1]+profileB[1]))
            New_Prof[::,i]=averaged_col
    #New_Prof = New_Prof

    return New_Prof
'''
def append_image(image1,image2):
    n_matrix=[]
    for i in image1:
        row_lst=[]
        for j in i:
            row_lst.append(j)
        n_matrix.append(row_lst)
    for i in image2:
        row_lst=[]
        for j in i:
            row_lst.append(j)
        n_matrix.append(row_lst)
    n_matrix=np.matrix(n_matrix)
    return n_matrix

def biprofile_to_profile(profileA,profileB):
    samp1_prof=profileA.prof_mat*(profileA.number/(profileA.number+profileB.number))
    samp2_prof=profileB.prof_mat*(profileB.number/(profileA.number+profileB.number))
    print(samp1_prof)
    print(samp2_prof)

    new_prof_mat=samp1_prof + samp2_prof
    total_number_of_new_prof = profileA.number + profileB.number

    Image = np.concatenate((profileA.AAseq, profileB.AAseq),axis=0)
    #Image = np.append(profileA.AAseq,profileB.AAseq)
    #Image=0
    #Image=append_image(profileA.AAseq,profileB.AAseq)


    return [new_prof_mat,total_number_of_new_prof,Image]





