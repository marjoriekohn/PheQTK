from dataclasses import dataclass


@dataclass(frozen=True)
class Variant:
    chromosome: int
    position: int
    ref_allele: str
    alt_allele: str

    @property
    def name(self) -> str:
        return f"{self.chromosome}_{self.position}_{self.ref_allele}_{self.alt_allele}"
