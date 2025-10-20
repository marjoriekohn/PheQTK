from PheQTK.helpers.response_validation import validate_yes_no_response
from PheQTK.modules.cohorts.get_covariates import get_covariates
from PheQTK.modules.cohorts.get_variants import get_variants
from PheQTK.modules.phecodes.get_phecodes import get_phecodes
from PheQTK.modules.phewas.get_settings import get_settings
from PheQTK.run_PheTK.cohorts import get_cohort
from PheQTK.run_PheTK.counts import get_counts
from PheQTK.run_PheTK.phewas import run_phewas
from PheQTK.helpers.presentation import *


def run():

    # Welcome
    rule()
    rule("Welcome to PheQTK — The PheWAS Quick Toolkit")
    para(
        "PheQTK is a friendly wrapper around the PheTK package that guides you "
        "through a complete PheWAS with minimal coding. You’ll provide your core "
        "choices up front; PheQTK will confirm them and then run each step for you.")
    rule()

    # Overview
    para("PheQTK automates the following modules:")
    bullet("Cohorts — build a genotype-defined cohort with covariates")
    bullet("Phecodes — choose Phecode and ICD mapping versions")
    bullet("PheWAS — run association scans using your cohort and mappings")
    bullet("Plots — visual summaries (coming soon)")
    rule()

    # Module 1: Variants & Covariates
    step(1, "Collect variants and covariates")
    para("First, we’ll record your variant(s) and the covariates.")
    variants = get_variants()
    covariates = get_covariates()
    rule()

    # Module 2: Phecodes
    step(2, "Choose phecode mapping")
    para("We’ll select a Phecode version and the ICD source.")
    phecodes = get_phecodes()
    rule()

    # Module 3: PheWAS settings
    step(3, "Configure PheWAS analysis")
    para("Next, we select analysis settings (rare-events and minimum case counts).")
    phewas_settings = get_settings(phecodes, variants)

    # Final confirmation (simple Y/N)
    rule("FINAL CONFIRMATION")
    user_ok = input("Ready to start? (y/n): ")
    user_ok = validate_yes_no_response(user_ok)
    if not user_ok:
        para("Run cancelled. No computations were started.")
        rule("Goodbye")
        return

    # Execution phase
    rule("Running PheTK modules")
    get_cohort(variants, covariates)
    get_counts(phecodes)
    for settings in phewas_settings:
        run_phewas(settings)
        print("PheTK Modules complete! Congrats 🎉")


if __name__ == "__main__":
    run()
