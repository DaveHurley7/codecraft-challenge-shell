import sys
import os

builtin_cmds = ["echo","type","exit"]

def is_exec(command):
    path_dirs = os.environ["PATH"].split(":")
    for pdir in path_dirs:
        if os.path.isdir(pdir):
            dir_files = os.listdir(pdir)
            for file in dir_files:
                if file == command:
                    print(command)
                    print(os.absname(command))
                    return os.absname(command)
    print("PATH NOT FOUND")
    return None

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
                print("BUILT IN")
                sys.stdout.write(args[1] + " is a shell builtin\n")
            elif execpath := is_exec(args[1]):
                print("EXEC:",args[1])
                sys.stdout.write(args[1] + " is " + execpath + "\n")
            else:
                print("NONE")
                sys.stdout.write(args[1] + " not found\n")
        elif command.startswith("exit"):
            args = command.split()
            quit(int(args[1]))
        else:
            sys.stdout.write(command + ": command not found\n")

if __name__ == "__main__":
    main()
