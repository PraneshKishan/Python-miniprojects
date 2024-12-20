plaintext = 'Pranesh kishan'
n = 1

def encrypyt_text(plaintext, n):
    ans = []
    res = ''
    for i in range(len(plaintext)):
        if plaintext[i] == ' ':
            ans.append(' ')
        elif plaintext[i].isupper():
            encrypted_char_u = ((ord(plaintext[i])+n-65)%26)+65
            ans.append(encrypted_char_u)
        elif plaintext[i].islower():
            encrypted_char_l = ((ord(plaintext[i])+n-97)%26)+97
            ans.append(encrypted_char_l)
    for val in ans:
        if isinstance(val, int):
            res += chr(val)
        else:
            res += val

    return res

print("Plaintext: ",plaintext)
print("Shift Pattern: ",n)
final = encrypyt_text(plaintext,n)
print(final)