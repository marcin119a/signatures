# Przekształcenie danych do formatu VCF
import pandas as pd


data = {
    "file_gdc_id": [
        "c02f3470-fce6-4ce8-a9e1-36023db2a3a8",
        "ad0dda7c-8df4-4160-a1a7-6657a7c4b74b",
        "4fa45b01-7ec4-41fe-adf6-396cc547dc78",
        "4fa45b01-7ec4-41fe-adf6-396cc547dc78",
        "c719388b-5210-49ac-b187-f3348d0c0790"
    ],
    "project_short_name": [
        "BEATAML1.0-COHORT",
        "BEATAML1.0-COHORT",
        "BEATAML1.0-COHORT",
        "BEATAML1.0-COHORT",
        "BEATAML1.0-COHORT"
    ],
    "Variant_Type": ["SNP", "SNP", "SNP", "SNP", "SNP"],
    "Variant_Classification": [
        "Silent",
        "Silent",
        "Intron",
        "Missense_Mutation",
        "3'Flank"
    ],
    "Reference_Allele": ["A", "A", "A", "A", "A"],
    "Tumor_Seq_Allele1": ["A", "A", "A", "A", "A"],
    "Tumor_Seq_Allele2": ["G", "G", "G", "C", "G"],
    "Gene": [
        "ENSG00000135953",
        "ENSG00000127530",
        "ENSG00000125107",
        "ENSG00000196998",
        "ENSG00000163399"
    ],
    "Exon": ["2/6", "1/1", "None", "8/11", "None"],
    "Start": [102732353, 14799855, 58543568, 49075707, 116405640],
    "End": [102732353, 14799855, 58543568, 49075707, 116405640],
    "Chromosome": ["chr2", "chr19", "chr16", "chrX", "chr1"],
    "Mutational_Motif": ["C[A>G]A", "C[A>G]A", "A[A>G]A", "G[A>C]A", "G[A>G]A"]
}
df = pd.DataFrame(data)



df_vcf = df.apply(
    lambda row: [
        row['Chromosome'].replace('chr', ''),
        row['Start'],
        row['Reference_Allele'],
        row['Tumor_Seq_Allele2'],
        '.',
        'Simulations',
        'GRCh38',
        row['Reference_Allele'],
        '+1'
    ],
    axis=1
)


# Tworzenie nowej ramki VCF
columns_vcf = [
    "Chromosome", "Position", "ID", "Ref", "Alt", "Qual", "Filter", "Info", "Motif", "Strand"
]
df_vcf = pd.DataFrame(df_vcf.tolist(), columns=columns_vcf)

vcf_filename = "data/vcf/converted_data.vcf"

# Tworzenie nagłówka VCF
vcf_header = """##fileformat=VCFv4.2
##source=CustomConversionScript
##reference=GRCh38
#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tMOTIF\tSTRAND
"""

# Zapis danych do pliku VCF
with open(vcf_filename, "w") as vcf_file:
    vcf_file.write(vcf_header)
    df_vcf.to_csv(vcf_file, sep="\t", index=False, header=False)
