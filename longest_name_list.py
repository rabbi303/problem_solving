
#Find the longest name in the list


names = ["Rahim", "rahman", "Chowdhuri"]

new_name = ""

for i in names:
    if len(i) > len(new_name):
        new_name = i 
print(new_name , len(new_name))
'''
#or
'''names = ["Rahim", "Chowdhuri", "rahman"]

new_name = max(names ,  key=len)
print(new_name, len(new_name))