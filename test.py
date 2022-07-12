EXIT = "100".encode("utf-8", 'strict')
DECODED_EXIT = EXIT.decode("utf-8", 'strict')
RECODED_EXIT = DECODED_EXIT.encode("utf-8")
print(EXIT)
print(EXIT.decode("utf-8"))

VARIABLE = '100'

if(EXIT == DECODED_EXIT):
    print("yes")
if(RECODED_EXIT == EXIT):
    print("no")
if(DECODED_EXIT == VARIABLE):
    print("derp")