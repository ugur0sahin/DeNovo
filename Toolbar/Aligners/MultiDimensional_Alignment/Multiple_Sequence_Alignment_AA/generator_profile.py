from Toolbar.Aligners.MultiDimensional_Alignment.Multiple_Sequence_Alignment_AA.calculator_across_diagonel_point import *
'''
# This function generate float include random profile
def generate_random_profile(length_of_profile, number_of_seq_in_profile):  # Generate random profile to compare
    Zero_Matrix=np.zeros([21,length_of_profile])
    unit=1/number_of_seq_in_profile
    for j in range(length_of_profile):
        choose_row=rnd.randint(0,20)
        for i in range(number_of_seq_in_profile):
            Zero_Matrix[choose_row,j]+=unit
            pos=rnd.randint(0,10)
            if pos==3 or pos==4:
                choose_row=20
            elif pos >= 8:
                choose_row=rnd.randint(0,20)
    new_Mat=Zero_Matrix
    return [Zero_Matrix,number_of_seq_in_profile]

#This is the function which only generate '-' image profile
def generate_random_image(length_of_profile, number_of_seq_in_profile):
    lst=[]
    for i in range(number_of_seq_in_profile):
        row=[]
        for j in range(length_of_profile):
            row.append('-')
        lst.append(row)
    return np.matrix(lst)
'''

#This is the function which get sequence to generate image profile
def converter_MS_sequences_to_image(sequences):
    lst=[]
    for i in range(len(sequences)):
        row=list(sequences[i])
        lst.append(row)
    lst = np.matrix(lst)
    return lst


# This is the function that convert MS include image to profile
def converter_MS_image_to_profile(image):
    rw_len_im, col_len_im =image.shape
    zero_Mat = np.zeros([21, col_len_im])
    unit = 1/rw_len_im
    AA_Val=get_PAM_elements()
    rwAA, clAA = AA_Val.shape
    for i in range(col_len_im):
        colon_of_im=image[::,i]
        for j in colon_of_im:
            for iterator_of_PAM_component in range(clAA):
                if [[AA_Val[0,iterator_of_PAM_component]]] == j[0]:
                    zero_Mat[iterator_of_PAM_component,i]+=unit
    return [zero_Mat,rw_len_im,image]

def sequence_to_profile(sequence_lst):
    image=converter_MS_sequences_to_image(sequence_lst)
    profile=converter_MS_image_to_profile(image)
    return profile



'''
rs= converter_MS_sequences_to_image(['MQSTRACTD'])
print(rs)
print(converter_MS_image_to_profile(rs))
'''