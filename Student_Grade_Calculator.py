print("Student Grade Calculator")
print ("-------------------------")

score = float(input("Enter your score: "))
max_score = float(input("Enter your maximum score: "))

def calcualate_percentage(score,max_score):
    total = (score / max_score )*100
    return round(total)

def remaining(score , max_score):
    remaining = max_score - score
    return remaining


print(f"The total percentage  is :{calcualate_percentage(score,max_score)},"%" ")
print(f"Remaining is :{remaining(score ,max_score)}")
      
      


