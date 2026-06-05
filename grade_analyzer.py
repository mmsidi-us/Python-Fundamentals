scores = [88, 45, 92, 67, 73, 95, 81, 56, 78, 100, 62, 85, 90, 38, 71]
print(scores)
a = 0
b = 0
c = 0
d = 0
f = 0
e = 0
t = 0

for score in scores:
    e+=1
    t+=score
    if score >= 90:
        print(f"{score} is A")
        a+=1
    elif score >= 80:
        print(f"{score} is B")
        b+=1
    elif score >= 70:
        print(f"{score} is C")
        c+=1
    elif score >= 60:
        print(f"{score} is D")
        d+=1
    else:
        print(f"{score} is F")
        f+=1
        
print(f"{a} students have A")
print(f"{b} students have B")
print(f"{c} students have C")
print(f"{d} students have D")
print(f"{f} students have F")
print(f"{e} students have score")
print(f"{t} is the total of scores")
av = t/e
print(f"{av:.1f} is the average of scores")

highest_score = scores[0]
for score in scores:
    if score > highest_score:
        highest_score = score
print(f"the highest score is {highest_score}")

lowest_score = scores[0]
for score in scores:
    if score < lowest_score:
        lowest_score = score
print(f"the lowest score is {lowest_score}")

p = 0
l = 0
for score in scores:
    if score >= 60:
        p += 1
    else:
        l += 1
print(f"passing: {p} {p*100/e}%")
print(f"failing: {l} {f*100/e}%")
# Uses a while loop to let the user enter additional scores. After each entry, display the updated average. Stop when the user types "done".
add = ""
while add != "done":
    add = input("Enter additional score (or type 'done'): ")
    
    if add == "done":
        break
        
    score = int(add)
    scores.append(score)
    
    average = sum(scores) / len(scores)
    print(f"Updated average: {average:.2f}")

print("\nFinal scores list:", scores)


