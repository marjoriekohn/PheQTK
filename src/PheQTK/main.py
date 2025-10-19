from src.PheQTK.modules.cohorts import get_cohort
from src.PheQTK.modules.phecodes import get_phecodes
from src.PheQTK.modules.phewass import run_phewass
from src.PheQTK.modules.plots import get_plots


def main():
    # 1. Cohorts & Covariates
    # TODO: ask user for their variant id(s) in a comma separated list
    raw_variants = input("Enter variant id(s): '20-13093478-G-A, 20-13091168-C-T':\n")
    cohorts = get_cohort(raw_variants)

    # 2. Phecodes
    phecodes = get_phecodes()

    # 3. PheWAS
    phewass = run_phewass()

    # 4. Plots
    plots = get_plots()


if __name__ == "__main__":
    main()
