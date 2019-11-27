

def get_choice_from_cli(options,
                        repeat_until_correct=True,
                        return_key=False,
                        title="Select one option from the list:",
                        prompt="Selection > ",
                        redo_text="Not a valid selection, try again."):
    """ lets the user choose one option from the passed list.

    :param options: A list of options, which are three item tuples with [0]=index, [1]=description/name, [2]=object
        The index needs to be convertible to string and printable.
        The description/name needs to be printable.
        The object doesn't have any requirements on it's type.
    :param repeat_until_correct: If True: keeps checking until valid option is selected.
        If False: faulty option key is returned regardless of value of return_key.
    :param return_key: If true the index for the selected option is returned instead of the third item in the tuple.
    :param title: The title shown above the option list. (Pass None for no title)
    :param prompt: The prompt shown below the option list. (Pass None for no prompt(just a new line))
    :param redo_text: The text shown when a invalid option is chosen and infinite is set (pass None for no redo text)
    :return: The callback that is chosen, or the given key if return_key is set
    """
    desired_pad_length = max([len(str(a[0])) for a in options])
    while True:
        if title is not None:
            print(title)

        for option in options:
            print("{}\t{}".format(str(option[0]).ljust(desired_pad_length), option[1]))
        choice = input(prompt or "")

        for option in options:
            if choice == str(option[0]):
                if return_key:
                    return choice
                else:
                    return option[2]
        # choice not in the list
        if repeat_until_correct:
            if redo_text is not None:
                print(redo_text)
            continue
        else:
            return choice
