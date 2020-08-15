#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)I am confused with this one. If given a negative INT, the runtime complexity is
O(1). However, if a positive INT is passed that WHILE loop will run infintely
because the square + "a" will always be less than the cube.


b) The runtime complexity is O(n log n). The FOR loop will run n times and
for each time, the while loop will run log n times as the *= catching up with the
n.


c) O(n). While this code has recursion, it only has one recursive call so as n
grows, it increases at a constant rate.

## Exercise II

The runtime is O(log n). As we wish to use the fewest eggs possible, I would use 
something like a binary search algorithm. Starting at half of n and drop the egg.
If it doesn't breaks, we remove all floors less than half of n. If breaks we 
remove all floors greater than n. Drop the egg at the midpoint of the remaining 
floors and repeat the process until only 1 floor remains. The worst case scenario
is it being the first or last floor.


