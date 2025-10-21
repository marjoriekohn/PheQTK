import csv

from PheQTK.helpers.response_validation import validate_yes_no_response, \
    validate_digit_response
from PheQTK.modules.cohorts import PHEWAS_CATALOG
from PheQTK.modules.phewas.Phewas import Phewas
from PheQTK.helpers.presentation import *


def get_settings(phecodes, variants) -> list[Phewas]:
    """Build a list of Phewas objects (one per variant) so that:
     • A Phewas run is specific to one variant.
     • A Phewas run uses the same covariates for all variants.
     • A Phewas run uses the same phecode settings for all variants.
    """

    settings: list[Phewas] = []

    # We keep a temporary location to hold the two configuration settings
    base = Phewas(covariate_cols=[])

    # PHECODE SETTINGS (same for all runs)
    setattr(base, "phecode_version", phecodes.phecode_version)
    setattr(base, "phecode_count_csv_path", phecodes.output_file_name)

    while True:
        # PHEWAS CONFIGURATION (same for all runs)
        for item in PHEWAS_CATALOG:
            attr = item["attr"]
            label = item["label"]
            help_text = item["help"]

            # get the current config settings
            current_value = getattr(base, attr)
            print(f"\n{label}")
            print(f"  Description: {help_text}")
            print(f"  Current value: {current_value}")

            # update the settings if the user wants to
            if validate_yes_no_response(input(f"  Update '{attr}' (y/n): ")):
                new_val = validate_digit_response(input("Enter a positive integer: "))
                setattr(base, attr, int(new_val))

        # PER-VARIANT PHEWAS CONSTRUCTION (one for each variant)
        settings.clear()        # clear the list of settings
        rejected_any = False    # reset the rejected_any flag

        for variant in variants:

            # create a phewas object for each variant and add global settings
            phewas = Phewas(covariate_cols=[])

            # save global configuration to the new object
            setattr(phewas, "phecode_version", getattr(base, "phecode_version"))
            setattr(phewas, "phecode_count_csv_path", getattr(base, "phecode_count_csv_path"))
            setattr(phewas, "min_cases", int(getattr(base, "min_cases")))
            setattr(phewas, "min_phecode_count", int(getattr(base, "min_phecode_count")))

            with open(variant.covariate_file, "r") as infile:
                reader = csv.reader(infile)
                header = next(reader)

                # skip the first two columns (patient id and case)
                setattr(phewas, "covariate_cols", header[2:])

                # find the "sex_at_birth" column name
                if header[3].startswith("sex"):
                    setattr(phewas, "sex_at_birth_col", header[3])
                elif header[4].startswith("sex"):
                    setattr(phewas, "sex_at_birth_col", header[4])
                elif header[5].startswith("sex"):
                    setattr(phewas, "sex_at_birth_col", header[5])

            # variant dependent paths
            setattr(phewas, "cohort_csv_path", variant.cohort_file)
            setattr(phewas, "output_file_name", f"{variant.variant_id}_phewas_results.csv")

            # print updated phewas configuration
            rule(f"Updated PheWAS Configuration for {variant.variant_id}")
            print(phewas)

            # confirm with the user that the settings are correct
            if validate_yes_no_response(input("Proceed with this configuration? (y/n): ")):
                rule(f"✅ PheWAS Configuration for {variant.variant_id} confirmed.")
                settings.append(phewas)

            # stop iterating over variants if the user rejects the settings
            else:
                print("🔁 No problem. Let’s run through the options again.")
                rejected_any = True
                break

        # if all variants are confirmed, break out of the loop
        if not rejected_any:
            break

    return settings
