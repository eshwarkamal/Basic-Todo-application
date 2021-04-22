import time
import sys
import os
args = sys.argv

if len(args)==1:
    print("""StringContaining "Usage :-""")
    print("""$./todo add "todo item"  # Add a new todo""")
    print("$./todo ls               # Show remaining todos")
    print("$./todo del NUMBER       # Delete a todo")
    print("$./todo done NUMBER      # Complete a todo")
    print("$./todo help             # Show usage")
    print("$./todo report           # Statistics",end="")
else:
    command = args[1]
    if command == "help":
        print("""StringContaining "Usage :-""")
        print("""$./todo add "todo item"  # Add a new todo""")
        print("$./todo ls               # Show remaining todos")
        print("$./todo del NUMBER       # Delete a todo")
        print("$./todo done NUMBER      # Complete a todo")
        print("$./todo help             # Show usage")
        print("$./todo report           # Statistics",end="")
    if command == "add":
        if len(args)==2:
            print("Error: Missing todo string. Nothing added!")
        else:
            task = args[2]
            with open("D:\\todo.txt","r") as f: 
                lines = f.readlines()
                if lines.count(task) <= 2:
                    lines.insert(0,task+"\n")
                    with open("D:\\todo.txt", "w") as f: 
                        f.writelines(lines)
                        f.close()
                    print("""Added todo: \"{0}\"""".format(str(task)),end="")
    if command == "ls":
        ls = []
        with open("D:\\todo.txt","r") as f: 
            lines = f.readlines()
            if len(lines)==0:
                print("There are no pending todos!")
            else:
                for i,j in list(zip([i for i in range(len(lines),0,-1)],[i for i in lines])):
                    ls.append("[{0}] {1}".format(i,j))
                if len(ls) != 0:
                    ls[-1] = ls[-1].replace(ls[-1][-1],"")
                    for i in ls:
                        print(i,end="")
            f.close()
    if command == "del":
        if len(args)==2:
            print("Error: Missing NUMBER for deleting todo.")
        else:
            number = int(args[2])
            with open("D:\\todo.txt","r") as f: 
                lines = f.readlines()
                lines_zip = list(zip([i for i in range(len(lines),0,-1)],[i for i in lines]))
                if number in [i for i,j in lines_zip]:
                    index_val = next((i for i, (j, ele) in enumerate(lines_zip) if j == number), None)
                    lines.remove(lines[index_val])
                    with open("D:\\todo.txt", "w") as f: 
                        f.writelines(lines)
                        f.close()
                        print("Deleted todo #{0}".format(number),end="")
                else:
                    print("Error: todo #{0} does not exist. Nothing deleted.".format(number),end="")
    if command == "done":
        if len(args)==2:
            print("Error: Missing NUMBER for marking todo as done.")
        else:
            number = int(args[2])
            with open("D:\\todo.txt","r") as f: 
                lines = f.readlines()
                lines_zip = list(zip([i for i in range(len(lines),0,-1)],[i for i in lines]))
                if number in [i for i,j in lines_zip]:
                    index_val = next((i for i, (j, ele) in enumerate(lines_zip) if j == number), None)
                    new = lines[index_val]
                    lines.remove(new)
                    with open("D:\\todo.txt", "w") as f: 
                        f.writelines(lines)
                        f.close()
                    with open("D:\\done.txt","r") as f: 
                        line = f.readlines()
                        line.insert(0,str([number])+" "+str(time.strftime("%Y-%m-%d"))+" "+new)
                    with open("D:\\done.txt", "w") as f: 
                        f.writelines(line)
                        f.close()
                    print("Marked todo #{0} as done.".format(number),end="")
                else:
                    print("Error: todo #{0} does not exist.".format(number),end="")
    if command == "report":
        with open("D:\\todo.txt","r") as f: 
            lines = len(f.readlines())
        with open("D:\\done.txt","r") as f: 
            line = len(f.readlines())
        print("{0} Pending : {1} Completed : {2}".format(time.strftime("%Y-%m-%d"),lines,line),end="")
