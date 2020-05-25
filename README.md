# RandomWalk-Probability-and-Statistics-Project

**Task 1 – discrete random variables:**
Create a one-dimensional random walk mathematical and simulation-based model to predict the expected distance from the starting point. You should test your models for range of scenarios e.g. starting position, (un)equal probabilities of moving left, right, and not moving at all.

**Task 2 – discrete random variables:**
Create a one-dimensional random walk mathematical and simulation-based model where two people start x units away from each other and are traversing the grid with some probabilities. Predict the expected time it takes to meet them. You should test your models for a range of scenarios. List any assumptions you may have made.

**Task 3 – discrete random variables:**
Create a two-dimensional random walk model using simulation-based approach. The two-dimensional region in R2 is a circular region of radius 100 units (1 unit can be 1 cm or 1 meter, or 1 km). We would refer our two dimensional circular space as a disc, d(0,R). A node or nodes within a circular region d(0,R) at time t, undertakes a random walk whose next position at the ﬁxed discrete time t+1 unit time’ is modeled as follows: (a) Step size is a discrete random variable. You can assume that step size is between {0,0.5,1}. (b) Orientation is a discrete random variable between [0−2π]. For example – a node at the center of a 100-unit radius circle will take a random step of size r between {0,0.5,1} and a direction with angle θ. To begin with, you may ﬁnd it easier to assume that all step sizes and angles are equally likely.
Over the next course of time slots the node will traverse a random path based on the random walk model described above. Of course, at some point in time, it is quite likely that after many units of time, the node might try to leave the 100-unit circular region. Its re-entry model, to ensure that the node does not escape the test region, is left for the students to be worked-out. As an example, once the node hits the boundary you can ensure that its bounces oﬀ the circumference back into the region. Whatever model of node re-entry you choose, it should be based on logic, explanation and some literature review. You would be asked for its explanation and justiﬁcation.
At the end of this task the trajectory of the node starting from the origin with the re-entry model will be demonstrated and assessed.

**Note:** I have used two different approaches. In task3(1).py, the random walk, the distance randomly chosen from the list, is associated with radius of the new circle around the starting point of the random walk which is then broken down into its x and y component. Whereas, in task3(2).py, I had assigned 2 randomly chosen distance to x and y and then I found the radius of the new circle from that. 

**Task 4 – Continuous random variables:**
Repeat task 1 by assuming that the step size is a continuous uniform random variable between 0−1. Again, you may ﬁnd it easier to model the PDF as a uniform random variable

**Task 5 – Continuous random variables:**
Repeat task 3 by assuming that the step size and the orientation are continuous random variables between 0 − 1 and 0 − 2π. Again, you may ﬁnd it easier to model the PDF as a uniform random variable. Feel free to try other distributions

**Task 6 – Continuous random variables:**
Repeat task 3 by assuming that the step size is a discrete random variable and the orientation is a continuous random variables between 0−2π.

**Task 8:**
Building on task 5, each team will capture the trajectory of two nodes whose initial locations are chosen randomly and uniformly over a circular region. Every team will be asked to explain how did they model the initial position of the two nodes. In this part you will have to determine, the average number of steps taken by the two nodes so that they are within 1 unit (distance between the two nodes < 1 unit distance). You will need to work out the number of simulations required to calculate the average number of steps needed. There is some science behind it. So make sure you are ready to defend the accuracy of your expected value of the number of steps taken by the two nodes so that they are within 1 unit of each other.

**Task 9 – Bonus:**
Building on task 8, extend your work to any applied problem or application related to the current ‘Coronavirus spread (COVID-19)’. World Health Organization (WHO) declared the 2019-20 coronavirus outbreak a pandemic. As an example, you can extend your Task – 7 to capture visual depiction of the “Social Distancing” aspects. The art in this task is to connect the work in Task – 5 & Task – 7 to the application, any problem formulation or depiction related to the COVID-19 situation.

**HINT:** For all the tasks mentioned above, in the beginning, please keep your models as simple as possible. You can add the complexity incrementally. For example if you are experience diﬃculty with circular region, you can start working on a square region and then transition to a circle
