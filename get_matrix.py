from SigProfilerMatrixGenerator.scripts import SigProfilerMatrixGeneratorFunc as matGen

matrices = matGen.SigProfilerMatrixGeneratorFunc("signatures",
                                                 "GRCh38",
                                                 "data/genomic_mutations")

