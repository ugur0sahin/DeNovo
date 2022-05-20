import Toolbar.Build_Tree_Tools.Distance_Tree.Least_Square_Min_Evolution_Tree.Min_Least_Tree_BaseFormation as MinEvoLeastSq


def least_square_tree(tree_data, DistMat):
    all_sum_errors=[]
    all_positive_trees=[]
    least_square_trees_return=[]
    for tree in tree_data:
        branch_lengths=tree[1]
        least_square_sum = 0
        if MinEvoLeastSq.check_negative(branch_lengths):
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
                    length_of_path_name=MinEvoLeastSq.find_length_of_name(path,branch_lengths)
                    total_length_of_node += length_of_path_name
                #print((total_length_of_node-Distance_of_Interest)**2)
                least_square_sum += (total_length_of_node-Distance_of_Interest)**2
            #print(least_square_sum)
            all_sum_errors.append(least_square_sum)
            all_positive_trees.append(tree)
    sum_locations=MinEvoLeastSq.find_min_index(all_sum_errors)
    for location in sum_locations:
        append_tree_for_least_square=all_positive_trees[location]
        append_tree_for_least_square=list(append_tree_for_least_square)
        append_tree_for_least_square.append(min(all_sum_errors))
        append_tree_for_least_square=tuple(append_tree_for_least_square)
        least_square_trees_return.append(append_tree_for_least_square)

    return least_square_trees_return



'''
DistMat=[['x','HSap','PPan','Rattus','Gallus'],

         ['HSap'  ,1,2,9,8],
         ['PPan'  ,2,1,9,8],
         ['Rattus',8,9,1,5],
         ['Gallus',8,8,5,1]]
         #['Tyy'    ,3,4,5,7,1]]

will_fit_name_list=DistMat[0][1:]
combined_list_w_names=MinEvoLeastSq.GenPath.generate_all_combinations_of_tree(will_fit_name_list) #Get combined list from generate_path_edit
result=MinEvoLeastSq.collect_tree(DistMat) #Minimum_Evolution
result1=least_square_tree(result,DistMat)
for i in result1:
    print(i)
'''