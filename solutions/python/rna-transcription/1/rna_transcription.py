def to_rna(dna_strand: str):
    rna_complement = {"G": "C", "C": "G", "T": "A", "A": "U"}
    return "".join([rna_complement[n] for n in dna_strand])
