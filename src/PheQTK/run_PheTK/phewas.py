from PheTK.PheWAS import PheWAS


def run_phewas(settings):

    # instantiate class PheWAS object and provide information for the PheWAS run
    phewas = PheWAS(
        phecode_version=settings.phecode_version,
        phecode_count_csv_path=settings.output_file_name,
        cohort_csv_path=settings.cohort_file,
        sex_at_birth_col="sex_at_birth",
        covariate_cols=[],
        independent_variable_of_interest="case",
        min_cases=settings.min_cases,
        min_phecode_count=settings.min_phecode_count,
        output_file_name="rs61738161_phewas_results.csv"
    )

    # run PheWAS
    phewas.run()
