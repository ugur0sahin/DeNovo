from Toolbar.Aligners.MultiDimensional_Alignment.MSA_Rec.globAlignment_for_Profiles import globAlignment as glbMSA
from Toolbar.Aligners.MultiDimensional_Alignment.MSA_Rec.generate_profile_random import generate_random_profile
import numpy as np



def track_Global_Matrix(Global_Matrix, Profile1, Profile2):
    checkpoint = False
    row_ln, colon_ln =Global_Matrix.shape
    lst_coordinates_ref=[row_ln-1, colon_ln-1]

    while not (lst_coordinates_ref[0] ==0 and lst_coordinates_ref[1]==0):
        try:
            if checkpoint==False:
                locations_to_move=[Global_Matrix[lst_coordinates_ref[0]-1, lst_coordinates_ref[1]-1] ,
                                   Global_Matrix[lst_coordinates_ref[0], lst_coordinates_ref[1]-1] ,
                                   Global_Matrix[lst_coordinates_ref[0]-1, lst_coordinates_ref[1]] ]
                max_Val = max(locations_to_move)
                locate_T = locations_to_move.index(max_Val)

                if locate_T==1:
                    lst_coordinates_ref=[lst_coordinates_ref[0], lst_coordinates_ref[1]-1]
                    np.insert(Profile1[0])
                elif locate_T == 2:
                    lst_coordinates_ref = [lst_coordinates_ref[0]-1, lst_coordinates_ref[1]]
                else:
                    lst_coordinates_ref = [lst_coordinates_ref[0]-1 , lst_coordinates_ref[1]-1]
            else:
                if lst_coordinates_ref[1]==0:
                    print('1')
                elif lst_coordinates_ref[0]==0:
                    print('0')

        except:
            checkpoint=True
            print('DGHRSAGRDE')







'''
if __name__ == '__main__':
    Prof1, Prof2 =generate_random_profile(25,5), generate_random_profile(35,7)
    print(glbMSA(Prof1,Prof2,4)) #output of glbMSA is a Matrix which is globally aligned of two profiles
    #print(Prof1[0], Prof2)          #Output of every profile is one matrix and presence of how many sequence in the profile
    GloballMatrix=glbMSA(Prof1,Prof2,4)
    Move=track_Global_Matrix(GloballMatrix,'','')
'''