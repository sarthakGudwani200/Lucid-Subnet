cd /c/Users/jum/Lucid-Subnet
export GIT_COMMITTER_NAME=get-lucid
export GIT_COMMITTER_EMAIL=pinionagent714@gmail.com
export GIT_AUTHOR_NAME=get-lucid
export GIT_AUTHOR_EMAIL=pinionagent714@gmail.com
git add -A
git commit -m "initial subnet structure"
git branch -M main
git push -u origin main
rm -f push.sh
