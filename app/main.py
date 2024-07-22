import sys


def main():
    # Uncomment this block to pass the first stage
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
    # Wait for user input
        command = input()
        if command.startswith("echo"):
            args = command.split(maxsplit=1)
            sys.stdout.write(args[1] + "\n")
        elif command.startswith("exit"):
            args = command.split()
            quit(int(args[1]))
        else:
            sys.stdout.write(command + ": command not found\n")

if __name__ == "__main__":
    main()
