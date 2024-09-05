import sys
first_line = sys.stdin.readline().rstrip()
item_num = int(first_line[0])
max_weight = int(first_line[1])
for i in range(item_num):
    item_attr = sys.stdin.readline().rstrip()
    item_weight = int(item_attr[0])
    item_value = int(item_attr[1])
