

def get_choice_from_cli(options,
                        repeat_until_correct=True,
                        return_key=False,
                        title="Select one option from the list:",
                        prompt="Selection > ",
                        redo_text="Not a valid selection, try again."):
    """ lets the user choose one option from the passed list.

    :param options: A list of options, which are three item tuples with [0]=index, [1]=name, [2]=callback
    :param repeat_until_correct: Keeps checking until valid option is selected if True.
        (If not faulty option key is always returned regardless of return_key)
    :param return_key: If true the index for the selected option is returned.
    :param title: The title shown above the option list.
    :param prompt: The prompt shown below the options list.
    :param redo_text: The text shown when a invalid option is chosen and infinite is set (pass None for no redo text)
    :return: The callback that is chosen, or the given key if return_key is set
    """
    desired_pad_length = max([len(str(a[0])) for a in options])
    while True:
        print(title)
        for option in options:
            print("{}\t{}".format(str(option[0]).ljust(desired_pad_length), option[1]))

        choice = input(prompt)

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
