from menu import get_choice_from_cli


if __name__ == "__main__":
    """ Example usage:
    """
    def client_run():
        print("Client run")

    def server_run():
        print("Server run")

    import sys

    choice = get_choice_from_cli([
        (1, "Run as Client", client_run),
        (2, "Run as Server", server_run),
        ('q', "Quit", sys.exit),
    ])

    choice()

