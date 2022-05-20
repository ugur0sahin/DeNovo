import sympy as sp
#from sympy import rref
import numpy as np
#import Toolbar.Aligners.Protein_Alignment.multiple_alignment_scores as MSS
import Toolbar.Build_Tree_Tools.Distance_Tree.Least_Square_Min_Evolution_Tree.generator_all_combinedpaths_distMat_organism_for_build_tree as GenPath

def find_min_index(lst):
    min_element=min(lst)
    min_index=[]
    for i in range(len(lst)):
        if lst[i]==min_element:
            min_index.append(i)
    return min_index

def find_all_Path_IDs(sample_will_fit):
    list_path_ID=[]
    for i in sample_will_fit:
        for j in i:
            path_IDs_in_loc=j[1]
            for x in path_IDs_in_loc:
                if not x in list_path_ID:
                    list_path_ID.append(x)
    return list_path_ID

def adjust_for_Sympy_formation(list_path_ID):
    Sympy_Names=''
    for i in list_path_ID:
        Sympy_Names += i
        Sympy_Names +=' '
    return Sympy_Names

def find_it(unknown_name, list_Path_ID):
    index_it = list_Path_ID.index(unknown_name)
    return index_it

def find_length_of_name(path_name, branch_lengths):
    for path_name_in_tree in branch_lengths:
        if path_name_in_tree[0]==path_name:
            path_length_chosen=path_name_in_tree[1]
    return path_length_chosen

def adjust_optimal_lengths_and_assign(combined_list_w_names, DistMat):
    result=find_all_Path_IDs(combined_list_w_names)
    unknown_names=adjust_for_Sympy_formation(result)
    unknown_list = sp.symbols(unknown_names)

    all_Matrices=[]
    for combined_grops in combined_list_w_names:
        total_equation = 0
        for combined_elements in combined_grops:
            interest_name=combined_elements[0]
            interest_path_ID = combined_elements[1]

            for i in range(len(DistMat)):
                for j in range(len(DistMat[0])):
                    sum_unknown=0
                    if DistMat[i][0]==interest_name[0] and DistMat[0][j]==interest_name[1]:
                        interest_Dist=DistMat[i][j]
                        for iterator_of_unknown in interest_path_ID:
                             it=find_it(iterator_of_unknown, result)
                             sum_unknown += unknown_list[it]
                        equation = (interest_Dist - sum_unknown )**2
                        equation = sp.expand(equation)
                        total_equation += equation
        total_equation =sp.simplify(total_equation)
        total_equation_Matrix=[]
        for in_term in unknown_list:
            derived_in_term=sp.diff(total_equation,in_term)
            derived_in_term_Coefficient=sp.Poly(derived_in_term,unknown_list)
            derived_in_term_Coefficient=derived_in_term_Coefficient.coeffs()
            total_equation_Matrix.append(derived_in_term_Coefficient)
        #print(np.matrix(total_equation_Matrix))
        Matrix=sp.Matrix(total_equation_Matrix)
        a= sp.Matrix.rref(Matrix)
        Matrix=np.matrix(a[0])

        #print('\n\n')
        #print(total_equation)
        all_Matrices.append(Matrix)

    return all_Matrices, unknown_names, combined_list_w_names

def collect_tree(DistMat):
    will_fit_name_list = DistMat[0][1:]
    combined_list_w_names = GenPath.generate_all_combinations_of_tree(will_fit_name_list)
    matrices, unknowns, combinedlstnames = adjust_optimal_lengths_and_assign(combined_list_w_names, DistMat)

    grand_pathID_Length_lst=[]
    unknowns=unknowns.split(' ')
    unknowns=unknowns[:-1]

    for j in matrices:
        counter = -1
        pathID_Length_lst = []
        list_name_length=[]
        for i in unknowns:
            counter +=1
            pathID_Length_lst.append((i,float(-(j[counter,-1]))))
        grand_pathID_Length_lst.append(pathID_Length_lst)

    counter=-1
    tree_big_data=[]
    for n in grand_pathID_Length_lst:
        counter +=1
        sum = 0
        for i in n:
            sum += i[1]
        tree_big_data.append((sum,grand_pathID_Length_lst[counter],combined_list_w_names[counter]))
        #print(str(sum)+ '  ||   ' + str(grand_pathID_Length_lst[counter]) + '  ||   ' + str(combined_list_w_names[counter]))


    return tree_big_data

def check_negative(length_branch):
    cp=True
    for i in length_branch:
        if int(i[1])<0:
            cp=False
            break
    return cp

def least_square_tree(tree_data, DistMat):
    all_sum_errors=[]
    all_positive_trees=[]
    least_square_trees_return=[]
    for tree in tree_data:
        branch_lengths=tree[1]
        least_square_sum = 0
        if check_negative(branch_lengths):
            #print('\n\n\n')
            for paths_and_name in tree[2]:
                total_length_of_node=0
                two_organism_name=paths_and_name[0]
                for i in range(len(DistMat)):
                    for j in range(len(DistMat[0])):
                        if DistMat[i][0]==two_organism_name[0] and DistMat[0][j]==two_organism_name[1]:
                            Distance_of_Interest=DistMat[i][j]
                path_name_of_distance=paths_and_name[1]
                for path in path_name_of_distance:
                    length_of_path_name=find_length_of_name(path,branch_lengths)
                    total_length_of_node += length_of_path_name
                #print((total_length_of_node-Distance_of_Interest)**2)
                least_square_sum += (total_length_of_node-Distance_of_Interest)**2
            #print(least_square_sum)
            all_sum_errors.append(least_square_sum)
            all_positive_trees.append(tree)
    sum_locations=find_min_index(all_sum_errors)
    for location in sum_locations:
        append_tree_for_least_square=all_positive_trees[location]
        append_tree_for_least_square=list(append_tree_for_least_square)
        append_tree_for_least_square.append(min(all_sum_errors))
        append_tree_for_least_square=tuple(append_tree_for_least_square)
        least_square_trees_return.append(append_tree_for_least_square)

    return least_square_trees_return



#A=['HSap','PPan','Rattus','Gallus']
#will_fit_name_list=['HSap','PPan','Rattus','Gallus']
#DistMat=MSS.evo_dist(['MACWSQLRLLLWKNLTFRRRQTCQLLLEVAWPLFIFLILISVRLSYPPYEQHECHFPNKAMPSAGTLPWVQGIICNANNPCFRYPTPGEAPGVVGNFNKSIV', 'MACWPQLRLLLWKNLTFRRRQTCQLLLEVAWPLFIFLILISVRLSYPPYEQHECHFPNKAMPSAGTLPWVQGIICNANNPCFRYPTPGEAPGVVGNFNKSIV', 'MACWPQLRLLLWKNLTFRRRQTCQLLLEVAWPLFIFLILISVRLSYPPYEQHECHFPNKAMPSAGTLPWVQGIICNANNPCFRYPTPGEAPGGNFNKSIV', 'MAFWTQLGLLLWKNFTYRRRQTFQLLIEVAWPLFIFFILISVRLSYPPYEQHECHFPNKAMPSAGTLPWIQGIICNANNPCFRYPTPGESPGIVGNFNASIV'],A)

