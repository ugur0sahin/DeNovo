# this fuunction provides getting file service unlimited, it appends file_paths to list

def get_chromosome_ID(chromosome):
    split_lst=chromosome.split('/')
    name=split_lst[-1]
    name=name.replace('.txt','')
    return name

def get_file_parsel_elemnt():
    import tkinter as tk
    import readerbody as rb
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    lst = []
    while True:
        file_path = filedialog.askopenfilename()
        if file_path == '':
            break
        lst.append(file_path)

    imported_chromosomes_elements = []
    for file in lst:
        chID=get_chromosome_ID(file)
        all_elements = rb.generate_all_element_list(file)
        imported_chromosomes_elements.append([all_elements,chID])
    return imported_chromosomes_elements

def add_chromosomeID_to_obj(obj, chromsomeID):
    obj(chromsomeID=chromsomeID)

def interface_chromosome_FamilyChoose(chromosome,type,chromosome_ID):
    import NBody.found_NAME_toshow_clas as name
    aClass, add, int_el=[],'Y',0
    while True:
        if add=='Y':
            print('\n\n')
            print('from:: ' + str(chromosome_ID))
            Ind_OR_GeneID=input('||Specify your search method||')

            if Ind_OR_GeneID == 'Index':  # Index Block
                show_All=input('Show All? ')
                if show_All=='Y':
                    print('--------------All gene names presence in the chromosome--------------')
                    for i in chromosome:
                        if i.type == 'gene':
                            print(i)
                    print('\n\n')
                    print('--------------After this line element type you interest will be shown --------------')
                    print('\n\n')
                    for i in chromosome:
                        if i.type==type:
                            print(i)
                print('\n')
                print('---------------------------------------------------')
                print('\n')
                index_name = input('Input Index name of the searching element gene,CDS,mRNA etc...')
                print('\n')

                for iterator1 in chromosome:
                    try:
                        if iterator1.product == index_name:
                            found_geneFam = iterator1
                            #print(found_geneFam)
                    except:
                        if iterator1.name ==index_name:
                            found_geneFam = iterator1
                            #print(found_geneFam)

                geneID_searched_element=found_geneFam.geneID

                family_lst=[]
                for iterator1 in chromosome:
                    if iterator1.geneID==geneID_searched_element:
                        family_lst.append(iterator1)
                import NBody.generate_Class_for_elements as gClass
                obj = gClass.Family(family_lst, geneID_searched_element,chromosome_ID)
                aClass.append(obj)

            else:  # GeneID block
                print('\n')
                a=None
                show_All =input('Show All Gene Family or not? (Y/N)')
                if show_All == 'Y':
                    for i in chromosome:
                        if i.type=='CDS':
                            if a !=i.geneID:
                                print(i.geneID)
                            a=i.geneID
                print('\n')
                geneID_searched_element =input('What is the GeneID of Interest?:')
                print('\n')
                family_lst = []
                for iterator1 in chromosome:
                    if iterator1.geneID==geneID_searched_element:
                        family_lst.append(iterator1)
                if family_lst != []:
                    import NBody.generate_Class_for_elements as gClass
                    obj=gClass.Family(family_lst,geneID_searched_element,chromosome_ID)
                    aClass.append(obj)

            #################
            ## This part of the block only demonstrate features of chosen elements
            for index in range(int_el,len(aClass)):
                name.categorizer(aClass[index],type)
                int_el+=1
            #################
            add = input('will you add any element more? (Y/N)')
            print('\n')
        else:
            break
    return aClass

def get_path():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def choose_family_indatabase(lst,db):
    rtrn_lst=[]
    for i in lst:
        rtrn_lst.append(db[i])
    return rtrn_lst

def get_database_interface(typ):
    db = []
    chromosomes_elements = get_file_parsel_elemnt()
    for chromosome in chromosomes_elements:
        output_familis = interface_chromosome_FamilyChoose(chromosome[0], typ, chromosome[1])  # In there chromosomes that will be get family chosen
        # after chosen families which have different geneID collect in output families lst as database
        for i in output_familis:
            db.append(i)
    return db

def choose_from_db(typ,db):
    chosen_db=[]
    for i in range(len(db)):
        for i in range(len(db)):
            print('[' + str(i) + ']' + ' ' + str(db[i]) + ' || ' + db[i].chromosomeID)
        selected_family_index = int(input('choose family:'))
        family_in = db[selected_family_index].return_all_elements()

        for i in range(len(family_in)):
            print('[' + str(i) + ']' + ' ' + str(family_in[i]) + '|| ' + str(family_in[i].type))
        chosen_element_ind = int(input('choose element will interest:'))
        if family_in[chosen_element_ind].type == typ:
            chosen_db.append([family_in[chosen_element_ind], db[selected_family_index].chromosomeID])
        else:
            print('This is not a ' + str(typ) + ' !')
        cnt_add = input('continue to add:')
        if cnt_add == 'N':
            break
    return chosen_db


def generator_distance_matrix():
    db = get_database_interface('CDS')
    chosen_db = choose_from_db('CDS',db)
    import Toolbar.Build_Tree_Tools.Distance_Matrix.generator_distance_matrix as DMatrix

    ct, only_seq_array, only_name_array_samp, only_seq_array_proc = 0, [], [], []
    only_name_array_proc,only_name_array_proc1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'],['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
    names = []
    for i in chosen_db:
        ct += 1
        file_n = i[-1].replace('.flat', '')
        name = str(i[0].geneID)  # + ' || ' + str(file_n)
        names.append(str(i[0].product) + ' || ' + str(file_n) + ' || ' + str(i[0].geneID))
        only_seq_array.append(i[0].AAseq)
        only_name_array_samp.append(name)
    only_name_array_proc = only_name_array_proc[:ct]
    DistanceMatInterest = DMatrix.generate_distance_matrix(only_seq_array, only_name_array_proc, indel=7, extension=2)
    for i in range(len(DistanceMatInterest)):
        for j in range(len(DistanceMatInterest[0])):
            if not (i == 0 or j == 0):
                DistanceMatInterest[i][j] = DistanceMatInterest[i][j] * 100
    return DistanceMatInterest, only_name_array_proc1, only_name_array_samp, names, ct, chosen_db


if __name__ == '__main__':
    ans_process=input('Input process will occur Alignment/PhyloTree/ProTools: ')
    if ans_process=='Alignment':
        ans_type=input("Input sample's type (Protein/NucleicAcid): ")
        if ans_type=='Protein':
            ans_sample_space=input("ınput size of sample space (Multiple Sequence Alignment/Bisequencial Alignment): ")
            if ans_sample_space=='Multiple Sequence Alignment':

                #Generation of Distance Matrix Path
                DistanceMatInterest, only_name_array_proc1, only_name_array_samp, names, ct,chosen_db= generator_distance_matrix()
                print('---------------DISTANCE MATRIX-----------------')
                for i in DistanceMatInterest:
                    print(i)
                print('-----------------------------------------------')
                print(chosen_db)
                #Neighboor Joining Tree Directions Generation
                import Toolbar.Build_Tree_Tools.Distance_Tree.Neighboor_Joining_Tree.Neighboor_Joining_New as NJ

                print('--------------------NODES INFO---------------------')
                for i in range(len(DistanceMatInterest)):
                    for j in range((len(DistanceMatInterest[0]))):
                        if i == 0 and j != 0:
                            DistanceMatInterest[0][j] = only_name_array_samp[j - 1]
                        elif j == 0 and i != 0:
                            DistanceMatInterest[i][0] = only_name_array_samp[i - 1]
                #Naked pathway
                Pathway = NJ.Neighboor_Joining(DistanceMatInterest)

                from Toolbar.Build_Tree_Tools.Distance_Tree.Neighboor_Joining_Tree.converter_NJ_Tree_formation import *
                from Toolbar.Build_Tree_Tools.plotter_Tree import *

                #Generate directions w names
                direction_lst=direction_NJ(Pathway,only_name_array_samp)

                #Starts Multiple Sequence Alignment
                '''
                import Toolbar.Aligners.MultiDimensional_Alignment.Multiple_Sequence_Alignment_AA.generator_profile as GENprof
                ### CONTINUE

                MSA_profile_db=[]
                for i in chosen_db:
                    image=GENprof.converter_MS_sequences_to_image(i[0].AAseq)
                    profile=GENprof.converter_MS_image_to_profile(image)
                    MSA_profile_db.append(profile)
                print(MSA_profile_db)
                '''

                from Toolbar.Aligners.MultiDimensional_Alignment.Multiple_Sequence_Alignment_AA.collect_MSA import *
                End_MultipleSequenceGenerator(chosen_db, direction_lst)



            elif ans_sample_space=='Bisequencial Alignment':
                db=get_database_interface('CDS')
                ans=input('Bisequencial Alignment process will takes place ase (Global Alignment/Local Alignment)?')
                BiSequencial_Alignment_db = []
                ct=0
                while ct<=1:
                    for t in range(len(db)):
                        print('[' + str(t) + ']' + ' ' + str(db[t]) + ' || ' + db[t].chromosomeID)
                    print('\n')
                    selected_family_index = int(input('choose family:'))
                    family_in = db[selected_family_index].return_all_elements()

                    for i in range(len(family_in)):
                        print('[' + str(i) + ']' + ' ' + str(family_in[i]) + '|| ' + str(family_in[i].type))
                    print('\n')
                    chosen_element_ind = int(input('choose element will interest:'))
                    if family_in[chosen_element_ind].type == 'CDS':
                        BiSequencial_Alignment_db.append([family_in[chosen_element_ind], db[selected_family_index].chromosomeID])
                        ct+=1
                    else:
                        print('This is not a protein !')

                if ans=='Global Alignment':
                        import Toolbar.Aligners.Two_Dim_Alignment.Protein_Alignment.generate_aligned_bisequence_wscore as biGlobal
                        import Toolbar.Aligners.PAM_and_BLOSOM_Matrices.prepare_PAM as prePAM
                        Indel=int(input('Enter Indel score:'))
                        Extension=int(input('Enter Extension score:'))
                        PAM_path=get_path()
                        PAM_MAT = prePAM.import_PAM_Matrix(PAM_Table=PAM_path)
                        res, identity, score=biGlobal.generate_bisequence_aligned_calulate_score_of_prof(BiSequencial_Alignment_db[0][0].AAseq,BiSequencial_Alignment_db[1][0].AAseq,Indel,Extension,PAM_MAT)

                        print('\n')
                        print('Found Identity between two sequence:' + str(identity))
                        print('Raw score between these sequences:' + str(score))
                        print('\n')
                        print(res)


                elif ans=='Local Alignment':
                    import Toolbar.Aligners.Two_Dim_Alignment.Protein_Alignment.smith_waterman_all_for_Prot as SmithWatermanBiProt
                    Indel = int(input('Enter Indel score:'))
                    add_PaMBLOSUM_matrix=input('Add manuel PAM or BLOSUM Matrix, or Default (Y/N):')
                    print('\n\n')
                    if add_PaMBLOSUM_matrix=='Y':
                        PAM_BLOSUM_chosen=get_path()
                        image=SmithWatermanBiProt.End_Local_Alignment(BiSequencial_Alignment_db[0][0].AAseq,
                                                                      BiSequencial_Alignment_db[1][0].AAseq, Indel,PAM_BLOSUM=PAM_BLOSUM_chosen)
                    else:
                        image, end_score=SmithWatermanBiProt.End_Local_Alignment(BiSequencial_Alignment_db[0][0].AAseq,BiSequencial_Alignment_db[1][0].AAseq,Indel)
                    print(image)
                    print('score--'+str(end_score))



        elif ans_type=='Nucleic Acid':
            ans = input("Choose_Path:")
            if ans=='Multiple Sequence Alignment':
                pass
            elif ans=='Bisequencial Alignment':
                if ans=='Global Alignment':
                    pass
                elif ans=='Local Alignment':
                    pass

    elif ans_process=='PhyloTree':
        ans_tree_purpose=input('Input sample type of tree (Distance Tree/ Phylogenetic Tree): ')
        if ans_tree_purpose=='Distance Tree':

            #######
            DistanceMatInterest, only_name_array_proc1, only_name_array_samp, names, ct,chosen_db=generator_distance_matrix()
            for i in DistanceMatInterest:
                print(i)
            #######

            ans_dist_tree_type=input('Enter distance tree type (U_WPGMA/MinimumEvolution_LeastSquare/NeighboorJoining)')
            if ans_dist_tree_type=='U_WPGMA':

                ans=input("UPGMA/WPGMA")
                if ans=='UPGMA':
                    import Toolbar.Build_Tree_Tools.Distance_Tree.U_and_W_PGMA.UPGMA_Tree as UPGMA
                    Pathways=UPGMA.UPGMA_Tree(DistanceMatInterest)
                    Pathways = UPGMA.pair_name(only_name_array_proc1[:ct], only_name_array_samp, Pathways)
                else:
                    import Toolbar.Build_Tree_Tools.Distance_Tree.U_and_W_PGMA.WPGMA_Tree as WPGMA
                    Pathways = WPGMA.generate_route_list_of_WPGMA_Tree(DistanceMatInterest)
                    Pathways = WPGMA.pair_name(only_name_array_proc1[:ct], only_name_array_samp, Pathways)

                print('------------PATHWAYS---------------')
                print(Pathways)
                print('-----------------------------------')
                for elements in names:
                    print(elements)

                import Toolbar.Build_Tree_Tools.plotter_Tree as plotter
                plotter.plot_tree(Pathways)

            elif ans_dist_tree_type=='MinimumEvolution_LeastSquare':
                collected_tree, min_evo_least_sq=None,None
                ans=input('Minimum Evolution/Least Square')
                from Toolbar.Build_Tree_Tools.Distance_Tree.Least_Square_Min_Evolution_Tree.LeastSquareTree import *
                import Toolbar.Build_Tree_Tools.Distance_Tree.Least_Square_Min_Evolution_Tree.Min_Least_Tree_BaseFormation as MinEvoLeastSq
                from Toolbar.Build_Tree_Tools.Distance_Tree.Least_Square_Min_Evolution_Tree.Minimum_Evolution_Tree import *

                for i in range(len(DistanceMatInterest)):
                    for j in range((len(DistanceMatInterest[0]))):
                        if i == 0 and j != 0:
                            DistanceMatInterest[0][j] = only_name_array_samp[j - 1]
                        elif j == 0 and i != 0:
                            DistanceMatInterest[i][0] = only_name_array_samp[i - 1]

                if ans=='Least Square':

                    collected_tree = MinEvoLeastSq.collect_tree(DistanceMatInterest)  # Minimum_Evolution
                    min_evo_least_sq = least_square_tree(collected_tree, DistanceMatInterest)


                if ans=='Minimum Evolution':
                  collected_tree = MinEvoLeastSq.collect_tree(DistanceMatInterest)  # Minimum_Evolution
                  min_evo_least_sq = minimum_evolution_tree(collected_tree)

                print('----------------All Sample Space-------------------')
                for i in collected_tree:
                  print('\n')
                  for a in i:
                      print(a)
                print('------------Possible Positiive Distane Tree----------')
                for possibles in min_evo_least_sq:
                    print(possibles)

            elif ans_dist_tree_type=='NeighboorJoining':

                import Toolbar.Build_Tree_Tools.Distance_Tree.Neighboor_Joining_Tree.Neighboor_Joining_New as NJ
                print('--------------------NODES INFO---------------------')
                for i in range(len(DistanceMatInterest)):
                    for j in range((len(DistanceMatInterest[0]))):
                        if i == 0 and j != 0:
                            DistanceMatInterest[0][j] = only_name_array_samp[j - 1]
                        elif j == 0 and i != 0:
                            DistanceMatInterest[i][0] = only_name_array_samp[i - 1]
                Pathway = NJ.Neighboor_Joining(DistanceMatInterest)
                for elements in names:
                    print(elements)
                from Toolbar.Build_Tree_Tools.Distance_Tree.Neighboor_Joining_Tree.converter_NJ_Tree_formation import *
                from Toolbar.Build_Tree_Tools.plotter_Tree import *
                Pathway_Transformed = converter_NJ_tree_to_plot(Pathway)
                edited_path_w_names = exchange_w_names(Pathway_Transformed,only_name_array_samp)
                plot_tree_NJ(edited_path_w_names)


        elif ans_tree_purpose=='PhylogeneticTree':

            '''
            if MaximumParsimony:
    
            elif MaximumLikeHood:
            '''
            pass

    elif ans_process=='ProTools':
        ans_process=input('Input process will be proceed (Convergence Possible Domains/ Hydropathy Index): ')
        if ans_process == 'Convergence Possible Domains':
            pass
        elif ans_process == 'Hydropathy Index':
            db = get_database_interface('CDS')
            BiSequencial_Alignment_db = []
            ct = 0
            while ct <= 1:
                for t in range(len(db)):
                    print('[' + str(t) + ']' + ' ' + str(db[t]) + ' || ' + db[t].chromosomeID)
                print('\n')
                selected_family_index = int(input('choose family:'))
                family_in = db[selected_family_index].return_all_elements()

                for i in range(len(family_in)):
                    print('[' + str(i) + ']' + ' ' + str(family_in[i]) + '|| ' + str(family_in[i].type))
                print('\n')
                chosen_element_ind = int(input('choose element will interest:'))
                if family_in[chosen_element_ind].type == 'CDS':
                    BiSequencial_Alignment_db.append(
                        [family_in[chosen_element_ind], db[selected_family_index].chromosomeID])
                    ct += 1
                else:
                    print('This is not a protein !')

            import Toolbar.Hydropath_Index.Hydropath as Hydropathy

            window_range=int(input('Enter window range of the hydropathy index: '))

            ReferenceParameters = {
                "A": 1.8, "C": 2.5, "D": -3.5, "E": -3.5, "F": 2.8,
                "G": -0.4, "H": -3.2, "I": 4.5, "K": -3.9, "L": 3.8,
                "M": 1.9, "N": -3.5, "P": -1.6, "Q": -3.5, "R": -4.5,
                "S": -0.8, "T": -0.7, "V": 4.2, "W": -0.9, "Y": -1.3
            }

            Hydropathy.Hydropathy_End([BiSequencial_Alignment_db[0][1],BiSequencial_Alignment_db[0][0].AAseq],[BiSequencial_Alignment_db[1][1],BiSequencial_Alignment_db[1][0].AAseq],ReferenceParameters,window_range)



