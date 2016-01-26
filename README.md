Disclaimer: This project is merely an attempt to explore Python and its 
threading capabilities.

-----------------------------------------------------------------------

This is rather simple pool threading concept, where you create a number 
of tasks statically or even dymanically and you add them in the pool.

The pool is implemented as a queue and executes the tasks in parallel. 
By default the pool can maintain up to 8 tasks at the same time. We 
choose this limit, since most people have 4 core CPUs, which most of 
the time corresponds to 8 hardware threads. Currently you are unable 
to resize your queue dynamically, only statically upon creation. This 
ISSUE will be fixed soon, so you can dynamically change the maximum 
number of threads.

