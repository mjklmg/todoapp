a cli todo app made with python as a learning project

https://roadmap.sh/projects/task-tracker

installation:
1. clone the repository 
git clone https://github.com/mjklmg/todoapp.git
cd /todo-cli

2. install the package
pip install

3. run the cli
todoapp ...


example:
todoapp add "My first task"
todoapp list
todoapp update 1 "Updated task title"
todoapp mark-in-progress 1
todoapp list --status in-progress
todoapp mark-done 1
todoapp del 1
