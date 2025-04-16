import pandas as pd

df = pd.read_parquet('data/mutations.case_barcode.parquet')


# Tworzenie nagłówka VCF
vcf_header = """##fileformat=VCFv4.2
##source=CustomConversionScript
##reference=GRCh38
#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tMOTIF\tSTRAND
"""


# Grupowanie po 'file_gdc_id'
grouped = df.groupby("case_barcode")

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
                f"{row['Chromosome'].replace('chr', '')}\t{row['Start_position']}\t{row['case_barcode']}\t"
                f"{row['Reference_Allele']}\t{row['Tumor_Seq_Allele2']}\t.\tcase_barcode\tGRCh38\t"
                f".\t+\n"
            )

import os
output_dir = "data/case_barcode"
os.makedirs(output_dir, exist_ok=True)


vcf_file_paths = []
for file_gdc_id, group in grouped:
    vcf_file_name = f"{file_gdc_id}.vcf"
    vcf_file_path = os.path.join(output_dir, vcf_file_name)
    save_to_vcf(group, vcf_file_path)
    vcf_file_paths.append(vcf_file_path)

