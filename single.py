# Question 1. 2. 3. 4. 7. 8. 9. 10.
# They give a question prompt, several options, each options it return an absolute value of score

# Below are the answers and their corresponding values
# Question One.
Q1P = 'You are walking on the campus and suddenly you heard people screaming. From distance you can see a girl vommiting blood. You are scared but wondering what happens. You stand still and that girl starts to attack people surrounding. "Zombie", the word comes to your mind, but you are unsure. What should you do first? '
Q1A = {
    'Try to seperate that gril and the person she is attacking':1,
    'Run back to your home':2,
    'Call the police':3,
    'Call your families and ask them to stay away from the crowd':4}
Q1K = {1:-10, 2:60, 3:30, 4:40}

#Question Two.
Q2P = 'Before you start to do anything, that girl chaced another person and left your visible range. You called the police and your families but your phone lost signal. It is time to go home. You know there are 3 routes, which one you choose?'
Q2A = {
    '22 minute trail cross a chuck of forest which will lead you to your backyard':1,
    '15 minute route but has to cut across the cafeteria':2, 
    '18 minutes route that avoid most people, will pass the front door of your neighbors':3}
Q2K = {1:60, 2:10, 3:30}

#Question Three.
Q3P = 'You arrived home. What should you do first?'
Q3A = {
    'Close all the doors and windows immediately':1,
    'Find a weapon':2,
    'Gather all the food and bottled waters':3
}
Q3K = {1:40, 2:30, 3:20}

#Question Four.
Q4P = 'Your radio rustled and then you heared the broadcast said "An unknown virus is spreading ... stay ... An unknown ...at home..." You lost signal again. What\'s your next plan?'
Q4A = {
    'Stay at home and wait for help':1,
    'Leave your home':2,
}
Q4K = {1:-10, 2:20}

#Question Seven.
Q7P = 'There are several weapons at home, which one do you choose?'
Q7A = {
    'Gun':1,
    'Chainsaw':2,
    'Baseball Bat':3,
    'Wrench':4
}
Q7K = {1:15, 2:10, 3:50, 4:-10}

#Question Eight.
Q7P = 'There are several weapons at home, which one do you choose?'
Q7A = {
    'Gun':1,
    'Chainsaw':2,
    'Baseball Bat':3,
    'Wrench':4
}
Q7K = {1:15, 2:10, 3:50, 4:-10}

#Question Nine.
Q9P = 'You came to a crossroad intersections. You quickly glance over all the four directions you can go and saw a human figure in each direction. Where do you want to go?'
Q9A = {
    'Direction 1':1,
    'Direction 2':2,
    'Direction 3':3,
    'Direction 4':4
}
Q9K = {1:15, 2:10, 3:50, 4:-10}

#Question Ten.
Q7P = 'There are several weapons at home, which one do you choose?'
Q7A = {
    'Gun':1,
    'Chainsaw':2,
    'Baseball Bat':3,
    'Wrench':4
}
Q7K = {1:15, 2:10, 3:50, 4:-10}

class abssingle:
    """Single questions"""
    
    def __init__(self, prompt, answers,answer_key):
        """Every Single questions have a prompt, more than one options but user can only select one, and answer keys."""
        self.prompt = prompt
        self.answer_key = answer_key
        self.answers = answers

    def score(self,option):
        return self.answer_key[self.answers[option]]

Q1 = abssingle(Q1P,Q1A,Q1K)
Q2 = abssingle(Q2P,Q2A,Q2K)
Q3 = abssingle(Q3P,Q3A,Q3K)
Q4 = abssingle(Q4P,Q4A,Q4K)
Q6 = abssingle(Q6P,Q6A,Q6K)
Q7 = abssingle(Q7P,Q7A,Q7K)