## shifty-secrets
Implements Caesar Cipher encryption/decryption algorithm.

## Caesar Cipher ?
It's a technique in cryptography where each letter in a message is shifted down the alphabet A..Z by a certain specified numerical value. 

For example: with a shift of <b>3</b>, the message <b>"hello world"</b> becomes <b>"khoor zruog"</b>

## Installation and set-up requirements
Here is a run through of how to set up the application localy.
### Requirements
- Python
    - to check for python run on terminal/shell
    >>>> $ python --version
    - or
    >>>> $ python3 --version
### Steps
1. Clone repository
    - example
    >>>> $ git clone https://github.com/brienjuma/shifty-secrets.git
2. Change to directory
    >>>> $ cd shifty-secrets 
3. Run 
    >>>> $ python main.py "This is the message to encrypt" 5 --mode encrypt
    -    or 
    >>>> $ python main.py "khoor zruog" 3 --mode decrypt
    - where the string in quotes is the message, 
    - integer value is the shift key. <b> !!!! shift value must be a positive integer i.e. greater than zero (x >= 1) </b>
    - and last is the encrypt/decrypt switch.
