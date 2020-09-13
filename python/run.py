import os
import sys
from git import Repo

def main():
	# repo_path = "../"
	repo_path = "/Users/apple/Work/Personal/mentorship/mentorship-website"
	currDir = os.listdir(repo_path)
	print(currDir)
	repo = Repo(repo_path)

	commits_list = list(repo.iter_commits('master', max_count=5))
	print("Number of commits:", len(commits_list))
	for commit in commits_list:
		print(commit.author)
		print(commit.size)
		diff_obj = commit.diff()
		for ct in diff_obj.change_type:
			diff_list = list(diff_obj.iter_change_type(ct))
			print("\tNum diffs for change_type "+ct+":", len(diff_list))

if __name__ == '__main__':
	main()