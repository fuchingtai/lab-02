# Lab 2
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Ching-Tai (Vincent) Fu
- no team member 2

## Lab Question Answers

Answer for Question 1: When lowered to 50%, the recieving end did not have anything showed up. The reliability is greatly reduced. This is because when UDP is lossy, the data may be lost or recieved out of order.

Answer for Question 2: Reliability of the TCP did not change. The numbers are still successfully transmitted. This is because the TCP will detect loss and ensure the data is still transmitted.

Answer for Question 3: The response speed of the TCP is decreased. This is because TCP will reconstruct the lost message and resend it. This action of reconstruction and retrasmission requires time, and hence the delay.


## tcp_server.c Question Answers

What is argc and *argv[]? 
Ans: In C/C++, argc stands for argument count (in integer), which indicates how many arguments were entered in the command line. *argv[] stands for argument vectors, and is an array of pointer to character (char) objects.

What is a UNIX file descriptor and file descriptor table? 
Ans: File descriptors are non-negative integers (entry numbers i.e.: 1, 2, ..., 100) that each represent an opened filed. If we opened 100 files, there are 100 of these entries. These entry numbers are the file descriptors. A file descriptor table is a series of integer array indices that contains pointers to the entries.

What is a struct? What's the structure of sockaddr_in? 
Ans: Struct is a user defined varaible type that can be used to group several related variables. All the variables are stored under one block of memory, which makes them accessible by a single pointer. The structure of sockaddr_in specifies a transport address and port for the AF_INET address family (Microsoft Learn).

What are the input parameters and return value of socket()? 
Ans: The input parameters are (1) the address family of the socket to be created, (2) the type of socket to be created, and (3) the protocal to be employed. The return value of socket() will return the socket file descriptor, which, by convention, is a non-negative integer.

What are the input parameters of bind() and listen()? 
Ans: bind() has the parameters fn, which is the function of objects and args. listen() requires two inputs, one is a descriptor for identifying a bound, unconnected socket, and the second is the max length that the pending connection queue can grow to.

Why use while(1)? Based on the code below, what problems might occur if there are multiple simultaneous connections to handle? 
Ans: We need to run this part of the code indefinitely. If there are multiple simultaneous connections to handle, the loop may fail owing to processing mutiple messages simultaneously.

Research how the command fork() works. How can it be applied here to better handle multiple connections? 
Ans: fork() works by creating two simultaneous executing processes of a progrom. One is refered to as the parent process and the other as the child process. In this case, fork() can be employed to handle multiple connections through the creation of two processess that can function simultaneously.

This program makes several system calls such as 'bind', and 'listen.' What exactly is a system call? 
Ans: A system call is the process in which a program requests a service from an operation system on which the program is executed (linux in our case). I'd understand it as an procedure that functions between a process and the Linux operating system.
