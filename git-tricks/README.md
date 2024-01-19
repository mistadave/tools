# Git Tips and Tricks

## Add new Branch from Forked

You forked a repository from original/abc. 
Now you'd like to add a new branch to your fork form the original. You'll accomplish this by doing the following:

```bash
# 1. Add Remote pointing to original/abc:

git remote add upstream https://github.com/original/abc.git

# 2. Fetch the repository Original:

git fetch upstream

# 3. Checkout the branch from the original/abc remote:

git checkout upstream/new-branch
# Branch is now in "detached HEAD" state.

# 4. Create local branch:

git checkout -b new-branch

# 5. Push to your remote:

git push -u origin new-branch
```
