#! /usr/bin/env python3
import os
import datetime

# boolean = os.path.getmtime("file2.txt")
# time = datetime.datetime.fromtimestamp(boolean )
# print(os.path.abspath("file2.txt"))
# print(time)


os.rmdir("/reading/new_dir/new_sub_dir")
os.mkdir("/reading/new_dir/new_sub_dir")
print(os.listdir("new_dir"))
print(os.getcwd())