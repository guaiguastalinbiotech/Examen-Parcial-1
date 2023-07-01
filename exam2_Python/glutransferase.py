# Escriba aquí su código para el ejercicio 2
#import modulo
def source(data): 
    file = open(data, "r")
    secuencias  = open("data/source.gb", "w")
    for linea in file:
        Entrez.email = "stalin.guaigua@est.ikiam.edu.ec"
        handle=Entrez.efetch(db="nucleotide" ,id=linea ,rettype="gb", retmode="text")
        data=(handle.read())
        secuencias.write(data) 
    genbank = list(SeqIO.parse("data/source.gb", "genbank"))
    source = []
    for i in range(len(genbank)):
        source.append(genbank[i].annotations["source"])
        frecuencias = collections.Counter(source)
    frecuencias = collections.Counter(source)
    df = pd.DataFrame(frecuencias.items(), columns=["Especie", "Frecuencia"])
    df.to_csv("results/frecuencias.csv") 
    return df 


def sequences(data): 
    file = open(data, "r")
    secuencias  = open("data/sequences.gb", "w")
    for linea in file: 
        Entrez.email = "stalin.guaigua@est.ikiam.edu.ec"
        handle=Entrez.efetch(db="nucleotide" ,id=linea ,rettype="gb", retmode="text")
        data=(handle.read())
        secuencias.write(data) 
    genbank = list(SeqIO.parse("data/sequences.gb", "genbank"))
    MW = []
    indice = []
    for i in range(len(genbank)):
        seq_peptide = genbank[i].seq.translate()
        if seq_peptide[0] == "M" and not re.search(re.escape("*"), str(seq_peptide[0:-1])):
            temp = ProteinAnalysis(seq_peptide[0:-1])
            MW.append(temp.molecular_weight())
            indice.append(temp.instability_index())
    df = pd.DataFrame() 
    df ["Peso Molecular"] = MW 
    df ["Indice de inestabilidad"] = indice
    df.to_csv("results/glupeptides.csv")  
    plt.plot(MW, indice, 'x', color='yellow')
    plt.xlabel('Peso Molecular [Daltons]', fontsize=12)
    plt.ylabel('Indice de Inestabilidad', fontsize=12)
    plt.savefig("results/glupeptides.png")
    