import os
from Interface_And_File_Manipulating import load_main_dictionary as main_dict


def file_show_and_choose_import_as_dict():
    files = os.listdir('/Users/ugursahin/Desktop/DeNovo-master kopyası/Modal_Organism_Databases')
    for i in files:
        if i != '.DS_Store':
            print(i)
    chosen_organism=input('Input Organism you Interest: ')
    files = os.listdir('/Users/ugursahin/Desktop/DeNovo-master kopyası/Modal_Organism_Databases'+'/'+chosen_organism)
    for i in files:
        if i != '.DS_Store':
            print(i)
    chosen_chromosome=input('Input Chromosome you Interest: ')

    dictionary_of_chromsome=main_dict.read_orginized_data_Advanced(chosen_organism,chosen_chromosome)

    return dictionary_of_chromsome