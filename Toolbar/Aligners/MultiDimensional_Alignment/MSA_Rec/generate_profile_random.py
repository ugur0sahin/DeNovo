import numpy as np
import random as rnd

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