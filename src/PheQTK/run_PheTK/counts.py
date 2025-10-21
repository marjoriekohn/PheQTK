from PheTK.Phecode import Phecode


def get_counts(phecodes):
    # instantiate PheTK Phecode class
    phecode = Phecode(platform="aou")

    # generate phecode counts
    phecode.count_phecode(
        phecode_version=phecodes.phecode_version,
        icd_version=phecodes.icd_version,
        phecode_map_file_path=phecodes.phecode_map_file_path,
        output_file_name=phecodes.output_file_name
    )
