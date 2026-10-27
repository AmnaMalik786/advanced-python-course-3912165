# Example file for Advanced Python by Joe Marini
# Demonstrate the use of documentation strings


def myFunction(arg1, arg2=None):
    """myFunction(arg1, arg2 = None) --> Doesn't really do anything

    Parameters used:
    arg1: the first argument. Whatever you feel like parsing.
    arg2: the second argument. Defaults to None
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
