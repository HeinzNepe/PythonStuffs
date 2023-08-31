lineOne = "Hello world"
lineTwo = "You are looking"
lineThree = "Quite good"

# Haiku is all lines
haiku = [lineOne, lineTwo, lineThree]
haiku_len = []

# Finds the lenght of each line in the haiku
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

