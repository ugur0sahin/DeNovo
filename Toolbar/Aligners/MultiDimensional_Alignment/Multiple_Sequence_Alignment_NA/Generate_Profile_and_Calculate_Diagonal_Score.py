import numpy as np

def sequence_sequence_profile_generate(seq1,seq2): # gap '-' is acceptable
    zero_Matrix=np.zeros([5,len(seq2)])
    sequences=[seq1,seq2]
    for int_sequences in range(len(seq1)):
        A_Val, G_Val, T_Val, C_Val, GaP_Val = 0,0,0,0,0
        for seq in sequences:
            if seq[int_sequences]=='A':
                A_Val += 0.5
            elif seq[int_sequences]=='G':
                G_Val += 0.5
            elif seq[int_sequences]=='T':
                T_Val += 0.5
            elif seq[int_sequences]=='C':
                C_Val += 0.5
            else:
                GaP_Val += 0.5
        zero_Matrix[0,int_sequences], zero_Matrix[1,int_sequences], zero_Matrix[2, int_sequences], zero_Matrix[3,int_sequences],zero_Matrix[4,int_sequences]\
            =A_Val, G_Val, T_Val, C_Val, GaP_Val

    return zero_Matrix

def diagonal_point(row,colon,match_point, mismatch_point):
    np.matrix(row); np.matrix(colon)
    zero_Matrix=np.zeros([len(row),len(colon)])
    for i in range(len(row)):
        for j in range(len(colon)):
            coefficient=float(row[i])*float(colon[j])
            zero_Matrix[i,j]=coefficient
    sum_match, sum_mismatch =0,0
    for i in range(len(zero_Matrix)):
        for j in range(len(zero_Matrix[0])):
            if i==j:
                sum_match+=zero_Matrix[i,j]
            if i>j:
                sum_mismatch+=zero_Matrix[i,j]

    match_score=sum_match*match_point
    mismatch_match_score=sum_mismatch*(-mismatch_point)


    diagonal_score=match_score + mismatch_match_score
    return diagonal_score
'''
def main():
    row=[0, 0.25, 0.25, 0.5, 0]; colon=[0, 0.50, 0.5, 0, 0]
    diagonal_result=diagonal_point(row,colon,3,2)
    print(diagonal_result)

main()
'''