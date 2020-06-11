# 清除历史记录(慎用) 

```Shell
git checkout --orphan latest_branch
git add -A
git commit -am "clear git history"
git branch -D master
git branch -m master
git push -f origin master
```
