# git-profiler
By running this project, a user can create a profile README file showing the languages (and frameworks) that he/she contributes most in. This will be displayed in the form of visualizations similar to GitHub's own profile illustrations (eg. timeline heatmap)

## Strategy
We want to support various frameworks for easy integration everywhere. We are starting with Python3 and NodeJS.

In each framework, we will create the project in two modules:
1. `core`
2. `ui`

The `core` module will be the exportable module which is provided the address of the `.git` folder for all the repositories that need to be scanned.

The `ui` module will help any user to use the core module with their cloud `git` repositories, located in *GitHub*, *GitLab*, *BitBucket* etc.

### core
1. Get commits from `.git`
2. For each commit, get all file-changes and map it to the programming language or framework to which it belongs
3. Store this mapping from "commits to language/framework wise number of file-changes"
4. Provide functions to visualize and export this information
5. Provide function to create a README.md file for the user which has contribution language distribution and day-wise heatmap colored by the most used technology in his/her contributions

### ui
The overall idea is to clone all the repositories or locate them locally and then utilize the `core` module to generate the visualizations and README.md.
#### Github
As an output, we can create a repository by the same name as the user's github-id and add the generated README.md file in that repository.