import sys
import os
args = sys.argv
command = args[1]

if command == 'add':
    if len(args)==2:
        print("Error: Missing todo string. Nothing added!")
    else:
        task = args[2]
        with open("D:\\todo.txt","r") as f: 
            lines = f.readlines()
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