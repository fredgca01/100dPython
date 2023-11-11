abbreviations = {"sp":" ", "bS":"\\", "sQ":"'", "nl":"\n"}

code="1sp 1/ 1bS 1_ 1/ 1bS nl 1( 1sp 1o 1. 1o 1sp 1) nl 1sp 1> 1sp 1^ 1sp 1< nl 2sp 3|"

def decode_chunk(chunk):
    decimal_index=0
    while len(chunk)>decimal_index and chunk[decimal_index].isnumeric():
        decimal_index+=1
    if decimal_index==len(chunk):
        decimal_index-=1
    return decimal_index

def translate_chunk(chunk, repeat):
    code=chunk[repeat:]
    if repeat>0:
        for i in range(int(chunk[:repeat])):
            if code in abbreviations:
                print(abbreviations[code], end="")
            else:
                print(code, end="")
    else:
        if code in abbreviations:
            print(abbreviations[code], end="")
        else:
            print(code, end="")


for chunk in code.split(" "):
    repeat = decode_chunk(chunk)
    translate_chunk(chunk, repeat)
        