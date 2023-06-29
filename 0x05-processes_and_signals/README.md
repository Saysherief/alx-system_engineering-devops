#Processes and signals
##PID Definition
A PID (i.e., process identification number) is an identification number that is automatically assigned to each process when it is created on a Unix-like operating system.

A process is an executing (i.e., running) instance of a program. Each process is guaranteed a unique PID, which is always a non-negative integer.

The process init is the only process that will always have the same PID on any session and on any system, and that PID is 1. This is because init is always the first process on the system and is the ancestor of all other processes.

A very large PID does not necessarily mean that there are anywhere near that many processes on a system. This is because such numbers are often a result of the fact that PIDs are not immediately reused, in order to prevent possible errors.

The default maximum value of PIDs is 32,767. 

##What is a Process?
A process can be thought of as an instance of a program in execution. We called this an ‘instance of a program’, because if the same program is run lets say 10 times then there will be 10 corresponding processes.

Moving ahead, each process has its own unique process ID through which it is identified in the system. Besides it own ID, a parent’s process ID is also associated with a process.

##The main() Function
A ‘C’ program always starts with a call to main() function. This is the first function that gets called when a program is run.

The prototype of a main() function is :
code <int main(int argc, char *argv[]);>
In the above prototype :

The return type of the main() function is ‘int’. This is because,, when the main() function exits, the program finishes. And a return type from main() would signify whether the program got executed properly or not. In strict sense we say that if main() returns ‘0’, then the program got executed successfully. Any other return value indicates a failure.
The main() function accepts two arguments. One is the number of command line arguments and the other is the list of all the command line arguments.
Types of Processes in Linux
In Linux processes can be of two types:

Foreground Processes
depend on the user for input
also referred to as interactive processes

Background Processes
run independently of the user
referred to as non-interactive or automatic processes

Process States in Linux
A process in Linux can go through different states after it’s created and before it’s terminated. These states are:
A process in **running** state means that it is running or it’s ready to run.

The process is in a **sleeping** state when it is waiting for a resource to be available.

A process in ***Interruptible sleep*** will wakeup to handle signals, whereas a process in ***Uninterruptible sleep*** will not.

A process enters a **stopped** state when it receives a stop signal.

**Zombie** state is when a process is dead but the entry for the process is still present in the table.

*To learn more* https://www.digitalocean.com/community/tutorials/process-management-in-linux
