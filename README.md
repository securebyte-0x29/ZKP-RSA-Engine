# Project Title
ZKP-RSA-Engine

## Overview of the project
This is a simple command line Python program that shows how RSA encryption and Zero Knowledge Proofs works. I built this entirely from scratch using basics of cryptography without using any external security libraries. 

## Features
* **ZKP Login:** A math-based challenge that lets a user prove who they are without ever sending a password over the network.
* **Custom RSA Encryption:** Code that generates random prime numbers and calculates public/private keys from scratch.
* **Text Converter:** A custom tool that turns text letters into numbers so the RSA math formulas can encrypt them.
* **RAM Memory Storage:** Messages are temporarily saved in a simple Python dictionary while the program is running, instead of saving them to a hard drive.

## Project Structure -
   
```text
RSA_ZKP_PROJECT/
├── main.py              
├── crypto_ops/
│   ├── rsa_gen.py       
│   └── zkp_auth.py      
├── math_ops/
│   ├── prime_gen.py      
│   └── gcd_e_d.py       
└── utilities/
    ├── codec.py        
    └── memory.py       
```

## Technologies/tools used
* **Language:** Python 3.8+
* **Libraries:** Standard Python library and the `random` module
* **Tools:** Git, GitHub, and VS Code

## Steps to install & run the project
1. Make sure Python 3.8 or higher is installed on your computer.
2. Open your terminal and clone the project: `git clone https://github.com/securebyte-0x29/ZKP-RSA-Engine.git`
4. Run the code: `python3 main.py`

## Instructions for testing
1. **Generate Keys:** Press 1 on the menu to create the RSA public and private keys for the Client and Server.
2. **Test ZKP:** Press 2 to start the ZKP login. Watch the Client and Server pass numbers back and forth to verify identity.
3. **Send Message:** Press 3 to type a text message. The program will turn your text into numbers and encrypt it with a public key.
4. **Read Message:** Press 4 to decrypt the inbox. The receiver uses their private key to turn the numbers back into readable text.
