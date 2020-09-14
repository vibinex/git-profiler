import os
import sys
from git import Repo

def getCommitsList(repo_path, number_of_commits):
	repo = Repo(repo_path)
	commits_list = list(repo.iter_commits('master', max_count=number_of_commits))
	return commits_list

def retrieveDiffs(commits_list):
	print("Number of commits:", len(commits_list))
	number_of_commits = len(commits_list)
	i = 0
	for commit in commits_list:
		print("\t", commit.message)
		if i < number_of_commits-1:
			i+=1
			continue
		print(commit.author)
		print(commit.stats.files)

def main():
	repo_path = "../"
	number_of_commits = 47

	currDir = os.listdir(repo_path)
	print(currDir)
	commits_list = getCommitsList(repo_path, number_of_commits)
	retrieveDiffs(commits_list)

if __name__ == '__main__':
	main()