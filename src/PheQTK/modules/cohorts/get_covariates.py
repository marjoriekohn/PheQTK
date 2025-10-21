"""
This helper function asks the user if they want to update the covariates.
"""
from PheQTK.helpers.response_validation import validate_yes_no_response, validate_digit_response
from PheQTK.modules.cohorts import COVARIATES_CATALOG
from PheQTK.modules.cohorts.Covariates import Covariates
from PheQTK.helpers.presentation import *


def get_covariates() -> Covariates:
    """
    Interactive covariate picker for PheTK on AoU.
    Shows a brief explanation for each covariate, asks a single clear question,
    and lets the user confirm or redo the whole set.
    """

    # instantiate Covariates object
    covariates = Covariates()

    while True:
        # print default covariates settings
        rule("Default Settings for Covariates")
        print(covariates)

        # Overview
        para("We’ll step through each covariate. For each, you’ll see:")
        bullet("A short description")
        bullet("The current value (False means the covariate is excluded)")
        bullet("An option to update it")

        # loop through all covariates
        for item in COVARIATES_CATALOG:
            attr = item["attr"]
            label = item["label"]
            kind = item["kind"]
            help_text = item["help"]

            # get the covariate's current value
            current_value = getattr(covariates, attr)

            # print the information
            rule(f"Covariate: {attr}")
            para(f"{label}")
            bullet(f"Description: {help_text}")
            bullet(f"Current value: {current_value}")

            if kind == "bool":
                question = f"Include '{attr}'? (y/n): "
                want_on = validate_yes_no_response(input(question))
                setattr(covariates, attr, bool(want_on))
            elif kind == "int":
                question = f" Update '{attr}' (currently {current_value})? (y/n): "
                change_it = validate_yes_no_response(input(question))
                if change_it:
                    new_val = validate_digit_response(input("Enter a positive number: "))
                    setattr(covariates, attr, new_val)

        # verify covariates are correct before building cohorts
        rule("Updated Covariates")
        print(covariates)
        if validate_yes_no_response(input("Proceed with these covariates? (y/n): ")):
            rule("✅ Covariates confirmed.")
            return covariates

        para("🔁 No problem. Lets run through the options again.")



