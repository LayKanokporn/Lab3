#Lab 3 Exercise.3 1630902656 Kanokporn Hudsree
Operators = set(['+', '-', '*', '/', '(', ')', '^' , ','])  # เซต  Operators 
Priority = {'+':1, '-':1, '*':2, '/':2, ',':0} # เซตความสำคัญของ Operator 
def Postfix(equations):  
    Opstack = [] # initialization of empty stack 
    output = ''  
    for character in equations: 
        if character not in Operators:  # ถ้าไม่ใช่ Operators เอา character to output 
            output += character 
        elif character=='(':  # ถ้าเป็น Operators push to stack 
            Opstack.append('(') 
        elif character==')': 
            while Opstack and Opstack[-1]!= '(': 
                output+=Opstack.pop() 
            Opstack.pop() 
        else:  
            while Opstack and Opstack[-1]!='(' and Priority[character]<=Priority[Opstack[-1]]: 
                output+=Opstack.pop() 
            Opstack.append(character) 
        if character is str(","): 
            Opstack.pop(0) 
             
    while Opstack: 
        output+=Opstack.pop() 
    return output 
 
equations = "A+B, A-B, A+B-C, A*B, (A+B)*C, A*(B+C)" 
print("infix: ",equations) 
print('postfix: ',Postfix(equations))
