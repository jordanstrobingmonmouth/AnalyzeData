# AnalyzeData - Script to analyze the .txt files from GreatSPN
import tkinter as tk
from tkinter import filedialog, simpledialog
import re

# These lines open a prompt asking the user what file to open
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename() # This saves the path of the file we need to read from
# print(file_path) <- test with this
# We need to make it so it only accepts .txt, should be pretty simple but not important yet


# This reads every line of the file
with open(file_path) as f:
    lines = f.readlines()

# This writes every line of the txt to the console, just using it for testing
'''for line in lines:
    print(line)'''

# This line opens the "Save as" box. Not sure if name is necessary but it was in testing
newFile = filedialog.asksaveasfile().name

# This opens the file we want to write to, the 'w' means write. For appending, we'd use 'a' instead.
f = open(newFile, 'w')

# This loop takes all input in from the read file, exports it to the write file
# Used this for testing, will prob delete later but you might find it interesting to play with.
'''for line in lines:
    f.write(line)'''

# This saves all the times and exports them to the file
# Might be useless but it could help for reference, maybe.
# If it is useful, we can definitely clean it up
'''times = []
i = 0
for line in lines:
    for x in range(len(line)):
        if (line[x] == '@'):
            times.append(line[x:x+6])
            i += 1
for t in times:
    f.write(t + "\n")'''

# This is a pop up box to ask the user the name of the place, saves it to placeName
placeName = simpledialog.askstring(title="Place Information", prompt="Enter the name of the place you'd like to get data for: (case sensitive)")

# This loop checks if the place name entered is in each line. Can use this to help get the number.
# We can use this logic as a foundation to figuring out how to extract the numbers
for line in lines:
    if placeName in line:
        print("true")
    else:
        print("false")

# We need to close the file in order for the program to stop
f.close()