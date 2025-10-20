from dataclasses import dataclass


@dataclass
class Phewas:
    covariate_cols: list[str]
    phecode_version: str = "X"
    phecode_count_csv_path: str = "aou_phecode_counts.csv"
    cohort_csv_path: str = "cohort.csv"
    sex_at_birth_col: str = "sex_at_birth"
    independent_variable_of_interest: str = "case"
    min_cases: int = 50
    min_phecode_count: int = 2
    output_file_name: str = "phewas_results.csv"

    def __str__(self) -> str:
        return (f"-------------------------------------------------\n"
                f"PheWAS Settings\n"
                f"-------------------------------------------------\n"
                f"phecode_version = {self.phecode_version}\n"
                f"phecode_count_csv_path = {self.phecode_count_csv_path}\n"
                f"cohort_csv_path = {self.cohort_csv_path}\n"
                f"sex_at_birth_col = {self.sex_at_birth_col}\n"
                f"covariate_cols = {self.covariate_cols}\n"
                f"independent_variable_of_interest = {self.independent_variable_of_interest}\n"
                f"min_cases = {self.min_cases}\n"
                f"min_phecode_count = {self.min_phecode_count}\n"
                f"output_file_name = {self.output_file_name}\n"
                f"-------------------------------------------------\n")
