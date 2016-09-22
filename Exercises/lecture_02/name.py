text = input("Enter first text: ")

params = text.split()
initial = ""
for name in params:
    if name[0].isupper():
        initial += name[0] + "."
print(initial)

# txt = "|                 a ||||||||||||"
# print(txt.strip("|"))