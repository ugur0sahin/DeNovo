import Toolbar.Build_Tree_Tools.Distance_Tree.Least_Square_Min_Evolution_Tree.Min_Least_Tree_BaseFormation as MinEvoLeastSq

def  minimum_evolution_tree(tree_data):
    min_tree_score=1000
    min_tree_lst=[]
    for i in tree_data:
        cp = True
        if i[0]<min_tree_score:
            for a in i[1]:
                if a[1]<0:
                    cp=False
            if cp:
                min_tree_lst = []
                min_tree_score=i[0]
                min_tree_lst.append(i)
        elif i[0]==min_tree_score:
            for a in i[1]:
                if a[1]<0:
                    cp=False
            if cp:
                min_tree_lst.append(i)

    return min_tree_lst

'''
DistMat=[['x','HSap','PPan','Rattus','Gallus','SusScrofa'],
         ['HSap'  ,1,2,9,8,3],
         ['PPan'  ,2,1,9,8,4],
         ['Rattus',8,9,1,5,5],
         ['Gallus',8,8,5,1,7],
         ['SusScrofa',3,4,5,7,1]]
#will_fit_name_list=DistMat[0][1:]
#combined_list_w_names=MinEvoLeastSq.GenPath.generate_all_combinations_of_tree(will_fit_name_list) #Get combined list from generate_path_edit
result=MinEvoLeastSq.collect_tree(DistMat) #Minimum_Evolution
result1=minimum_evolution_tree(result)
for i in result1:
    print(i)
'''