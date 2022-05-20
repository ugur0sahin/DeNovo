class CDS:
    CDS_info = "CDSs are proteins"
    def __init__(self,product,geneID,AAseq, location,chromosomeID=None ):
        self.AAseq=AAseq
        self.product=product
        self.geneID=str(geneID)
        self.type='CDS'
        self.location=location[0]
        self.location_pose=location[1]
        self.chromosomeID = chromosomeID

    def __str__(self):
        #return (str(self.seq)+','+str(self.product)+','+str(self.geneID))
        return str(self.product)



class gene:
    def __init__(self,gene, geneID, gene_synonyms, location, chromosomeID=None):
        self.name=gene
        self.geneID = str(geneID)
        self.synonyms=gene_synonyms
        self.location=location[0]
        self.location_pose=location[1]
        self.type='gene'
        self.chromosomeID=chromosomeID
    def __str__(self):
        return str(self.name)


class Family:
    Family='Families composed of the same geneID include elements'
    def __init__(self,element_list,geneID,chromosomeID):
        CDS_lst, gene_lst=[],[]
        for i in element_list:
            if i.type =='CDS':
                CDS_lst.append(i)
            elif i.type=='gene':
                gene_lst.append(i)
        self.CDSs= CDS_lst
        self.genes = gene_lst
        self.geneID = str(geneID)
        self.element_list=element_list
        self.chromosomeID= chromosomeID

    def __str__(self):
        return str(self.geneID)
    def return_all_elements(self):
        return self.element_list

def categorizer_as_families(all_elements):  #IT DOESN'T WORK
    all_families=[]
    rec_all_elements=all_elements
    while not rec_all_elements == []:
        geneID_search = rec_all_elements[0].geneID
        for i in range(len(rec_all_elements)):
            geneFamily_collect_lst=[]
            if rec_all_elements[i].geneID == geneID_search:
                geneFamily_collect_lst.append(all_elements[i])
            if rec_all_elements[i+1].geneID != geneID_search and i < len(rec_all_elements)-3:
                break
        for found in geneFamily_collect_lst:
            rec_all_elements.remove(found)
        all_families.append(Family(geneFamily_collect_lst,rec_all_elements[i].geneID))



