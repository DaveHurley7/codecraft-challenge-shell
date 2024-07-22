import sys
import os
import subprocess

builtin_cmds = ["echo","type","exit","pwd"]

def is_exec(command):
    path_dirs = os.environ["PATH"].split(":")
    for pdir in path_dirs:
        if os.path.isdir(pdir):
            dir_files = os.listdir(pdir)
            for file in dir_files:
                if file == command:
                    return pdir + "/" + file
    return None

def exec_with_args(command):
    prog, *args = command.split()
    prog_path = is_exec(prog)
    return [prog_path, *args] if prog_path else None

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
        elif command.startswith("pwd"):
            sys.stdout.write(os.getcwd() + "\n")
        elif command.startswith("type"):
            args = command.split()
            if args[1] in builtin_cmds:
                sys.stdout.write(args[1] + " is a shell builtin\n")
            elif execpath := is_exec(args[1]):
                sys.stdout.write(args[1] + " is " + execpath + "\n")
            else:
                sys.stdout.write(args[1] + ": not found\n")
        elif command.startswith("exit"):
            args = command.split()
            quit(int(args[1]))
        elif cmd := exec_with_args(command):
            subprocess.run(cmd)
        else:
            sys.stdout.write(command + ": command not found\n")

if __name__ == "__main__":
    main()
