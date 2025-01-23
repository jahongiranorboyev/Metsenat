def generate_choices(enum_class):
    """
    Generate choices for a Django model field from an Enum class.

    :param enum_class: Enum class containing the choices
    :return: List of tuples for Django field choices
    """
    return [(item.value, item.name.capitalize()) for item in enum_class]