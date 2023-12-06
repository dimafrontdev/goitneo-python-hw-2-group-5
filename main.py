def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "\033[91mPlease provide a valid name and phone number.\033[0m"
        except IndexError:
            return "\033[91mInvalid number of arguments.\033[0m"
        except KeyError:
            return "\033[91mContact not found.\033[0m"
        except Exception as e:
            return f"\033[91mUnexpected error: {e}\033[0m"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise IndexError
    name, phone = args
    contacts[name] = phone
    return "\033[92mContact added.\033[0m"


@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise IndexError
    name, new_phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = new_phone
    return "\033[92mContact updated.\033[0m"


@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name not in contacts:
        raise KeyError
    return f"\033[94m{name}'s phone number is {contacts[name]}\033[0m"


@input_error
def show_all(contacts):
    if not contacts:
        return "\033[93mNo contacts saved.\033[0m"
    return "\n".join(
        [f"\033[94m{name}: {phone}\033[0m" for name, phone in contacts.items()]
    )


def show_help():
    help_text = """
    \033[1mAvailable commands:\033[0m
    - \033[94mhello\033[0m: Greet the bot.
    - \033[92madd [name] [phone number]\033[0m: Add a new contact.
    - \033[92mchange [name] [new phone number]\033[0m: Change an existing contact's phone number.
    - \033[93mphone [name]\033[0m: Retrieve the phone number of a contact.
    - \033[93mall\033[0m: Show all saved contacts.
    - \033[95mhelp\033[0m: Show this help message.
    - \033[91mclose/exit\033[0m: Exit the program.
    """
    return help_text


def main():
    contacts = {}
    print("\033[96mWelcome to the assistant bot!\033[0m")
    while True:
        user_input = input("\033[95mEnter a command: \033[0m")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("\033[91mGood bye!\033[0m")
            break
        elif command == "hello":
            print("\033[94mHow can I help you?\033[0m")
        elif command == "help":
            print(show_help())
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("\033[91mInvalid command.\033[0m")


if __name__ == "__main__":
    main()
