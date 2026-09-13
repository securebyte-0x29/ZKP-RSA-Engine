# Project Statement: ZKP-RSA-Engine

## 1. Problem Statement

Modern communications rely on Certificate Authorities and password hashes for authentications
. This model introduces many points of failure and vulnerable password storage repos moreover 
an eavesdropper could listen on the network and increase the risk of session hijacking. There is a need for a lightweight
security protocol that verifies user identity without transmitting secret tokens across the network while establishing asymmetrical
encryptions.

## 2. Scope of the Project
This is a ram base CLI cryptographic environment built in Python. The system integrates two core cryptographic standards:

* **Identity Verification:** Employs an interactive Zero Knowledge Proof (ZKP) challenge response
   protocol to authenticate users without exposing sensitive credentials.
  
* **Asynchronous Confidentiality:** Implements custom RSA key pair generation
   to secure message exchanges between client and server in memory vaults.

The project excludes file storage and third party cryptographic libraries
to demonstrate underlying mathematical logic.

## 3. Target Users
* **Cybersecurity Researchers & Students:** Analyzing zero trust mathematical execution and asymmetric key management.
* **System Architects:** Inspecting volatile session management for embedded terminal environments.

## 4. High-Level Features
* Dynamic generation of distinct RSA key pairs for Client and Server.
* Zero-Knowledge challenge-response authentication protocol (Commitment, Challenge, Response, Verification).
* Custom text to integer ASCII translation codec for raw message preparation.
* power `pow()` modular exponentiation method for RSA encryption decryption.
* Volatile ram bases memory `dictionary` for client-server encrypted message communication.