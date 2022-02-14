# AnalyzeData - Script to analyze the .txt files from GreatSPN
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import re
from easygui import *
from easygui import *

# These lines open a prompt asking the user what file to open
root = tk.Tk()
root.withdraw()
root.geometry("100x100")
file_path = filedialog.askopenfilename() # This saves the path of the file we need to read from
if file_path[-4:] != '.txt':
    messagebox.showerror("Error", "This program only accepts files with the .txt extension, quitting now...")
    exit(1)


# This reads every line of the file
with open(file_path) as f:
    lines = f.readlines()

# This writes every line of the txt to the console, just using it for testing
'''for line in lines:
    print(line)'''

# This is a pop up box to ask the user the name of the place, saves it to placeName
placeName = simpledialog.askstring(title="Place Information", prompt="Enter the name of the place you'd like to get data for: (case sensitive)",)
placeName = placeName + '='

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

# This loop checks if the place name entered is in each line. Can use this to help get the number.
# We can use this logic as a foundation to figuring out how to extract the numbers
'''for line in lines:
    if placeName in line:
        print("true")
    else:
        print("false")'''

# question = tk.messagebox.askquestion("Menu option","Do you want every line that " + placeName[:-1] + " appears in? (Press no just to show instances where the number has changed)")

msg = "Select one of the two options"
title = "Options"
choices = ["Option 1: Export all instances of " + placeName[:-1],
           "Option 2: Only export when " + placeName[:-1] + " changes in state"]
choice = choicebox(msg, title, choices)

# This makes it so that the only thing that prints is the place chosen and how many tokens it has
# Tracks place as long as it has 1 or more tokens
# For later, need to get the times to show up and concatenate them (done)
ind = 0
lastChange = ""
n = "n"
for line in lines:
    if placeName in line:
        if re.search(r'\s%s.*[^,]*' % placeName, line):
            n = re.search(r'\s%s.*[^,]*' % placeName, line)
            t = re.search(r'@.*[^\s]*', line)
            n.group()
            t.group()
            head, sep, tail = n.group().partition(',')
            timehead, timesep, timetail = t.group().partition(' ')
            ind = line
            if choice == choices[0]:
                # Code for repeats:
                f.write(timehead[1:] + " " + head + "\n")
                #print(timehead + " " + head + "\n")
            # This is code to not have repeats, but we might want repeats
            else:
                if lastChange != head:
                    f.write(timehead[1:] + " " + head + "\n")
                    #print(timehead + " " + head + "\n")
                    lastChange = head
        #if re.search(r'\s%s.*=[^,]*' % placeName, line):
            #ind = line

# The [:-1] prints all the characters of placeName except the last one, because '=' is the last char
# The try and except is to negate the bounds error when a state hasn't changed at the last line
try:
    f.write("First line where " + placeName[:-1] + " is either empty or no longer changed: ")
    f.write(lines[lines.index(ind)+1])
    #print("First line where " + placeName[:-1] + " is either empty or no longer changed: ")
    #print(lines[lines.index(ind)+1])
except:
    f.write("First line where " + placeName[:-1] + " is either empty or no longer changed: ")
    f.write(lines[lines.index(ind)])
    #print("First line where " + placeName[:-1] + " is either empty or no longer changed: ")
    #print(lines[lines.index(ind)])

# We need to close the file in order for the program to stop
f.close()