from dataclasses import dataclass


@dataclass
class Covariates:
    natural_age: bool = False
    age_at_last_event: bool = False
    sex_at_birth: bool = False
    ehr_length: bool = False
    dx_code_occurrence_count: bool = False
    dx_condition_count: bool = False
    genetic_ancestry: bool = False
    first_n_pcs: int = 10
    drop_nulls: bool = False

    @property
    def name(self) -> str:
        return (f"natural_age: {self.natural_age}\n"
                f"age_at_last_event: {self.age_at_last_event}\n"
                f"sex_at_birth: {self.sex_at_birth}\n"
                f"ehr_length: {self.ehr_length}\n"
                f"dx_code_occurrence_count: {self.dx_code_occurrence_count}\n"
                f"dx_condition_count: {self.dx_condition_count}\n"
                f"genetic_ancestry: {self.genetic_ancestry}\n"
                f"first_n_pcs: {self.first_n_pcs}\n"
                f"drop_nulls: {self.drop_nulls}\n"
                )

    def __set__(self, instance, value):
        self.instance = value
