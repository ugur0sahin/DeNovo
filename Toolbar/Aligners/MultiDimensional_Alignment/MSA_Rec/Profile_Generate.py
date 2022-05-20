import numpy as np
from Toolbar.Aligners.MultiDimensional_Alignment.MSA_Rec.generate_profile_random import *

def import_PAM_Matrix(PAM_Table):
    f=open(PAM_Table,'r')
    file=f.readlines()
    PAM_list=[]
    for i in file:
        line1=i.rstrip('\n')
        line=line1.split(';')
        PAM_list.append(line)
    return PAM_list

def profile_profile_toGen_new_profile(profileA,profileB): #profile A denote their profile matrix and length
    if len(profileA[0]) != len(profileB[0]):
        print("lengths of profiles are not equal!")
    else:
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

def sequence_to_profile(sequence):   #It get a sequence to generate profile
    one_seq_profile=np.zeros([21,len(sequence)])
    PAM_tble = import_PAM_Matrix('/Users/ugurs.ahin/Desktop/DeNoVo/Toolbar/Aligners/PAM_and_BLOSOM_Matrices/PAM_table.csv')
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


if __name__ =='__main__':
    #ProfA, ProfB =generate_random_profile(30,2),generate_random_profile(30,2)
    #ProfA,ProfB=[ProfA,5], [ProfB, 5]
    #print(ProfA)
    #print(ProfB)
    #print(profile_profile_toGen_new_profile(ProfA,ProfB))
    a=sequence_to_profile('A-R-TG')
    b=sequence_to_profile('T-Q-MM')
    print(a)
    print('\n')
    print(b)
    print('\n')
    print(profile_profile_toGen_new_profile([a,2],[b,1]))




