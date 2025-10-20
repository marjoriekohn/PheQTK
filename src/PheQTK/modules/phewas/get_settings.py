from PheQTK.helpers.response_validation import validate_yes_no_response, validate_digit_response
from PheQTK.modules.phewas.Phewas import Phewas


def get_settings(phecodes, variants) -> list[Phewas]:
    settings = []
    covariate_cols = []

    # create the phewas object
    phewas = Phewas(covariate_cols)

    # USER DEFINED SETTINGS
    # min_cases settings
    print(f"To test a phecode, there must be {phewas.min_cases} cases and at "
          f"least {phewas.min_cases} controls per phecode.")
    is_min_cases = input("Do you want to change min_cases? (y/n): ")
    is_min_cases = validate_yes_no_response(is_min_cases)
    if is_min_cases:
        user_input = input("Enter the minimum number of cases: ")
        user_input = validate_digit_response(user_input)
        setattr(phewas, "min_cases", user_input)
        print(f"Phecodes must now have at least {phewas.min_cases} cases and controls for the phecode to be tested.")

    # min_phecode_count settings
    print(f"A participant is considered a 'case' for a phecode if they have {phewas.min_phecode_count} or more qualifying events.")
    is_min_phecode_count = input("Do you want to change min_phecode_count? (y/n): ")
    is_min_phecode_count = validate_yes_no_response(is_min_phecode_count)
    if is_min_phecode_count:
        user_input = input("Enter the minimum number of phecode counts: ")
        user_input = validate_digit_response(user_input)
        setattr(phewas, "min_phecode_count", user_input)
        print(f"A participant must now have a minimum count of {phewas.min_phecode_count} phecode events to be considered a case.")

    # PHECODE SETTINGS
    phecode_version = phecodes.phecode_version
    setattr(phewas, "phecode_version", phecode_version)

    phecode_count_csv_path = phecodes.output_file_name
    setattr(phewas, "phecode_count_csv_path", phecode_count_csv_path)

    # VARIANT DEPENDENT SETTINGS
    for variant in variants:

        # get covariate columns
        with open(f"{variant.covariate_file}", "r") as infile:
            header_line = infile.readline().strip().split(",")

            # the first two columns are patient id and case
            covariate_cols.append(header_line[2:])

            # TODO: get sex_at_birth column name

        # get cohort csv path
        cohort_csv_path = variant.cohort_file
        setattr(phewas, "cohort_csv_path", cohort_csv_path)

        # create the output file name
        output_file_name = f"{variant.variant_id}_phewas_results.csv"
        setattr(phewas, "output_file_name", output_file_name)

        # print default settings for user to review
        print(f"{phewas}")

        # verify settings are correct before running phewas
        user_confirmation = input("Are these settings correct? (y/n): ")
        confirmation = validate_yes_no_response(user_confirmation)

        if not confirmation:
            get_settings(phecodes, variants)

        # add these settings to the list
        settings.append(phewas)

    return settings
