import os
from collections import defaultdict
from repository_profiler import RepositoryProfiler

def main():
	with open("../repository_paths.txt", 'r') as f:
		repos = f.readlines()
		repos = [repo.strip() for repo in repos]

	with open("../user_emails.txt", 'r') as f:
		user_emails = f.readlines()
		user_emails = [email.strip() for email in user_emails]

	profile = defaultdict(int)
	for repo_path in repos:
		print(repo_path)
		profiler = RepositoryProfiler(repo_path)
		profiler.addUserEmails(user_emails)
		repo_profile = profiler.getProfile()
		for lang in repo_profile:
			profile[lang] += repo_profile[lang]

	for l in profile:
		print(l, profile[l])

if __name__ == '__main__':
	main()