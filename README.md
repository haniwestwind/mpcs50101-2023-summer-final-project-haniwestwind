To make this program an executable, one can simply add the following line to the ~/.bash_profile file.

export PATH="{ToDoAppDirectory}:$PATH"

Additionally, you need to change the permission of the python file with the following command.

sudo chmod +x todo.py

After updating the file, reopen a terminal and run your program like below.
todo.py --list 

Notice that you don't need to call python explicitly anymore.