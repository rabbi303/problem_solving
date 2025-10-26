
#Find the longest word in the list

names = ["Rahim", "rahman", "Chowdhuri"]

new_name = ""

for i in names:
    if len(i) > len(new_name):
        new_name = i 
print(f'The big word is -> {new_name} , and the that is -> {len(new_name)}')