#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
Runtime: constant O(1)

In the worst case scenario, the function will only run twice for any input, no matter how large. 


b)
Runtime: Linearithmic O(n log n)

In the worst case scenario, the runtime will increase faster than at a linear rate as n increases, however the runtime will grow slightly less than at a polynomial rate due to the while loop. 

c)
Runtime: Linear O(n)

In the worst case scenario, the number of times that the bunnyEars function runs is directly proportional to the number of bunnies passed to the function. 

## Exercise II

From the way this question is posed, my understanding is that we could write an algorithm such that only only one egg is broken. 

To accomplish this, I would:

- First make sure the input value f was in an itterable format. If not, I would put it into a list or or some other itterable format.

- I would then loop through f, and at each itteration / floor, I would throw an egg and see if it was broken.

- At the first floor, I would throw an egg. If the egg broke, then f would be equal to the first floor, and we would have broken only one egg. I would then return i ( the itteration of the loop we were on).

- If the egg did not break, I would advance to the next floor, and repeat this process until I reached the floor where the egg broke. I would then return i ( the itteration of the loop we were on).

- The runtime complexity of the algorithm would be O(n), or linear. In the worst case, f would be the very top floor / end of the list, meaning that the time complexity would grow proportionally to the number of floors in f. 
