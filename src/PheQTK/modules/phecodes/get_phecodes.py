from PheQTK.modules.phecodes.Phecodes import Phecodes


def get_phecodes() -> Phecodes:

    # instantiate Phecodes object
    phecodes = Phecodes()

    # print default settings
    print(f"{phecodes}")

    # TODO: implement user input for unique preferences

    return phecodes


