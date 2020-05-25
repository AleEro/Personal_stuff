# This script is created to detect twin copied books in different directory's
import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
current_path = filedialog.askdirectory()

dir_list = {}


print('current_path:', current_path)
# r-root d-directory f-file
for r,d,f in os.walk(current_path):
    books_list = []
    dir_list[r] = []
    for file in f:
        for i in dir_list:
            if file in dir_list[i]:
                print(r + '\\' + file)
                print(i + '\\' + file)

        if file not in dir_list[r]:
            dir_list[r].append(file)
