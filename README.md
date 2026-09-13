# ZKP-RSA-Engine

The project features a CLI (Command Line Interface) based simulation of encryption and decryption using cryptographic algorithms like RSA and ZKP.
It is build without any external libraries and relies on pure arithmetic calculations for implementation of the algorithms.

---

## Technical Features -

* **i)   Zero Knowledge Proof Authentication:** Challenge-response verification protocol protecting user secrets from network exposure.
* **ii)  Custom RSA Engine:** Prime number generation, Euler's totient calculation , gcd calculations , and modular calculations.
* **iii) RAM Based Memory:** Ephemeral memory storage (data) handling encrypted exchanges with zero disk I/O.
* **iv)  Custom Codec's:** Character-to-integer conversion routines converting strings to ASCII arrays for mathematical processing.

---

## Technologies and Tools Used -

* **i)   Programming Language:** Python 3.8+ .
* **ii)  Core Modules:** Standard Python standard library , Random Module.
* **iii) Version Control:** Git & GitHub
* **iv)  Development Environment:** Visual Studio Code (VS Code).

---

## Project Structure -

```text
RSA_ZKP_PROJECT/
├── main.py               # Interactive CLI.
├── crypto_ops/
│   ├── rsa_gen.py        # RSA key pair generations.
│   └── zkp_auth.py       # ZKP protocol execution.
├── math_ops/
│   ├── prime_gen.py      # Custom prime number generation.
│   └── gcd_e_d.py        # GCD , e ,d calculation.
└── utilities/
    ├── codec.py          # Translator [Text to Ascii to Text].
    └── memory.py         # Stores the Client Server Conversations.
```
---  

## Steps to Install & Run the Project -

* **Prerequisites** i) Ensure Python 3.8 or higher is installed.

* **Installation** i) git clone https://github.com/securebyte-0x29/ZKP-RSA-Engine.git ii) cd RSA_ZKP_PROJECT

* **Execution** i) python3 main.py

---

## Instructions for Testing - 

* **Step 1: System Key Generation ->** Select Option 1 from the main menu. Verify that the system generates distinct RSA key pairs (e, n) and (d, n) for both the Client and Server entities.

* **Step 2: Execute ZKP Identity Handshake ->** Select the Option 2 after generating system keys. Client registers public token V, sends commitment X, receives challenge {0, 1} and submits response Y.
  
* **Step 3: Encrypt & Relay Message ->** Select Option 3 to send message. Observe the custom ASCII codec converting text into integer arrays and encrypting them with the recipient's public key before saving to the RAM inbox.
  
* **Step 4: Parse & Decrypt Inbox ->** Select Option 4 to view messages available to decrypt. Observe that the recipient successfully decrypts the integer array back to the original plaintext message using their private key.

---
    
    
