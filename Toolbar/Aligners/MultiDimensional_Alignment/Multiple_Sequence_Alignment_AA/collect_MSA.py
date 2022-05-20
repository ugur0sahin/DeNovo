from Toolbar.Aligners.MultiDimensional_Alignment.Multiple_Sequence_Alignment_AA.tracker_of_globally_MSA_matrix import *
from Toolbar.Aligners.MultiDimensional_Alignment.Multiple_Sequence_Alignment_AA.generator_globAlMatrix_needleman_wunch import *
from Toolbar.Aligners.MultiDimensional_Alignment.Multiple_Sequence_Alignment_AA.converter_biprofile_to_profile import *
class Profile:
    def __init__(self, prof_mat, number_seq, AAseq, name,prof1=None,prof2=None):
        self.prof_mat = prof_mat
        self.number = number_seq
        self.name = name
        self.AAseq=AAseq
        self.include_elements=prof1,prof2

    def __str__(self):
        return str(self.name)

'''
if __name__ == '__main__':
    db = [['MQSRTDARHDFLAQRTH', 1, 'cytochromeCX5'],
          ['SRTDARHDFLQ', 1, 'cytochromeCX4'],
          ['MQSRTDARHTH', 1, 'cytochromeCX3'],
          ['MQSRTDRRHDMLAQRTH', 1, 'cytochromeCX2'],
          ['LQSRTDRHM', 1, 'cytochromeCX1']]
    profiled_db=[]
    for i in db:
        N=sequence_to_profile([i[0]])
        N.append(i[-1])
        profiled_db.append(N)

    direction=[('cytochromeCX5','cytochromeCX2','J'),('cytochromeCX3','cytochromeCX4','T'),('T','J','E'),('cytochromeCX1','E','M')]
    prof_lst=[]
    #Fulfill list w/ object profiles non-aligned
    for i in range(len(db)):
        A=Profile(profiled_db[i][0],profiled_db[i][1],profiled_db[i][2],profiled_db[i][3])
        prof_lst.append(A)

    for commands in direction:
        search_object1,search_object2,new_profile_name=commands[0],commands[1],commands[2]
        #print(search_object1,search_object2,new_profile_name)

        for i in prof_lst:
            if search_object1==i.name:
                interest_object1=i
            if search_object2==i.name:
                interest_object2=i
        new_images_of_late_prof_w_MAT=globAlignEndProt([interest_object1.prof_mat,interest_object1.number, interest_object1.AAseq],
        [interest_object2.prof_mat, interest_object2.number, interest_object2.AAseq],4)

        new_profile_A=new_images_of_late_prof_w_MAT[0]
        new_profile_B=new_images_of_late_prof_w_MAT[1]

        #print('\n\n\n\n')
        #print(new_profile_A[0])
        #print('\n\n\n\n')
        #print(new_profile_B[1])
        PROFA=Profile(new_profile_A[0],new_profile_A[2],new_profile_A[1],interest_object1)
        PROFB=Profile(new_profile_B[0],new_profile_B[2],new_profile_B[1],interest_object2)


        #NEW_PROFILE_Info=biprofile_to_profile([PROFA.prof_mat,PROFA.AAseq,PROFA.number],[PROFB.prof_mat,PROFB.AAseq,PROFB.number])
        NEW_PROFILE_Info=biprofile_to_profile(PROFA,PROFB)
        NEW_PROFILE=Profile(NEW_PROFILE_Info[0],NEW_PROFILE_Info[1],NEW_PROFILE_Info[2],new_profile_name,prof1=interest_object1,prof2=interest_object2)
        print('HEY')
        print('\n')
        print(NEW_PROFILE.AAseq)

        prof_lst.append(NEW_PROFILE)
'''
def End_MultipleSequenceGenerator(chosen_db,directions):
    #db = [['MQSRTDARHDFLAQRTH', 1, 'cytochromeCX5'],
    #      ['SRTDARHDFLQ', 1, 'cytochromeCX4'],
    #      ['MQSRTDARHTH', 1, 'cytochromeCX3'],
    #      ['MQSRTDRRHDMLAQRTH', 1, 'cytochromeCX2'],
    #      ['LQSRTDRHM', 1, 'cytochromeCX1']]
    db,profiled_db=[],[]

    for item in chosen_db:
        db.append([item[0].AAseq, 1 ,item[0].geneID])

    for i in db:
        N=sequence_to_profile([i[0]])
        N.append(i[-1])
        profiled_db.append(N)

    #direction=[('cytochromeCX5','cytochromeCX2','J'),('cytochromeCX3','cytochromeCX4','T'),('T','J','E'),('cytochromeCX1','E','M')]
    prof_lst=[]
    #Fulfill list w/ object profiles non-aligned
    for i in range(len(db)):
        A=Profile(profiled_db[i][0],profiled_db[i][1],profiled_db[i][2],profiled_db[i][3])
        prof_lst.append(A)

    for commands in directions:
        search_object1,search_object2,new_profile_name=commands[0],commands[1],commands[2]
        #print(search_object1,search_object2,new_profile_name)

        for i in prof_lst:
            if search_object1==i.name:
                interest_object1=i
            if search_object2==i.name:
                interest_object2=i

        new_images_of_late_prof_w_MAT=globAlignEndProt([interest_object1.prof_mat,interest_object1.number, interest_object1.AAseq],
        [interest_object2.prof_mat, interest_object2.number, interest_object2.AAseq],4)

        new_profile_A=new_images_of_late_prof_w_MAT[0]
        new_profile_B=new_images_of_late_prof_w_MAT[1]

        #print('\n\n\n\n')
        #print(new_profile_A[0])
        #print('\n\n\n\n')
        #print(new_profile_B[1])
        PROFA=Profile(new_profile_A[0],new_profile_A[2],new_profile_A[1],interest_object1)
        PROFB=Profile(new_profile_B[0],new_profile_B[2],new_profile_B[1],interest_object2)


        #NEW_PROFILE_Info=biprofile_to_profile([PROFA.prof_mat,PROFA.AAseq,PROFA.number],[PROFB.prof_mat,PROFB.AAseq,PROFB.number])
        NEW_PROFILE_Info=biprofile_to_profile(PROFA,PROFB)
        NEW_PROFILE=Profile(NEW_PROFILE_Info[0],NEW_PROFILE_Info[1],NEW_PROFILE_Info[2],new_profile_name,prof1=interest_object1,prof2=interest_object2)
        #print('HEY')
        print('\n')
        print(NEW_PROFILE.AAseq)

        prof_lst.append(NEW_PROFILE)

