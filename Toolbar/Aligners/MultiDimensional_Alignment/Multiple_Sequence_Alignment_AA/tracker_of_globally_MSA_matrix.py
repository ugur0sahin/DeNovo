from Toolbar.Aligners.MultiDimensional_Alignment.Multiple_Sequence_Alignment_AA.generator_globAlMatrix_needleman_wunch import globAlignment_for_profiles
from Toolbar.Aligners.MultiDimensional_Alignment.Multiple_Sequence_Alignment_AA.generator_profile import *

def track_Global_Matrix(Global_Matrix, Profile1, Profile2):
    #print(Profile1)
    #print('\n')
    #print(Profile2)
    checkpoint = False
    row_ln, colon_ln =Global_Matrix.shape
    lst_coordinates_ref=[row_ln-1, colon_ln-1]
    counter_locate1, counter_locate2 = 0, 0
    prof1_zero, prof2_zero = range(0,21),range(0,21)
    prof1_image, prof2_image=[],[]
    for i in range(Profile1[1]):
        prof1_image.append('-')
    for i in range(Profile2[1]):
        prof2_image.append('-')
    prof1_zero, prof2_zero=np.matrix(prof1_zero, dtype=float), np.matrix(prof2_zero, dtype=float)
    prof1_zero, prof2_zero = prof1_zero.transpose(), prof2_zero.transpose()
    prof1_image, prof2_image = np.matrix(prof1_image), np.matrix(prof2_image)
    prof1_image, prof2_image = prof1_image.transpose(), prof2_image.transpose()

    while lst_coordinates_ref[0] !=0 and lst_coordinates_ref[1]!=0:
        gap_clmn= np.zeros([1, 21])
        gap_clmn[0, 20] = 1
        try:
            if not checkpoint:
                locations_to_move=[Global_Matrix[lst_coordinates_ref[0]-1, lst_coordinates_ref[1]-1] ,
                                   Global_Matrix[lst_coordinates_ref[0], lst_coordinates_ref[1]-1] ,
                                   Global_Matrix[lst_coordinates_ref[0]-1, lst_coordinates_ref[1]] ]
                max_Val = max(locations_to_move)
                locate_T = locations_to_move.index(max_Val)

                if locate_T == 1:
                    prof1_zero=np.insert(prof1_zero,0,gap_clmn,axis=1 )
                    rtc=np.transpose((Profile2[0][::,lst_coordinates_ref[0]-1]))
                    prof2_zero = np.insert(prof2_zero, 0, rtc, axis=1)


                    image_el=np.transpose(Profile1[-1][::,lst_coordinates_ref[1]-1])
                    prof1_image = np.insert(prof1_image, 0, image_el, axis=1)
                    prof2_image=np.insert(prof2_image,0,'-',axis=1)

                    lst_coordinates_ref = [lst_coordinates_ref[0], lst_coordinates_ref[1] - 1]

                elif locate_T == 2:
                    prof2_zero = np.insert(prof2_zero, 0, gap_clmn, axis=1)
                    rtc = np.transpose(Profile1[0][::,lst_coordinates_ref[1]-1])
                    prof1_zero = np.insert(prof1_zero, 0,rtc, axis=1)

                    image_el =np.transpose(Profile2[-1][::,lst_coordinates_ref[0]-1])
                    prof2_image = np.insert(prof2_image,0,image_el,axis=1)
                    prof1_image = np.insert(prof1_image,0,'-',axis=1)


                    lst_coordinates_ref = [lst_coordinates_ref[0]-1, lst_coordinates_ref[1]]

                else:
                    rtc = np.transpose(Profile2[0][::, lst_coordinates_ref[0]-1])
                    rtc1= np.transpose(Profile1[0][::,lst_coordinates_ref[1]-1])
                    prof1_zero=np.insert(prof1_zero,0,rtc1,axis=1 )
                    prof2_zero= np.insert(prof2_zero,0,rtc,axis=1)

                    image_el1 =np.transpose(Profile1[-1][::,lst_coordinates_ref[1]-1])
                    image_el2 = np.transpose(Profile2[-1][::, lst_coordinates_ref[0] - 1])
                    prof1_image = np.insert(prof1_image,0,image_el1,axis=1)
                    prof2_image = np.insert(prof2_image, 0, image_el2, axis=1)



                    lst_coordinates_ref = [lst_coordinates_ref[0]-1 , lst_coordinates_ref[1]-1]
            else:
                if lst_coordinates_ref[1]==0:
                    lst_coordinates_ref = [lst_coordinates_ref[0] - 1, lst_coordinates_ref[1]]
                    Profile2[2] = np.insert(Profile2[2], lst_coordinates_ref[0] + 1 + counter_locate1, '-', axis=1)
                    Profile2[0] = np.insert(Profile2[0], lst_coordinates_ref[0] + 1 + counter_locate1, gap_clmn, axis=1)
                    counter_locate1 += 1
                elif lst_coordinates_ref[0]==0:
                    lst_coordinates_ref = [lst_coordinates_ref[0], lst_coordinates_ref[1] - 1]
                    Profile1[2] = np.insert(Profile1[2], lst_coordinates_ref[1] + 1 + counter_locate2, '-', axis=1)
                    Profile1[0] = np.insert(Profile1[0], lst_coordinates_ref[1] + 1 + counter_locate2, gap_clmn, axis=1)
                    counter_locate2 += 1

        except:
            print('EXCEPTION WILL COMPLETE')
            checkpoint=True

    Profile1 = [prof1_zero[::,:-1],prof1_image[::,:-1], Profile1[-2]]
    Profile2 = [prof2_zero[::,:-1],prof2_image[::,:-1], Profile2[-2]]

    return Profile1, Profile2

def globAlignEndProt(Profile1,Profile2,Indel=7):
    GlobalMAT=globAlignment_for_profiles(Profile1,Profile2,Indel)
    ways=track_Global_Matrix(GlobalMAT,Profile1,Profile2)
    return ways

if __name__ == '__main__':
    sequences_prof1 = ['AAAAAAAAAAAAAAAAAAAAAAAAAAAAAMSTSYMKYR','AAAAAAAAAAAAAAAAAAAAAAAAAAQSAMSTSYMKYR']
    sequences_prof2 = ['MSTSYMKYR','MSTSYMKYR']
    Prof1 = converter_MS_image_to_profile(converter_MS_sequences_to_image(sequences_prof1))
    Prof2 = converter_MS_image_to_profile(converter_MS_sequences_to_image(sequences_prof2))

    #Prof1.append(generate_random_image(25,5));Prof2.append(generate_random_image(35,7))
    #print(Prof1, Prof2)          #Output of every profile is one matrix and presence of how many sequence in the profile
    ways=globAlignEndProt(Prof1,Prof2,7)     #output of glbMSA is a Matrix which is globally aligned of two profiles
    print(ways[0][-2],ways[1][-2])
    #print(Prof1)
    #print('\n')
    #print(Prof2)
    #Move=track_Global_Matrix(GloballMatrix,Prof1,Prof2)
    #print(Move[0][1])
    #print('\n')
    #print(Move[1][1])
    #print('\n')
    #print(Move[0][0])
    #print(Move[1][0])

'''
N=sequence_to_profile(['M-AATSKYR'])
print(N[1])
'''



'''
sequences_prof1 = ['M-AATSKYR','QSAA-SKYR']
sequences_prof2 = ['MATSMKYR','MATSM--R']
Prof1 = converter_MS_image_to_profile(converter_MS_sequences_to_image(sequences_prof1))
Prof2 = converter_MS_image_to_profile(converter_MS_sequences_to_image(sequences_prof2))

#A=globAlignEndProt(Prof1,Prof2)
#print(A[0][-2])
#print(A[1][-2])
'''