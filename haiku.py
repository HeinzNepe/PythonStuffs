
# Just change the code for the variables if you want to give the program a different input :-)
lineOne = "Hello world"
lineTwo = "You are looking"
lineThree = "Quite good"

# Haiku is all lines. Make your own list if you want to
haiku = [lineOne, lineTwo, lineThree]

# Length of each line of the haiku is stored here
haiku_len = []

# Finds the length of each line in the haiku
for line in haiku:
    i = int(len(line))
    haiku_len.append(i)

# Gets the longest line in the haiku
haiku_max = max(haiku_len)

# ======= PRINT THE THING ===========
# Print top header (max length plus 4)
print('@' * (haiku_max+4))

# For every line in the haiku
for line in haiku:
    # Add a space until they are all the same length
    while len(line) < haiku_max:
        line = " " + line

    # Add the border on the line, and print it
    print('@', line, '@')

# Print bottom header (max length plus 4)
print('@' * (haiku_max+4))

