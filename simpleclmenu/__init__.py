from simpleclmenu.menu import get_choice_from_cli


if __name__ == "__main__":
    """ Example usage:
    """

    # noinspection PyListCreation
    options = [
        (1, "Option 1", "Some object"),
        (2, "Option 2", "another object"),
        ("text", "It even works for methods", get_choice_from_cli),
        ("q", "And numbers", 123),
        ("What an incredibly long example right here. Wow.  ", "Look how it is all lined up neatly!", 123),
    ]
    print(get_choice_from_cli(options))

