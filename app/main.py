import sys

builtin_cmds = ["echo","type","exit"]

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
        elif command.startswith("type"):
            args = command.split()
            if args[1] in builtin_cmds:
                sys.stdout.write(args[1] + " is a shell builtin\n")
            else:
                sys.stdout.write(args[1] + " not found\n")
        elif command.startswith("exit"):
            args = command.split()
            quit(int(args[1]))
        else:
            sys.stdout.write(command + ": command not found\n")

if __name__ == "__main__":
    main()
