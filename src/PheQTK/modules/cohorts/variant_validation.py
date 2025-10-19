import re
from src.PheQTK.modules.cohorts.Variant import Variant
from src.PheQTK.helpers.response_validation import validate_yes_no_response


VARIANT_PATTERN = re.compile(
  r"""^\s*
    (?P<chrom>[1-9]|1[0-9]|2[0-2])
    -
    (?P<pos>[1-9]\d{0,8})
    -
    (?P<ref>[ACGT])
    -
    (?P<alt>[ACGT])
    \s*$""",
  re.IGNORECASE | re.VERBOSE
)


def get_variants() -> set[Variant]:
    variants: set[Variant] = set()

    raw_variants = input("Enter variant id(s): 20-13093478-G-A, 20-13091168-C-T\n")

    for raw_variant in raw_variants.split(","):
        variant = VARIANT_PATTERN.match(raw_variant)
        if not variant:
            raise ValueError(
                f"Bad variant format: '{raw_variant}'. Expected: chromosome-position-reference-alternate (e.g. 20-13093478-G-A)"
            )
        chrom = int(variant.group("chrom"))
        pos = int(variant.group("pos"))
        ref = variant.group("ref").upper()
        alt = variant.group("alt").upper()
        cohort_file = f"{raw_variant}.csv"
        covariate_file = f"{raw_variant}_covariates.csv"

        new_variant = Variant(raw_variant, chrom, pos, ref, alt, cohort_file, covariate_file)
        variants.add(new_variant)

        # show the user the variants that we read
        print("The following variants were read:")
        for variant in variants:
            print(f"{variant}")

        # verify variants are correct before building cohorts
        user_confirmation = input("Is this information correct? (y/n): ")
        confirmation = validate_yes_no_response(user_confirmation)

        # TODO: verify user_confirmation is 'y' or 'yes' and continue asking until we get a 'n' or 'no' response
        # if the user confirms, we return the variants to the get_cohort function
        if not confirmation:
            print("Exiting...")
            exit()
            # TODO: implement exit logic so the user can try again

    return variants
