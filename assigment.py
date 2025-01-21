from SigProfilerAssignment import Analyzer as Analyze
Analyze.cosmic_fit('/Users/mw/PycharmProjects/get_vcsv/data/genomic_mutations/output/SBS/signatures.SBS96.all', 'data/signatures',
                   input_type="matrix",
                   context_type="96",
                   collapse_to_SBS96=True, cosmic_version=3.4, exome=False,
                   genome_build="GRCh38", signature_database=None,
                   exclude_signature_subgroups=None, export_probabilities=False,
                   export_probabilities_per_mutation=False, make_plots=False,
                   sample_reconstruction_plots=False, verbose=False)