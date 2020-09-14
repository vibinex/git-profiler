import subprocess
import os
import sys

def find_repos(root):
	relative_path = os.path.relpath(root, os.curdir)
	bash_cmd = "find "+relative_path+" -name .git -type d -prune"
	process = subprocess.Popen(bash_cmd.split(), stdout=subprocess.PIPE)
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
	find_repos(os.path.expanduser("~"))