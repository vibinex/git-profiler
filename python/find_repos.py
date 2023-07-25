import subprocess
import os
import sys

def find_repos(root):
    relative_path = os.path.relpath(root, os.curdir)
    bash_cmd = "find relative_path -name .git -type d -prune".split()
    bash_cmd[1] = relative_path
    process = subprocess.Popen(bash_cmd, stdout=subprocess.PIPE)
    output, error = process.communicate()
    error = None
    if error == None:
        repository_paths = output.decode("utf-8").split()
        repository_paths = [os.path.abspath(p[:p.rindex("/")]) for p in repository_paths]
        repository_paths = "\n".join(repository_paths)
        with open("../repository_paths.txt", "w+") as f:
            f.write(repository_paths)
    else:
        print(error, file=sys.stderr)

if __name__ == '__main__':
    input_path = sys.argv[1] if len(sys.argv)>1 else "~"
    if input_path[0] == "~":
        input_path = os.path.expanduser(input_path)
    find_repos(input_path)
