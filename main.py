from crypto_ops.rsa_gen import system_keys, encrypt_message, decrypt_message
from crypto_ops.zkp_auth import run_zkp
from utilities.codec import text_ascii, ascii_text
from utilities.memory import data

is_auth = False 
c_pub_k, c_pvt_k = 0 , 0
s_pub_k, s_pvt_k = 0 , 0

while True:
    print(" RSA-ZKP TERMINAL ")

    print("1. Generate System Keys")
    print("2. Authenticate via ZKP")
        
    if is_auth:
        print("3. Encrypt & Send Message")
        print("4. Decrypt & Read Message")
            
    print("5. Exit")
        
    ch = input("Enter your choice : ")

    if ch == '1':
        
        c_pub_k, c_pvt_k, s_pub_k, s_pvt_k = system_keys()
        print("Client Public : ",c_pub_k)
        print("Server Public Keys : ",s_pub_k)

    elif ch == '2':
        if c_pub_k == 0:
            print("Generate keys first!")
        else:
            is_auth = run_zkp(c_pub_k)

    elif ch == '3' and is_auth:
        
        print("ENCRYPT MESSAGE")
        
        dirc = input("Who is sending [C - Client, S - Server] : ").upper()
        msg = input("Enter the text: ")
       
        l = text_ascii(msg)
            
        if dirc == 'C':
            
            print("Client encrypting with Server's Public Key...")
            encry_text = encrypt_message(l, s_pub_k)
            data["server"].append(encry_text)
            print("Encrypted text: ",encry_text)
            
        elif dirc == 'S':
            
            print("Server encrypting with Client's Public Key...")
            encry_text = encrypt_message(l, c_pub_k)
            data["client"].append(encry_text)
            print("Encrypted text: ",encry_text)

    elif ch == '4' and is_auth:
            
        print("DECRYPT MESSAGE")
        direc = input("Who is reading [C - Client, S - Server] : ").upper()
            
        if direc == 'S':
            count = 1
            for d in data["server"]:
                print("Server decrypting message",count," with Server's Private Key...")
                decryp_nums = decrypt_message(d, s_pvt_k)
                text = ascii_text(decryp_nums)
                print("Decrypted Text: ",text)
                count += 1
                    
        elif direc == 'C':
            count = 1
            for d in data["client"]:
                print("Client decrypting message",count," with Client's Private Key...")
                decryp_nums = decrypt_message(d, c_pvt_k)
                text = ascii_text(decryp_nums)
                print("Decrypted Text: ",text)
                count += 1

    elif ch == '5':
        print("Exiting...")
        break
    else:
        print("Invalid Choice...")

