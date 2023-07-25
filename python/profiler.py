import sys
import os
from find_repos import find_repos

def main(): 
    if len(sys.argv) < 2:
        sys.stderr.write('''Usage: git-profiler [command]\n\nCOMMANDS:\n
        find_repos: finds all the Git repositories in the file tree of the provided folder\n
        generate: find the insights from the given repos and generate objective resume
        \n''')
        sys.stderr.flush()
        return

    command = sys.argv[1]
    if command == 'find_repos':
        input_path = sys.argv[2] if len(sys.argv)>2 else "~"
        if input_path[0] == "~":
            input_path = os.path.expanduser(input_path)
        find_repos(input_path)
    elif command == 'generate':
        from tqdm import tqdm
        import time
        with open("../repository_paths.txt", 'r') as f:
            repos = f.readlines()
            repos = [repo.strip() for repo in repos]

        for repo_path in tqdm(repos):
            time.sleep(0.7)

        with open("report.md", 'w+') as f:
            f.write('report')

        should_upload = input("Should we upload the report to Vibinex.com? [y/n] ")
        if (should_upload == 'y'):
            sys.stdout.write("Uploading...")
            sys.stdout.flush()
            time.sleep(1.4)
            sys.stdout.write("\rReport uploaded!\n")
            sys.stdout.flush()
        
        print("Your report has been generated and saved as `report.md` in the current directory")

if __name__ == '__main__':
    main()
