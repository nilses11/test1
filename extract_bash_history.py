import sys

file = open(sys.argv[1], 'r')

dict = {}

for line in file:
    dict[line] = 1

file2 = open('result' , 'w')
file2.writelines(dict.keys())



