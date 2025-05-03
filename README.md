# 🧬 Inner Primer Design Script for Tetra-Primer ARMS PCR

This Python script automates the design of **inner forward** and **inner reverse** primers for **Tetra-Primer ARMS PCR**, a widely used method for **SNP genotyping**.

---

## 🎯 Purpose

The script generates **allele-specific inner primers**:

- **Inner Forward Primer:** Ends at the SNP position (3′ end) and matches the **wild-type allele**.
- **Inner Reverse Primer:** Ends at the SNP position (reverse complement) and matches the **alternate (mutant) allele**.

This ensures that each inner primer is highly specific for its corresponding allele.

---

## 📂 Input Format

The script processes a `.csv` (or any table-readable format) file containing the following columns:

| Column             | Description                                                |
|--------------------|------------------------------------------------------------|
| Sequence ID        | Identifier for the SNP entry                               |
| Reference Allele   | The wild-type nucleotide at the SNP position               |
| Alternative Allele | The mutant or alternate nucleotide at the SNP position     |
| Full Sequence      | ~900 bp flanking sequence (e.g., 350 bp upstream + 550 downstream) |

### 📌 Example Input:

| Sequence ID | Reference Allele | Alternative Allele | Full Sequence         |
|-------------|------------------|--------------------|------------------------|
| chr1        | G                | A                  | ATGCGTACG... (900 bp) |
| chr2        | T                | C                  | GTACGTCAG... (900 bp) |

> ⚠️ **Note:** The SNP is assumed to be at position **551** (i.e., 350 bp upstream of SNP in the full sequence).  
No separate SNP position input is required.

---

## 🧪 Output

The script generates an `.ods` file with two rows per SNP:

| Sequence ID | Primer Type           | Sequence         |
|-------------|-----------------------|------------------|
| chr1        | Inner Forward (G)     | ATGCGTACG...     |
| chr1        | Inner Reverse (A)     | TGCATGCA...      |
| chr2        | Inner Forward (T)     | GTACGTCAG...     |
| chr2        | Inner Reverse (C)     | GATGTCAG...      |

---

## 🔧 How It Works

- **SNP Position:** Fixed at 551 within the input sequence.
- **Inner Forward Primer:**
  - Extracts 20 bp upstream ending at SNP.
  - SNP base at 3′ end, matching **reference allele**.
- **Inner Reverse Primer:**
  - Extracts 20 bp starting from SNP.
  - Takes reverse complement and modifies SNP base to match **alternate allele** at 3′ end.

---

## 🧬 Primer Pairing Strategy (Tetra-ARMS)

For each SNP, you’ll need four primers:

| Primer Type       | Designed By        | Target Allele     |
|-------------------|--------------------|--------------------|
| Outer Forward (OF)| External (e.g., IDT Tool) | Flanks region |
| Outer Reverse (OR)| External           | Flanks region |
| Inner Forward (IF)| **This Script**    | Wild-Type allele   |
| Inner Reverse (IR)| **This Script**    | Alternate allele   |

### 🧪 Recommended Pairing in PCR:

- **OF + IR →** Amplifies **alternate allele**
- **IF + OR →** Amplifies **wild-type allele**

---

## 🚀 Usage

You don't need to specify input or output files as command-line arguments. The filenames are set directly in the script.

## 🔭 Scope

This tool is intended **only for designing inner primers** for allele-specific SNP detection.  
**Outer primers** should be designed using tools such as:

- [IDT PrimerQuest Tool](https://www.idtdna.com/Primerquest)
- [Primer3](http://primer3.ut.ee/)

---

### Example:

1. Place your input file as `sequences.csv` (or other suitable format).
2. Run the script:

```bash
python inner_primer_design.py
