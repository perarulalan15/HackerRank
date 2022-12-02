records=[]
scores=[]
for i in range(int(input("Enter the no.of.students:"))):
    name = input("Enter name:")
    score = float(input("Enter score:"))
    records.append([name,score])
    scores.append(score)
b=sorted(list(set(scores)))[1]
for a,c in sorted(records):
    if c==b:
        print(a)
    
    
    
