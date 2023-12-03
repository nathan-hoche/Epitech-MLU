# Exercise 4

## Technique used

In this exercise, as we have to find the reward at each cycle, to get the best reward, we have to explore the environment and exploit the best action we found.

To do so, some points are used:
1. Detect if it's a new cycle or not
2. If it's a new cycle, we have to explore the environment
3. If we are on an extremity, we have to change the direction
4. If we are on the reward, we need to stay on it until the end of the cycle