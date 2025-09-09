def friendship_score(name1, name2):
    name1, name2 = name1.lower(), name2.lower()
    score = 0
    shared_letters = set(name1) & set(name2)
    vowels = set('aeious')
    
    score += len(shared_letters) * 5
    score += len(vowels & shared_letters) * 10
    
    
    return min(score, 100)

def run_friendship_calculator():
    print("* Frndship comp calc")
    name1 = input("enter first name")
    name2 = input("Enter secnd name") 
    score = friendship_score(name1,name2)
    print(f"\n {score}")
    
    
run_friendship_calculator()