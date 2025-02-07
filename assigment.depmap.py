from SigProfilerAssignment import Analyzer as Analyze
Analyze.cosmic_fit('data/depmap', 'data/depmap_signatures',
                   input_type="vcf",
                   context_type="96",
                   collapse_to_SBS96=True, cosmic_version=3.4, exome=False,
                   genome_build="GRCh37", signature_database=None,
                   exclude_signature_subgroups=None, export_probabilities=True,
                   export_probabilities_per_mutation=True, make_plots=False,
                   sample_reconstruction_plots=False, verbose=False)