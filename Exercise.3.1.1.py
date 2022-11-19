#Lab 3 Exercise.1.1 1630902656 Kanokporn Hudsree
# First In first out (FIFO) 
Array_A = [ ] 
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
Array_A.pop(0) 
# A in 0 position and Pop “A” from Array_A  A in 0 position
print(Array_A) 
Array_A.pop(0) 
# position B slide to 0 and Pop “B” from Array_A  
print(Array_A) 
Array_A.pop(0) 
# position C slide to 0 and Pop “C” from Array_A 
print(Array_A) 
Array_A.pop(0) 
# position D slide to 0 and Pop “D” from Array_A 
print(Array_A)
