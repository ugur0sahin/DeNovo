import numpy as np

def import_PAM_Matrix():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    PAM_Table = filedialog.askopenfilename()

    f=open(PAM_Table,'r')
    file=f.readlines()
    PAM_list=[]
    for i in file:
        line1=i.rstrip('\n')
        line=line1.split(';')
        PAM_list.append(line)
    return PAM_list

def insert_Gap_score(PAM_list):
    PAM_Matrix=np.matrix(PAM_list)
    Gap_Inserted_lst =['Gap']
    for i in range(19):
        interest=PAM_Matrix[i,0]
        summation=0
        for t in range(20):
            search=PAM_Matrix[t, 0]
            if  search!= interest:
                summation += find_PAM_Value(interest,search,PAM_list)
        Gap_Inserted_lst.append(str(summation/19))
    summation=0

    for iterator_for_diagonel in range(1,len(PAM_Matrix)-1):
        A=PAM_Matrix[iterator_for_diagonel-1,iterator_for_diagonel]
        summation += int(A)
    end = summation/20
    Gap_Inserted_lst.append(str(end))

    New_Matrix=[]
    for iterator in range(21):
        if iterator == 20:
            New_Matrix.append(Gap_Inserted_lst)
            A=PAM_list[iterator]
            A.append('Gap')
            New_Matrix.append(A)
        else:
            New_Matrix.append(PAM_list[iterator])
    return New_Matrix
def find_PAM_Value(Id1,Id2,PAM_Matrix):
    found=0
    for i in range(len(PAM_Matrix)):
        for j in range(len(PAM_Matrix[i])):
            #print(PAM_Matrix[-1][i], PAM_Matrix[j][0])
            if PAM_Matrix[-1][j]==Id1 and PAM_Matrix[i][0]==Id2:
                #print(PAM_Matrix[-1][j],PAM_Matrix[i][0] )
                if not PAM_Matrix[i][j] =='0':
                    found=float(PAM_Matrix[i][j])
                elif not PAM_Matrix[j-1][i+1] == '0':
                    found=float(PAM_Matrix[j-1][i+1])
                else:
                    found = 0
                break
        if found != 0:
            break
    return found
def compare_in_BLOSUM_or_PAM(Id1,Id2,PAM_Matrix):
    found = 0
    for i in range(len(PAM_Matrix)):
        for j in range(len(PAM_Matrix[i])):
            if PAM_Matrix[-1][j] == Id1 and PAM_Matrix[i][0] == Id2:
                if not PAM_Matrix[i][j] == '0':
                    found = float(PAM_Matrix[i][j])
                elif not PAM_Matrix[j - 1][i + 1] == '0':
                    found = float(PAM_Matrix[j - 1][i + 1])
                else:
                    found = 0
                break
        if found != 0:
            break
    return found
def generate_GAP_inserted_PAM_BLOSUM():
    PAM_list = import_PAM_Matrix()
    inserted_GAP=insert_Gap_score(PAM_list)
    return inserted_GAP

class Domain:
    def __init__(self,element_lst, similarity_score, valuable_lst, profile_matrix):
        self.element_lst=element_lst
        self.similarity_score=similarity_score
        self.valuable_lst=valuable_lst
        self.ProfMAT=profile_matrix

    def get_skeleton(self,PAM_BLOSUM_GAP_Inserted):
        indexing_colon=self.element_lst
        prof_MAT=self.ProfMAT
        sorted_indexing_colons=sorted(indexing_colon)
        start, end = sorted_indexing_colons[0],sorted_indexing_colons[-1]
        show_lst=[]
        for iterator in range(start,end):

            '''
            in profile start to end get colons
            choose precise AA residue to determine 
            if there is no minus PAM score between any combination in colon profile this
            is a resident domain AA residue
            
            else case -> it is not resident will be called as X
            '''

            cp=True
            interest_colon=prof_MAT[::,iterator]
            for i in range(len(interest_colon)):
                for j in range(len(interest_colon)):
                    if i<j:
                        point_ret=compare_in_BLOSUM_or_PAM(interest_colon[i], interest_colon[j], PAM_BLOSUM_GAP_Inserted)
                        if point_ret < -1:
                            cp=False
            if cp:
                lst_resident=[]
                for u in interest_colon:
                    if not u in lst_resident:
                        lst_resident.append(u)
                if len(lst_resident)==1:
                    show_lst.append(lst_resident[0])
                else:
                    txt=''
                    for i in lst_resident:
                        txt += '/' + str(i)
                    show_lst.append(txt)
            if not cp:
                show_lst.append('X')


        txt = ''
        for i in show_lst:
            txt += str(i)


        return txt


class Profile:
    def __init__(self,prfile_matrix,group_name="None"):
        self.profile_matrix=np.matrix(prfile_matrix)
        self.profile_name=group_name
    def raw_entropy(self):
        row,colon=np.shape(self.profile_matrix)
        raw_entropy_of_row=[]
        for iterator in range(row):
            interest_colon=self.profile_matrix[iterator,::]
            same_lst=[]
            for element in interest_colon:
                if not element in same_lst:
                    same_lst.append(element)
            raw_entropy_of_colon=1/len(same_lst)
            raw_entropy_of_row.append(raw_entropy_of_colon)
        raw_entropy_row=np.array(raw_entropy_of_row)
        return raw_entropy_row

    def sum_of_pairs(self):
        PAM_BLOSUM_GAP_Inserted = generate_GAP_inserted_PAM_BLOSUM()
        self.used_PAM=PAM_BLOSUM_GAP_Inserted
        row, colon = np.shape(self.profile_matrix)
        prof_mat=self.profile_matrix
        zero_MAT_for_sum_of_p_end=np.zeros([1,colon])
        for i in range(row):
            for j in range(row):
                if i < j:
                    sequence_first=prof_mat[i,::]
                    sequence_second=prof_mat[j,::]
                    for AAres in range(colon):
                        colon_point_for_a_comb=compare_in_BLOSUM_or_PAM(sequence_first[0,AAres], sequence_second[0,AAres], PAM_BLOSUM_GAP_Inserted)
                        zero_MAT_for_sum_of_p_end[0,AAres] += colon_point_for_a_comb
        return zero_MAT_for_sum_of_p_end


    def domain_pattern_recognizer(self, lower_seq_lim, upper_seq_lim):
        #raw_entropy_row=self.raw_entropy()
        raw_entropy_row=self.sum_of_pairs()
        prof_mat_all=self.profile_matrix
        raw_entropy_row=raw_entropy_row.tolist()
        raw_entropy=raw_entropy_row[0]
        denotes=range(len(raw_entropy))
        from itertools import combinations
        output = sum([list(map(list, combinations(denotes, i))) for i in range(len(raw_entropy) + 1)], []) #generation of all combinations
        possible_domain_lst_w_info, simscore_rank_ls = [], []
        for element_lst in output:
            try:
                length_of_domain=element_lst[-1] - element_lst[0]
            except:
                continue
            if length_of_domain < upper_seq_lim and length_of_domain > lower_seq_lim:

                valuable_lst=[]
                for iterator_i in element_lst:
                    lst_converted_sc=raw_entropy[iterator_i]
                    valuable_lst.append(lst_converted_sc)

                similarity_score = sum(valuable_lst) / len(valuable_lst) #rawentropy this will change with entropy
                if similarity_score > 0:
                    simscore_rank_ls.append(similarity_score)
                    possible_domain_lst_w_info.append(Domain(element_lst, similarity_score, valuable_lst, prof_mat_all))

        number_show_skeleton = int(input('How many highest hit domain will show: '))
        simscore_rank_ls=sorted(simscore_rank_ls); simscore_rank_ls=simscore_rank_ls[:number_show_skeleton-1] #sort and choose how many highest element will be proceed
        possible_domains=[]
        for domain in possible_domain_lst_w_info:
            if domain.similarity_score in simscore_rank_ls:
                domain_ske=domain.get_skeleton(self.used_PAM) #sketchskeleton of highest pair domains
                possible_domains.append(domain_ske)
        return possible_domains


    def __str__(self):
        return (self.profile_name)

