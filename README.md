# EncryptedM
This programm allow to send encrypted messages between two hosts thought LAN. 
This App, created with Python 3.4, allows sending encrypted messages between two hosts in LAN. A cryptographic algorithm is AES. 

List of used modules:
*	Tkinter
*	Socket
*	Time
*	Crypto
*	Thread

First, need to input secret AES-key in AES_KEY.txt (16/24/32 bytes), which to know only two persons. Second, to fill fields of the form:
*	«destination IP» is IP address of catcher host in LAN
*	«my IP» is your IP in LAN
*	«port» is used the port with App.

And click «start» for each hosts.

Example:

![1st host](https://github.com/ST1LLY/EncryptedM/blob/master/1st_host.png)
![2nd host](https://github.com/ST1LLY/EncryptedM/blob/master/2nd_host.png)
