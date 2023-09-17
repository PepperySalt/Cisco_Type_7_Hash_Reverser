def reverse_hash(hashed_pw):
    xlat = list("dsfd;kfoA,.iyewrkldJKDHSUBsgvca69834ncxv9873254k;fg87")
    hashed_pw = list(hashed_pw)
    clear_pw = [-1] * (len(hashed_pw)//2 - 1)

    val = 0

    if(len(hashed_pw)%2 != 0):
        print("ERROR : incorrect encrypted password format due to odd lenght")
        return -1


    seed = (int(hashed_pw[0])) * 10 + int(hashed_pw[1])

    if(seed > 15 or not(hashed_pw[0].isnumeric()) or not(hashed_pw[0].isnumeric()) ):
        print("ERROR : incorrect encrypted password format due to the first two characters being wrong")
        return -1


    for i in range(2,len(hashed_pw)+1,1):

        if(i != 2 and i%2 == 0):
            clear_pw[i//2 - 2] = chr( val ^ ord(xlat[seed]) )
            seed += 1
            val = 0

        if(i != len(hashed_pw)):
            val *=  16

            if hashed_pw[i].isnumeric() : 
                val += int(hashed_pw[i])
            else:
                hashed_pw[i] = hashed_pw[i].upper()
                c = hashed_pw[i]
                if ord(c) >= ord('A') and ord(c) <= ord('F') :
                    val += int(c, 16)
    
    clear_pw = ''.join(map(str, clear_pw))
    return clear_pw


#This is the cisco 7 hash of the string "password"
password = "021605481811003348"
password = reverse_hash(password)
print(password)
