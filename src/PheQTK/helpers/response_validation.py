
# TODO: update this to use regex
def validate_yes_no_response(response):
    response = response.lower()

    if response == "y" or response == "yes":
        return True
    elif response == "n" or response == "no":
        return False
    else:
        raise ValueError("Invalid response. Please enter 'y' or 'n'.")


# TODO: update this to use regex?
def validate_int_response(response):
    try:
        int(response)
        return int(response)
    except ValueError:
        raise ValueError("Invalid response. Please enter an integer.")
