import re
from src.PheQTK.classes.Variant import Variant


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


def parse_variants(raw_input: str) -> list[Variant]:
    variants: list[Variant] = []
    seen_variants = set()

    for raw_variant in raw_input.split(","):
        verified_variant = VARIANT_PATTERN.match(raw_variant)
        if not verified_variant:
            raise ValueError(
                f"Bad variant format: '{raw_variant}'. Expected: chromosome-position-reference-alternate (e.g. 20-13093478-G-A)"
            )
        chrom = int(verified_variant.group("chrom"))
        pos = int(verified_variant.group("pos"))
        ref = verified_variant.group("ref").upper()
        alt = verified_variant.group("alt").upper()

        variant = Variant(chrom, pos, ref, alt)
        if variant not in seen_variants:
            variants.append(variant)
            seen_variants.add(variant)
    if not variants:
        raise ValueError("No valid variants parsed.")
    return variants
