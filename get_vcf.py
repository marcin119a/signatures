# Przekształcenie danych do formatu VCF
import pandas as pd

df = pd.read_parquet('data/df.parquet.hugo.snp.ins.del.all.qzip')


df_vcf = df.apply(
    lambda row: [
        row['Chromosome'].replace('chr', ''),
        row['Start'],
        row['file_gdc_id'],
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


# Grupowanie po 'file_gdc_id'
grouped = df.groupby("file_gdc_id")

def save_to_vcf(group, file_path):
    vcf_header = """##fileformat=VCFv4.2
##source=CustomConversionScript
##reference=GRCh38
#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tMOTIF\tSTRAND
"""
    with open(file_path, "w") as vcf_file:
        vcf_file.write(vcf_header)
        for _, row in group.iterrows():
            vcf_file.write(
                f"{row['Chromosome'].replace('chr', '')}\t{row['Start']}\t{row['file_gdc_id']}\t"
                f"{row['Reference_Allele']}\t{row['Tumor_Seq_Allele2']}\t.\tSimulations\tGRCh38\t"
                f"{row['Mutational_Motif']}\t+\n"
            )

import os
output_dir = "data/genomic_mutations"
os.makedirs(output_dir, exist_ok=True)


vcf_file_paths = []
for file_gdc_id, group in grouped:
    vcf_file_name = f"{file_gdc_id}.vcf"
    vcf_file_path = os.path.join(output_dir, vcf_file_name)
    save_to_vcf(group, vcf_file_path)
    vcf_file_paths.append(vcf_file_path)

