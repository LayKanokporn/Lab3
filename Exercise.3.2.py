#Lab 3 Exercise.2 1630902656 Kanokporn Hudsree
Array_A = [ ] 
Array_B = [ ] 
print(Array_A) 
Array_A.append("A")
 # append “A” into Array_A  in 0 position
print(Array_A) 
Array_A.append("B")
 # append “B” into Array_A  in 1 position
print(Array_A) 
Array_A.append("C")
 # append “C” into Array_A in 2 position
print(Array_A) 
Array_A.append("D") 
# append “D” into Array_A in 3 position
print(Array_A) 
Array_A.append("E") 
# append “E” into Array_A in 4 position
print(Array_A) 
Array_A.append("F") 
# append “F” into Array_A in 5 position
print(Array_A) 
 
# First in last out 
Array_B.append(Array_A.pop(-1))# position -1 pop out F  to push Array_B 
print(Array_B) 
Array_B.append(Array_A.pop(-1))# position -1 pop out E  to push Array_B 
print(Array_B) 
Array_B.append(Array_A.pop(-1))# position -1 pop out D  to push Array_B 
print(Array_B) 
Array_B.append(Array_A.pop(-1))# position -1 pop out C  to push Array_B 
print(Array_B) 
Array_B.append(Array_A.pop(-1)) # position -1 pop out B  to push Array_B 
print(Array_B) 
Array_B.append(Array_A.pop(-1)) # position -1 pop out A  to push Array_B 
print(Array_B) 
 
# First in first out 
Array_A.append(Array_B.pop(0)) # Pop “F” position   0 and Pop “B” from Array_B to push Array_A 
print(Array_A) 
Array_A.append(Array_B.pop(0)) # Pop “E” position   0 and Pop “B” from Array_B to push Array_A  
print(Array_A) 
Array_A.append(Array_B.pop(0)) # Pop “D” position   0 and Pop “B” from Array_B to push Array_A 
print(Array_A) 
Array_A.append(Array_B.pop(0)) # Pop “C” position   0 and Pop “B” from Array_B to push Array_A  
print(Array_A) 
Array_A.append(Array_B.pop(0)) # Pop “B” position   0 and Pop “B” from Array_B to push Array_A 
print(Array_A) 
Array_A.append(Array_B.pop(0)) # Pop “A” position   0 and Pop “B” from Array_B to push Array_A 
print(Array_A)
