For using the .gitignore :-


 #folder_name/
 #folder1/
 #folder2/
 #temp/
 #logs/       --------Folder's
 
 node_modules/
 # Files with any particular extension
 *.json
 # any particular file say ex: package.json.



Action	 	Command
Create branch	git checkout -b <branch-name>
Push branch	git push -u origin <branch-name>
Merge branch	git checkout main && git merge <branch>
Delete local	git branch -d <branch-name>
Delete remote	git push origin --delete <branch-name>
