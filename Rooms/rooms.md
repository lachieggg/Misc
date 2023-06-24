


Intro
= 

We are considering the number of people to bed assignments in a hotel for 10 people, 3 rooms, and 11 possible
beds across those 3 rooms. Therefore in every assignment there will be at least one spare bed.

We want to consider outcomes in which everybody is assigned a bed.

There are a few different working attempts here across different problems.

The first numerical approximation solution works out how many different room assignments there
are using a random function. We randomly assign people to each bedroom and then determine whether
that outcome is unique or not by checking whether the solution is in an array of previously found
solutions

The limit for this after 5 minutes of runtime is 2772 

The next attempt applies the same algorithm to the problem for individual bed permutations.
However, as we will see, there are billions of solutions to this problem, hence the runtime would
be infeasible. 

The third solution is faster but still likely computationally infeasible. However, it is easy to see
from this third solution when writing it out in code a variety of other ways to solve the problem.
The fastest of which is the probabilistic solution. 

Since each bed being spare has an exact probability of 1/11, we can work out the exact proportion of
cases where at least two beds are spare (n > 1). We can then determine the total number of solutions
generated. 

There are 10 for loops each iterating from 0 to 11, so there are exactly 11**10 outcomes generated
Thus we will have 25937424601 outcomes generated, and we just need to multiply that by the probability
that n = 1, which turns out to be approximately 0.99.

So then we get an outcome of approximately 25,701,629,831. So we can say with confidence that the 
number of possible permutations of beds in a hotel with 11 beds and 10 people is at least
25 and a half billion!


Notes
=

1
=
So it's 11**10 - k, where k is the number of situations in which n > 1
where n is the number of spare beds

2
=
A faster algorithm is therefore, to calculate the number of situations
in which there are more than 1 spare beds and take that from 11**10 (11^10)

Consider this as a graph. There are 11 nodes. There
are n*(n-1)/2 = 55 pairwise relationships between nodes

If the first two beds are both empty (i.e. have 'person id' of 0)
then all the rest generated after we have begun the second loop are also
invalid solutions (there are more than 1 spare beds).

The solutions generated in that situation are exactly 11**8 == 214358881

11**10 == 25937424601 (total solutions)

3
==
Consider if the first bed is taken, and the second is empty, how many situations
in which other beds could be spare too? I.e. there is at least one spare bed
after the second loop (i.e. loop 3 and beyond)

Well there are 11**8 total solutions in loop 3 and beyond. So how many situations in which 
there are no spare beds? There are 10**8 such situations, (iterating from 1 to 11 intead of from 0).

Therefore there are 11**8 - 10**8 == 114,358,881 situations where there are at least two spare
beds loop 3 and beyond.

So far we have 11**10 - 11**8 - (11**8 - 10**8) == 25608706839

4
=
Now we need to consider if the second is taken, and the first is empty
Which is just the same as (3.)

So then we have 11**10 - 11**8 - 2*(11**8 - 10**8) == 25,494,347,958 ~= 25 and a half billion

Pr(Bed is not taken) = 1/11

5
=
Now we must consider if they are both taken
Then we need to find the situations where n > 1 where n is the number of spare beds
except this time there are only 8 beds. So this becomes a recursive problem.

6
=
For one bed, there are no circumstances in which n > 1
For two beds, there is 1 circumstance
For three beds, there are 3 ({1: 0, 2: 0, 3: 1}, {1: 0, 2: 1, 3: 0} ...)
For 

Suppose that for k-1 beds, there are exactly j times when n > 1
Then for k beds, how many times is n > 1?

7
=

Consider the probabilistic solution.

Since our probabilities are exact, that is, we are guaranteed that 
the probability of any given bed being spare is exactly 1/11,
and each bed being empty is independent of any other bed being empty,
since which bed a person gets is essentially like a biased coin flip. 

Therefore

Pr(n = 1) = 1/11
Pr(n = 2) = 1/121
Pr(n = 3) = 1/11**3
Pr(n = k) = 1/11**k for 0 < k <= 11


So we need to do a sum to work out the exact probability that n > 1
Sum n from 2 to 11 of 1/11**n

= 2593742460/285311670611

So 1 - Pr(n > 1) ~= 25,701,629,831

So there are approximately 25 billion 700 million possible permutations of bed assignments
across 11 beds with 10 people.

