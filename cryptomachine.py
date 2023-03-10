def encrypt(usr_msg, mode):
    # keys = 'asdfghjkqwertyuiomnbvcxzqwertyuioplkjhgfdsa!?@#$%^&*()_+ '
    secret = open(r"src/Text.txt", "r+")
    keys = secret.read()
    value = keys[-1] + keys[0:-1]
    
    usr_msg = usr_msg.split('\n')
    new_usr_msg = listToString(usr_msg)

    encrypted_message = dict(zip(keys, value))

    if mode.upper() == 'E':
        newMsg = ''.join([encrypted_message[letter] for letter in new_usr_msg.lower()])
    else:
        print("Invalid mode")
    
    return newMsg

def decrypt(usr_msg, mode):
    # keys = 'asdfghjkqwertyuiomnbvcxzqwertyuioplkjhgfdsa!?@#$%^&*()_+ '
    secret = open(r"src/Text.txt", "r+")
    keys = secret.read()
    value = keys[-1] + keys[0:-1]
   
    usr_msg = usr_msg.split('\n')
    new_usr_msg = listToString(usr_msg)

    decrypted_message = dict(zip(value, keys))

    if mode.upper() == 'D':
        newMsg = ''.join([decrypted_message[letter] for letter in new_usr_msg.lower()])
        return newMsg
    else:
        print("Invalid mode")


def listToString(s):
 
    # initialize an empty string
    str1 = ""
 
    # traverse in the string
    for ele in s:
        str1 += ele
 
    # return string
    return str1
 

if __name__ == "__main__":
    while(True):
        usr_msg = input("Enter your message: ")
        mode = input("Encrypt or Decrypt: ")
    
        if mode.upper() == 'E':
            new_msg = encrypt(usr_msg, mode)
            print(new_msg)
        
        elif mode.upper() == 'D':
            new_msg = decrypt(usr_msg, mode)
            print(new_msg)

        else:
            print("Invalid mode")

        if input("Do you want to continue? (y/n): ").upper() == 'N':
            break


