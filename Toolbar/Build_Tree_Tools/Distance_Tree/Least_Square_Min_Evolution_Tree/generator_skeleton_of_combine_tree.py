from itertools import permutations
import string
import random

#combination_set=list(combination_set)


def Specific_path_name(i):
    all_letters = string.ascii_letters
    N=int(i/26)
    return_code=''
    for i in range(N+2):
        random_choice=random.choice(all_letters)
        return_code += random_choice
    return return_code


def DeNovo_tree_formation(sample_N):
    sample_N=sample_N-1
    tree=[]
    for i in range(sample_N):
        if i<1:
            i_add=i+1
            Node_Info=(['X'+str(i), Specific_path_name(i)],['X'+str(i_add), Specific_path_name(i)], Specific_path_name(i))
            tree=(Node_Info)
        elif i==sample_N-1:
            Node_Info = (tree, ['X' + str(i+1), Specific_path_name(i)])
            tree=(Node_Info)

        else:
            Node_Info=(tree,['X'+ str(i+1), Specific_path_name(i)], Specific_path_name(i))
            tree=(Node_Info)
    print(tree)
    return tree



def all_odd_location(list):
    return_list=list[1:-1]
    return return_list
def store_Path(tree, Sample_N):
    counter=0
    recover_tree=tree
    all_prepared_path = []
    while True:
                counter += 1
                if counter==1:
                    recover_tree=recover_tree
                else:
                    recover_tree=recover_tree[0]
                tree=recover_tree
                try:
                    interest_element=tree[-1]
                    Name_of_interest_element=interest_element[0]
                    Id_path_interest_element=interest_element[-1]
                    check=Id_path_interest_element[1]
                except:
                    try:
                        interest_element=tree[-2]
                        Name_of_interest_element = interest_element[0]
                        Id_path_interest_element = interest_element[-1]
                    except:
                        break
                for i in range(Sample_N-counter+1):
                    name=[]; path=[]; prepared_path=[]
                    if isinstance(tree[0],tuple):
                        path.append(Id_path_interest_element)
                        name.append(Name_of_interest_element)
                        tree=tree[0]
                        element_will_add=(tree[1],tree[-1])
                        try:
                            if all_prepared_path[-1][0][0] == Name_of_interest_element:
                                last_path_list=all_odd_location(all_prepared_path[-1][-1])
                                for i in last_path_list:
                                    path.append(i)
                        except:
                            pass
                        path.append(element_will_add[1])
                        path.append(element_will_add[0][-1])
                        name.append(element_will_add[0][0])
                        prepared_path.append(name), prepared_path.append(path)
                        all_prepared_path.append(prepared_path)


                    else:
                        path.append(Id_path_interest_element)
                        name.append(Name_of_interest_element)
                        element_will_add=(tree[0][0],tree[0][1])
                        name.append(element_will_add[0])
                        last_path_list=all_odd_location(all_prepared_path[-1][-1])
                        for i in last_path_list:
                            path.append(i)
                        path.append(element_will_add[-1])
                        prepared_path.append(name), prepared_path.append(path)
                        if not prepared_path in all_prepared_path:
                            all_prepared_path.append(prepared_path)

    all_prepared_path[-1][-1]=[all_prepared_path[-1][-1][0], all_prepared_path[-1][-1][-1]]
    return all_prepared_path


def replacew_all_combinations(combination_set, All_Path):
    grand_list=[]
    for i in combination_set:
        short_list=[]
        #print('\n\n\n')
        for j in range(len(All_Path)):
            name_tap=All_Path[j][0]
            series=(int(name_tap[0][-1]), int(name_tap[1][-1]))
            will_append=[All_Path[j][0],All_Path[j][-1]]
            will_append[0]=[i[series[0]],i[series[1]]]
            short_list.append(will_append)
        grand_list.append(short_list)
        #for i in short_list:
        #    print(i)
    return grand_list



def generate_all_combinations_of_tree(Organism_Set):
    length_of_set=len(Organism_Set)
    combination_set = permutations(Organism_Set)
    result_tree=DeNovo_tree_formation(length_of_set)
    result_path=store_Path(result_tree,length_of_set-1)
    grand_list=replacew_all_combinations(combination_set,result_path)

    return grand_list



organisms=['a','b','c','d','e','f']

res=generate_all_combinations_of_tree(organisms)
