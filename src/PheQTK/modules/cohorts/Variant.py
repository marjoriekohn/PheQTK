from dataclasses import dataclass


@dataclass
class Variant:
    variant_id: str
    chromosome: int
    position: int
    ref_allele: str
    alt_allele: str
    cohort_file: str
    covariate_file: str

    @property
    def name(self) -> str:
        return (f"Variant ID: {self.variant_id}\n"
                f"Chromosome: {self.chromosome}\n"
                f"Position: {self.position}\n"
                f"Reference Allele: {self.ref_allele}\n"
                f"Alternate Allele: {self.alt_allele}\n"
                )


"""
The Covariates class is used to store the covariates for ALL cohorts.
This means that the covariates are the same for ALL cohorts.
The user has the opportunity to change the covariates when the program is run.
"""


@dataclass
class Covariates:
    cohort_csv_path: str
    natural_age = False
    age_at_last_event = False
    sex_at_birth = False
    ehr_length = False
    dx_code_occurrence_count = False
    dx_condition_count = False
    genetic_ancestry = False
    first_n_pcs = 10
    drop_nulls = False
    output_file_name: str

    @property
    def name(self) -> str:
        return (f"cohort_csv_path: {self.cohort_csv_path}\n"
                f"natural_age: {self.natural_age}\n"
                f"age_at_last_event: {self.age_at_last_event}\n"
                f"sex_at_birth: {self.sex_at_birth}\n"
                f"ehr_length: {self.ehr_length}\n"
                f"dx_code_occurrence_count: {self.dx_code_occurrence_count}\n"
                f"dx_condition_count: {self.dx_condition_count}\n"
                f"genetic_ancestry: {self.genetic_ancestry}\n"
                f"first_n_pcs: {self.first_n_pcs}\n"
                f"drop_nulls: {self.drop_nulls}\n"
                f"output_file_name: {self.output_file_name}\n"
                )

    def __set__(self, instance, value):
        self.instance = value
