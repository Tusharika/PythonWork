row = eval(input("enter the height of tree: "))
num = 1
space = " "
tree_space = row - 1
stump = row - 1
for i in range(row):

    print (space * tree_space + ("#" * num))
    num += 2
    tree_space -= 1

print (space * stump + "#")
