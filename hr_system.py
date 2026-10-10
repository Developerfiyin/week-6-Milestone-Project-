# Open the file 


with open("hr_system.txt") as hr_file : 

# continue with comments and code to process the file

    for line in hr_file:

        part = line.split(" ")
        print(line)

        