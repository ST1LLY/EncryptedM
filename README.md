# EncryptedM
This App, created with Python 3.4, allows sending encrypted messages between two hosts within LAN. A cryptographic algorithm is AES. 

List of used modules:
*	Tkinter;
*	Socket;
*	Time;
*	Crypto;
*	Thread.

First, you need to input secret AES-key in `AES_KEY.txt` (16/24/32 bytes), which is known by only two persons. Second, fill the fields of the form:
*	«destination IP» is the IP address of the catcher host in LAN;
*	«my IP» is your IP in LAN;
*	«port» is the port used by the App.

And click «start» for each hosts.

Example:

![1st host](https://github.com/ST1LLY/EncryptedM/blob/master/1st_host.png)
![2nd host](https://github.com/ST1LLY/EncryptedM/blob/master/2nd_host.png)
