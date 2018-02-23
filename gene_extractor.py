import numpy as np
import h5py
import itertools



#helpers
def geneExtractor(target_list, data, labels):
    data_return = []
    label_return = []
    for i in range(len(data)):
        if (labels[i][0] == target_list[0] and labels[i][1] == target_list[1] and labels[i][2] == target_list[2]):
            data_return.append(data[i])
            label_return.append(labels[i])

    return data_return, label_return

def iterGen(x,y,z):
    if(x == y and  y == z):
        return [x,y,z]
    return ([x,y,z], [z,x,y], [y,z,x])

def shift(l,n):
    return l[n:] + l[:n]


def extract_data(x,y,z,data,label):
    
    #get valid iterations of x, y, z
    a = iterGen(x,y,z)
    
    #get corresponding expression data
    genes = []
    c = []
    labels = []
    l = []
    for i in a:
        c,l = geneExtractor(i, data, label)
        genes.extend(c)
        labels.extend(l)
        
    genes = np.array(genes)
    
    #creat final dataset (reorder shuffled labels)
    gene_final = []
    label_final = []
    
    for j in range(len(genes)):
        temp_gene = list(genes[j])
        temp_label = list(labels[j])
        while (temp_label[0] != x or temp_label[1] != y or temp_label[2] != z):
            temp_label = shift(temp_label, 1)
            temp_gene = shift(temp_gene, 1)


        gene_final.append(temp_gene)
        label_final.append(temp_label)
    
    return np.transpose(np.array(gene_final), [0,2,1]), np.array(label_final)
