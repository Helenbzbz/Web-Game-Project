# Final Project Proposal

## The Big Idea

This project is a website to help users prioritzie tasks, keep tracks of things to do, long-term goals, how long they spent on long-term goals, and (if possible) visualize everyday schedule into a calendar. 
I will apply flask for this assignment. I wish I will be able to get all parts done and work on formatting and designing this websites. 
If I still have extra time, I will try to add more interactive elements in this website to motivate users to stick to their schedules. For example, I can add tokens to this website and allow users to set a dream lists with pre-set token price for each item they want.

This is a sktech of the website
![This is a sketch of the website](https://github.com/Helenbzbz/Team-Project/blob/main/Sketch.png)

## Learning Goals

I regard this project as a good practice of what I learnt in this class so far. 
The biggest goal is to use Python to turn my ideas into a useful website. 
By the end of the project, I wish I will learn some contents outside the scope of the courses. 
The contents I might learn includes UI/UX, how to save the content entered into the website somewhere else and return when the website is reopened, and how to visualize information in Python in a more user-friendly manner. 
I hope after this project, I can be more experienced and efficient at building website from scratch and managing database.
This project will also train me on how to manage a project timelines and divide the work appropriately into time blocks.

## Implementation Plan & Project Schedule

I break down the project into the following tasks and allocate these tasks into the 3.5 weeks schedule.
Since I chose to work alone, there is no collaboration plan.

**Week 1. 4.7~4.14**
1. *Write the codes for to do list function*
- A function that will automatically return the current time, after entering the deadline, returns how many hours still have
- A function generate a list of all the time used for completing tasks fall under one long-term goal
2. *Write the codes for saving schedule part* 
- A function to automatically generate the 2 hours interval for next 7 days
3. *Write the codes to calculate the total time used on a long-term goal* 
- A function that will return the current date, after entering the deadline, returns how many days still have
- Take an unput from part 1 to compute the total time used on one lng-term goal

**Week 2. 4.14~4.21**
1. *Write flask codes to implement the to do list function*
- Allows 4 inputs, one for long term goal, one for task name, one for deadlines, and one for estimated time
- Update the to do after entering the value
- After clicking the complete, the task's time will be saved under the long-term goal
2. *Write flask codes to implement the shcedule part*
- Allow entry of task for each time interval generated
- Print the outcome in a table format
3. *Write flask codes to implement long-term goal section*
- Allow 2 inputs, one for long term goal, one for deadlines
- Update the long-term goal in a nice manner
- Process the list of task times for each long-term goal and show it on the website

**Week 3. 4.21~4.28**
1. Improve UI/UX of the website
2. Improve the projects, preapre for demo session
3. Add encouraging system

The following 3 things I need to learn during this weekend before I can start to work on the project:
1. How to save inputs or data in a database so that next time when I open the website it still has the information I entered previously
2. How to organize the website design to make it more userfriendly
3. After clicking the button of 'Complete', how do I add the time for this task into the total time I spent in a corresponding category

## Risks

I considered this project as a little bit ambitious and I am unsure whether I can successfully complete all my desired functions. 
Given we only have 3 weeks to finish this project, I will first finish the core function of the website, to do list, and then moves on to finish other function if possible.
If the tasks turned out to be more difficult than I thought, I may give up on the total time spent for each long-term goal function.

## Additional Course Content

I think we will cover how to save data on website in the following classes? I think more materials about user interactive functions will be very helpful.
One thing I am personally interested in is how to create a website that user have to register in order to use it. But I think it might be too advanced. 