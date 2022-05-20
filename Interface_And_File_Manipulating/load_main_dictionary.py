import pickle

main_dict = {}
'''
Read data from Data_Analyze_Text and load main dictionary.
Resulting dictionary will have the following form:
    
    { geneID1: { 'mRNA': [data], 'gene': [data] } , geneID2: { 'ncRNA': [data], 'mRNA': [data] } , ... }

'''
def read_orginized_data():
    with open('/Users/ugursahin/Desktop/DeNovo-master kopyası/Modal_Organism_Databases/Homo_Sapiens/Chromosome 1/Data_Analyze_Text_E.txt', 'rb') as file:
        main_list = pickle.load(file)
    for sample in main_list:
        rna = 0
        gene_id = sample[0]
        main_dict[gene_id] = {}
        for i in range(1, len(sample)):
            type = sample[i][0]  # gene, mRNA, ncRNA etc
            if not type in main_dict[gene_id].keys():
                main_dict[gene_id][type] = [sample[i][1:]]
            else:
                main_dict[gene_id][type].append(sample[i][1:])
    file.close()
    return main_dict


def read_orginized_data_Advanced(Organism,Chromosome):
    with open('/Users/ugursahin/Desktop/DeNovo-master kopyası/Modal_Organism_Databases/'+'/'+Organism+'/'+Chromosome+'.txt', 'rb') as file:
        main_list = pickle.load(file)
    for sample in main_list:
        rna = 0
        gene_id = sample[0]
        main_dict[gene_id] = {}
        for i in range(1, len(sample)):
            type = sample[i][0]  # gene, mRNA, ncRNA etc
            if not type in main_dict[gene_id].keys():
                main_dict[gene_id][type] = [sample[i][1:]]
            else:
                main_dict[gene_id][type].append(sample[i][1:])
    file.close()
    return main_dict

