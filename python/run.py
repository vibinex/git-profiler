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
		print(commit.size)
		diff_obj = commit.diff(commits_list[i-1])
		for ct in diff_obj.change_type:
			diff_list = list(diff_obj.iter_change_type(ct))
			print("\tNum diffs for change_type "+ct+":", len(diff_list))
			for ct_diff in diff_list:
				print(type(ct_diff))
				print(ct_diff.__str__())
				print(ct_diff.change_type, ct_diff.score)
				print(ct_diff.a_path, ct_diff.b_path)
			# break

def main():
	# repo_path = "../"
	repo_path = "/Users/apple/Work/Personal/mentorship/mentorship-website"
	number_of_commits = 47

	currDir = os.listdir(repo_path)
	print(currDir)
	commits_list = getCommitsList(repo_path, number_of_commits)
	retrieveDiffs(commits_list)

if __name__ == '__main__':
	main()