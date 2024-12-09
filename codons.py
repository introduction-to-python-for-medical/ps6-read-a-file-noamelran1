file_path = 'data/codons.txt'

def create_codon_dict(file_path):
    with open(file_path) as file:
        rows = file.readlines()
    
    codon_to_amino_acid = {}
    
    for row in rows:
        cells = row.strip().split('\t')
        
        codon = cells[0]
        amino_acid = cells[2]
        
        codon_to_amino_acid[codon] = amino_acid
    
    return codon_to_amino_acid

codon_dict = create_codon_dict(file_path)

print(codon_dict)

