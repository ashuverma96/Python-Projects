import textwrap

name = input("Enter the name: ").strip()
profession = input("Enter the profession: ").strip()
passion = input("Enter the passion in one line: ").strip()
emoji = input("Enter your fav emoji: ").strip()
website = input("Enter your website: ").strip()

print("\n choose your style:")
print("1. Simple Lines")
print("2. Vertical flair ")
print("3 Emoji sandwich ")

style = input("Enter 1, 2 or 3: ").strip()



def generate_bio(style):
    if style == "1":
        return f"{emoji} {name} | {profession} \n {passion} \n {website}"
    
    elif style == "2":
        return f"{emoji} {name}\n {profession}\n {passion}\n {website} "
    
    elif style =="3":
        return f"{emoji*3}\n {name} - {profession}\n {passion} \n {website} \n {emoji*3}"
    
bio = generate_bio(style)

print("\nYou stylish bio:\n")
print("*" * 50)
print(textwrap.dedent(bio))
print("*" * 50)
    
save = input("Do you want save this in text file? Y or N").lower()

if save =='y':
    filename= f"{name.lower().replace('','_')}_bio.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(bio)
    print("File save")