# 8.4. Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the
# split() method. The program should build a list of words. For each word on each line, check to see if the word is
# already in the list and if not append it to the list. When the program completes, sort and print the resulting
# words in python sort() order as shown in the desired output.

fname = input("Enter file name: ")
fname = './text/romeo.txt'
fh = open(fname)
lst = list()
for line in fh:
    for word in line.split():
        if word not in lst:
            lst.append(word)

lst.sort()
#print(f'There are {len(lst)} unique words in {fname}. the words shown bellow:')
print(f'{lst}')