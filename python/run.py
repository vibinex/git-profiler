import os
from profiler import Profiler

def main():
	with open("../repository_paths.txt", 'r') as f:
		repos = f.readlines()
		repos = [repo.strip() for repo in repos]

	with open("../user_emails.txt", 'r') as f:
		user_emails = f.readlines()
		user_emails = [email.strip() for email in user_emails]

	for repo_path in repos:
		print(repo_path)
		profiler = Profiler(repo_path)
		profiler.addUserEmails(user_emails)
		profiler.getProfile()
		# break

if __name__ == '__main__':
	main()