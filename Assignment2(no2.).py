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


Message = input("Message:")
key = input("keyword:")

Message_num = [ord(c) - 65 for c in Message]
key_num = [ord(c) - 65 for c in key]

key_rep = []
key_num = 0

for i in range(len(Message)):
  key_rep.append(key_num[key_index])
  key_index = (key_index + 1) % len(key)

  ciphertext_num = []
  for i in range(len(Message)):
    mn = Message_num[i]
    kr = key_rep[i]
    ciphertext_num.append((mn + kr) % 26)

    ciphertext = ''
    for c in ciphertext_num:
      ciphertext += chr(c + 65)

print("\n", "\033[4m"+"\033[1;36m"+ciphertext)
