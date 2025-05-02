# inner-primer-design-Tetra--Arms-InsilicoPCR
# Inner Primer Design Script for Tetra-Primer ARMS PCR

This Python script automates the design of **inner forward and reverse primers** for **Tetra-Primer ARMS PCR (ARMS-PCR)**, a method used for SNP genotyping.

---

## 🎯 Purpose

The script generates **allele-specific inner primers** for Tetra-Primer ARMS PCR. The key points are:

- The **forward inner primer** ends at the SNP position and matches the **wild-type allele** at its 3′ end.
- The **reverse inner primer** ends at the SNP position (reverse complement strand) and matches the **alternate (mutant) allele** at its 3′ end.

---

## 📂 Input Format

The input should be an **ODS file**or any other suitable format containing the following information for each SNP:, where each row contains the following information for each SNP:

- `Sequence ID` – Identifier for the sequence
- `Reference Allele` – The base at the SNP in the wild-type allele
- `Alternative Allele` – The base at the SNP in the mutant/alternate allele
- `Full Sequence` – Nucleotide sequence (e.g., 350 bp upstream + SNP + 550 bp downstream)

### Example ODS Format:

| Sequence ID | Reference Allele | Alternative Allele | Full Sequence                 |
|-------------|------------------|--------------------|-------------------------------|
| chr1        | G                | A                  | ATGCGTACG... (900 bp total)   |
| chr2        | T                | C                  | GTACGTCAG... (900 bp total)   |

⚠️ **Note:**  
The SNP position is **assumed to be fixed in the script** (e.g., **position 551**), so you don’t need to specify it in the input.

---

## 🧪 Output

The script generates an **ODS file** containing the designed inner primers:

- **Forward inner primer** (matching the wild-type allele)
- **Reverse inner primer** (matching the alternate allele, reverse complement)

### Example Output:

| Sequence ID | Primer Type              | Sequence        |
|-------------|--------------------------|-----------------|
| chr1        | Inner Forward (G)         | ATGCGTACG...    |
| chr1        | Inner Reverse (A)         | TGCATGCA...    |
| chr2        | Inner Forward (T)         | GTACGTCAG...    |
| chr2        | Inner Reverse (C)         | GATGTCAG...    |

---

## ⚙️ How It Works

- The **SNP position** is fixed at **position 551** in the input sequences.
- **Inner forward primer** is designed to end at the SNP and match the **wild-type allele** at its 3′ end.
- **Inner reverse primer** is designed to end at the SNP (on the reverse complement strand) and match the **alternate allele** at its 3′ end.

---

## 🚀 Usage

```bash
python inner_primer_design.py --input sequences.ods --output primers.ods
