# Python-Data-Structures
Python learning project.

My implementation of some basic Data Structures from scratch.

1. Linked List:  
- add_first  
- append  
- get  
- pop  
- clear  
- append_list  
	
2. Stack(list based):  
- push  
- pop  
- peek  
- search  
- is_empty  
- clear  

3. Queue(double linked list based):  
- push  
- pop  
- peek  
- search  
- is_empty  
- clear  

4. Heap (min)  
- append  
- peek  
- pop  
- is_empty  
- clear  

5. Hash Table  
- from_keys (static constructor)
- insert  
- search  
- pop  
- clear  
- [] sintax

6. Doubly Linked List  
- add_first  
- append  
- get  
- pop  
- clear  

7. Circular Linked List  
- add_first  
- append  
- get  
- pop  
- clear  
- step  


Time complexity:  

| data structure | Add first | Add last | Delete first | Delete last | Delete middle | Get first | Get last | Get middle |
| - | - | - | - | - | - | - | - | - |
| Stack | - | О(1) | - | О(1) | - | О(1) | О(n) | О(n) |
| Queue | О(1) | - | - | О(1) | - | О(n) | О(1) | О(n) |
| Heap | О(log n) | - | О(log n) | - | - | О(1) | - | - |
| Linked list | О(1) | О(n) | О(1) | О(n) | О(n) | О(1) | О(n) | О(n) |
| Doubly linked list | О(1) | О(1) | О(1) | О(n) | О(n) | О(1) | О(n) | О(n) |
| Circular linked list | О(1) | О(1) | О(1) | О(n) | О(n) | О(1) | О(n) | О(n) |
