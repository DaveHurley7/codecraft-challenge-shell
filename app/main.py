import sys
import os

builtin_cmds = ["echo","type","exit"]

def is_exec(command):
    path_dirs = os.environ("PATH").split(":")
    print("PATH DIRS:",path_dirs)
    for pdir in path_dirs:
        dir_files = os.listdir(pdir)
        for file in dir_files:
            if os.basename(file) == command:
                return command
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
            print("USING TYPE CMD",args)
            if args[1] in builtin_cmds:
                sys.stdout.write(args[1] + " is a shell builtin\n")
            elif execcmd := is_exec(args[1]):
                print("EXEC:",execcmd)
                sys.stdout.write(args[1] + " is " + os.path.absname(args[1]) + "\n")
            else:
                sys.stdout.write(args[1] + " not found\n")
        elif command.startswith("exit"):
            args = command.split()
            quit(int(args[1]))
        else:
            sys.stdout.write(command + ": command not found\n")

if __name__ == "__main__":
    main()
