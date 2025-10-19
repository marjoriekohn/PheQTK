from PheTK.Cohort import Cohort

# TODO: we need to pass in each covariate the user wants to include
# TODO: add a description of each covariate


def get_covariates(cohort: Cohort):
    cohort.add_covariates(
        cohort_csv_path="rs61738161_cohort.csv",
        age_at_last_event=True,
        sex_at_birth=True,  # sex_at_birth_col is always required as certain phecodes are sex restricted
        first_n_pcs=3,
        drop_nulls=True,
        output_file_name="rs61738161_cohort_with_covariates.csv"
    )
