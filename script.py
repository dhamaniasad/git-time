from git import Repo
from datetime import timedelta


branch=raw_input("Which branch?: ")

repo = Repo(".")
commit_time = []
all_commits = list(repo.iter_commits(branch))
previous_time = 0
differences = []
for commit in all_commits:
	this_time = commit.committed_date
	if not previous_time == 0:
		difference = previous_time - this_time
		differences.append(difference)
	previous_time = this_time
average_time = sum(differences) / float(len(differences))
print("Average time between commits: {}".format(timedelta(seconds=average_time)))
