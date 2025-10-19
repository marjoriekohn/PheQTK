"""
This helper function prints helpful information about covariates.
The user is asked if they want to change them.
"""
from src.PheQTK.helpers.response_validation import validate_yes_no_response, validate_int_response


def get_covariates():
    # get covariate information from user
    print("To review currently supported covariates visit "
          "https://github.com/nhgritctran/PheTK?tab=readme-ov-file#512-add_covariates")
    print("By default, PheTK sets all covariates to 'no'")

    raw_natural_age = input("Do you want to include natural age? (y/n): ")
    natural_age = validate_yes_no_response(raw_natural_age)

    age_at_last_event = input("Do you want to include age at last event? (y/n): ")
    sex_at_birth = input("Do you wan to include sex at birth? (y/n): ")
    ehr_length = input("Do you want to include ehr length? (y/n): ")
    dx_code_occurrence_count = input("Do you want to include dx code occurrence count? (y/n): ")
    dx_condition_count = input("Do you want to include dx condition count? (y/n): ")
    genetic_ancestry = input("Do you want to include genetic ancestry? (y/n): ")

    raw_first_n_pcs = input("How many PCs do you want to include?: ")
    first_n_pcs = validate_int_response(raw_first_n_pcs)

    drop_nulls = input("Do you want to drop nulls? (y/n): ")

    # TODO: set the ones that are true to true in the object
    Covariates.set(raw_natural_age, natural_age)
