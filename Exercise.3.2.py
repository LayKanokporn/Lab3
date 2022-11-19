#Lab 3 Exercise.2 1630902656 Kanokporn Hudsree
Array_A = [ ] 
Array_B = [ ] 
print(Array_A) 
Array_A.append("A") # Push “A” into Array_A 
print(Array_A) 
Array_A.append("B") # Push “B” into Array_A 
print(Array_A) 
Array_A.append("C") # Push “C” into Array_A 
print(Array_A) 
Array_A.append("D") # Push “D” into Array_A 
print(Array_A) 
Array_A.append("E") # Push “D” into Array_A 
print(Array_A) 
Array_A.append("F") # Push “D” into Array_A 
print(Array_A) 
 
# First in last out 
Array_B.append(Array_A.pop(-1)) # Pop “F” from Array_A to push Array_B 
print(Array_B) 
Array_B.append(Array_A.pop(-1)) # Pop “E” from Array_A to push Array_B 
print(Array_B) 
Array_B.append(Array_A.pop(-1)) # Pop “D” from Array_A to push Array_B 
print(Array_B) 
Array_B.append(Array_A.pop(-1)) # Pop “C” from Array_A to push Array_B 
print(Array_B) 
Array_B.append(Array_A.pop(-1)) # Pop “B” from Array_A to push Array_B 
print(Array_B) 
Array_B.append(Array_A.pop(-1)) # Pop “A” from Array_A to push Array_B 
print(Array_B) 
 
# First in first out 
Array_A.append(Array_B.pop(0)) # Pop “A” from Array_B to push Array_A 
print(Array_A) 
Array_A.append(Array_B.pop(0)) # Pop “B” from Array_B to push Array_A 
print(Array_A) 
Array_A.append(Array_B.pop(0)) # Pop “C” from Array_B to push Array_A 
print(Array_A) 
Array_A.append(Array_B.pop(0)) # Pop “D” from Array_B to push Array_A 
print(Array_A) 
Array_A.append(Array_B.pop(0)) # Pop “E” from Array_B to push Array_A 
print(Array_A) 
Array_A.append(Array_B.pop(0)) # Pop “F” from Array_B to push Array_A 
print(Array_A)
