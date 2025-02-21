# Write a function that checks if the passed parameter is a valid URL or not.
# Please also explain your reasoning. Use only the concepts that we learned in class.
# Do not use any imports

def is_valid_url(url):
    """
    Checks if the given parameter is a valid URL based on basic rules
    :param url: the input string to check
    :return: True if it is a valid URL, False otherwise
    """
    # check if it starts with "https://", or "www"
    if not (url.startswith("https://") or url.startswith("http://") or url.startswith("www")):
        return False

    # check if it contains at least one dot "."
    if "." not in url:
        return False

    # check if it contains spaces (not valid in a URL)
    if " " in url:
        return False

    # if all conditions are met, it is a valid URL
    return True


print(is_valid_url("https://google.com"))
print(is_valid_url("https:// google.com"))
