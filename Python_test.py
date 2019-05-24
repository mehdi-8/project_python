import pandas

# import file
file = open(r"C:\Users\RBELMEHDI\Desktop\test.txt")
# read file
content = file.read()
if len(content) == 0:
    print("THE FILE IS EMPTY")
else:
    print("THE FILE IS NOT EMPTY")
   
file.close
 
    