import pandas as pd
from Bio.Seq import Seq

def design_inner_primers(sequence, ref_allele, alt_allele, snp_position=1, primer_length=20):
    """
    Designs inner primers for Tetra-ARMS PCR.
    - Inner forward primer: Takes 20 bp upstream of SNP, keeping the SNP at the 3' end.
    - Inner reverse primer: Takes 20 bp starting from SNP position (551) and replaces the SNP with the reverse complement of the alternative allele.
    """
    # Inner forward primer: 20 bases before SNP, SNP at the 3' end
    inner_forward = sequence[snp_position - primer_length:snp_position]  # Reference allele at SNP
    
    # Inner reverse primer: Take 20 bp starting from SNP (551), then reverse complement
    reverse_seq = sequence[snp_position - 1:snp_position + primer_length - 1]  # Start at SNP position (551)
    rev_complement = str(Seq(reverse_seq).reverse_complement())  # Reverse complement full sequence
    rev_complement = rev_complement[:19] + str(Seq(alt_allele).complement())  # Replace SNP with alternative allele complement
    
    return inner_forward, rev_complement

def process_ods(input_file, output_file):
    df = pd.read_excel(input_file, engine="odf")  # Read ODS file
    df["Full Sequence"] = df["Full Sequence"].astype(str).replace("nan", "").str.strip()
    primer_data = []
    
    for index, row in df.iterrows():
        seq_id, ref, alt, sequence = row["Sequence ID"], row["Reference Allele"], row["Alternative Allele"], row["Full Sequence"]
        inner_f, inner_r = design_inner_primers(sequence, ref, alt)
        
        primer_data.append([seq_id, f"Inner Forward ({ref})", inner_f])
        primer_data.append([seq_id, f"Inner Reverse ({alt})", inner_r])
    
    primer_df = pd.DataFrame(primer_data, columns=["Sequence ID", "Primer Type", "Sequence"])
    primer_df.to_excel(output_file, index=False, engine="odf")  # Save as ODS file
    print(f"Inner primers saved to {output_file}")

# Example usage
input_ods = "remaining.ods"  # Replace with your actual ODS file
output_ods = "remainingout.ods"
process_ods(input_ods, output_ods)
