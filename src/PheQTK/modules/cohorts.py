from PheTK.Cohort import Cohort
from src.PheQTK.helpers.variant_validation import parse_variants


def get_cohort(raw_variants: str):

    # parse variants from user input
    variants = parse_variants(raw_variants)

    # show the user the variants that we read
    for variant in variants:
        print(f"The following variants have been saved: {variant}.")

    # TODO: verify user_confirmation is 'y' or 'yes' and continue asking until we get a 'n' or 'no' response
    # verify users variants are correct
    user_confirmation = input("Are your variants correct? (y/n): ")

    # if the user confirms, we build the cohorts
    if user_confirmation == "y":
        # instantiate class Cohort object for _All of Us_ database version 7
        cohort = Cohort(platform="aou", aou_db_version=7)

        # create a cohort for each variant
        for variant in variants:
            # generate cohort by genotype
            cohort.by_genotype(
                chromosome_number=int(variant[0]),
                genomic_position=int(variant[1]),
                ref_allele=variant[2],
                alt_allele=variant[3],
                case_gt=["0/1", "1/1"],
                control_gt="0/0",
                reference_genome="GRCh38",
                mt_path=None,
                output_file_name=f"{variant_id}_cohort.csv"
            )
