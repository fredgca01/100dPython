
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]*2

def cipher(shift,msg):
    ciphered_msg=[]
    for letter in msg:
        if(alphabet.count(letter.lower())==0):
            ciphered_msg.append(letter)
        else:
            index = alphabet.index(letter.lower())   
            ciphered_msg.append(alphabet[index+shift])
    return "".join(ciphered_msg)

decoding=True

while (decoding):
    way = input("Type encode to cipher or decode to uncipher: ")
    message = input("Give your message: ")
    shift_nb = input("Give the shift number: ")
    if(int(shift_nb)>len(alphabet)):
        shift_nb=int(shift_nb)%26
    if(way=="encode"):
        data = cipher(int(shift_nb),message)
    elif(way=="decode"):
        data = cipher(-int(shift_nb),message)
    print(f"Here is the message : {data} \n")
    answer = input("Do you want to continue ? (yes/no): ")
    if(answer!="yes"):
        decoding=False