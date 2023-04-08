input_str = input ("What is your input string?")
output_str = ""

for i in range (len(input_str)):

    if input_str[i] == "*":
        output_str += "a"
        
    elif input_str[i] == "&":
        output_str += "e"
        
    elif input_str[i] == "#":
        output_str += "i"
        
    elif input_str[i] == "+":
        output_str += "o"
        
    elif input_str[i] == "!":
        output_str += "u"
    else:
        output_str += input_str[i]
        
print(output_str)