## Problem statement
 Systems use simple passwords for login, but these can be easily stolen if an attacker is spying on the network.There is need for a lightweight, simple tool that lets users log in securely without sending their actual password, while also keeping their messages safely encrypted.

## Scope of the project
This is a terminal-based project it focuses on two core cybersecurity concepts:

1. **Safe Login:** Using a Zero Knowledge Proof so a user can authenticate safely.
2. **Secret Messages:** Using custom built RSA encryption to secure messages between a client and a server. 

The project avoids external databases or third party crypto libraries so mathematical logic can be demonstrated.

## Target users
* **Cybersecurity Students:** Anyone learning about encryption who wants to see how zero-trust logins and public/private keys work from scratch.
* **Teachers/Reviewers:** To inspect a basic terminal program that manages secure data in memory.

## High-level features
* Creates custom RSA public and private keys for both the Client and Server.
* Runs a 4 step ZKP math challenge (Commitment, Challenge, Response, Verification) for login.
* Converts standard text into integers for math processing.
* Uses Python's built-in `pow()` math function for RSA encryption and decryption.
* Stores chat messages temporarily in RAM using a Python dictionary.