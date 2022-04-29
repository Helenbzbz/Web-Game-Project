# Question 5. 6. 7.
# They give a question prompt, several options.
# Player can choose multiple results and by taking a line of input seperate by comma, the score function will return the score.

#Question Five.
Q5P = 'After counting all the things you have at home, you realized you can\'t stay at home for long so you decided to leave your home anyway. You have space to carry 4 of them with you. What are the 4 things you will take?'
Q5A = {
    '3 Bottles of water':1,
    '4 Slices of toasts':2,
    'Flashlight':3,
    'First aid kit':4,
    'N95 face masks':5,
    'Basic medicines':6,
    'Family photo':7,
    'A bottle of vodka':8,
    'Map':9
}
Q5K = {1:30, 2:10, 3:20, 4:30, 5:-10, 6:30, 7:20, 8:15, 9:40}

#Question Six.
Q6P = 'Before you leave, you recall the memory about all the zombie fictions you read. How do you kill a zombie?'
Q6A = {
    'Burn it':1,
    'Hit its heart or head with gun or other weapon':2,
    'Use Salt':3,
    'Headshot':4
}
Q6K = {1:15, 2:5, 3:-60, 4:40}

#Question Seven.
Q7P = 'Great. And what are the characteristics of zombies?'
Q7A = {
    'They walk slow':1,
    'They may or may not have sights':2,
    'They attack human and feed on human':3,
    'They only appear at night':4,
    'They can think':5,
    'They look different from human':6
}
Q7K = {1:15, 2:10, 3:50, 4:-10}

class multiple:
    """multiple questions"""
    
    def __init__(self, prompt, answers,answer_key):
        """Every multiple question has a prompt, more than one options, user can choose all the options they want, and answer keys."""
        self.prompt = prompt
        self.answer_key = answer_key
        self.answers = answers

    def score(self,option):
        answer_list = option.split(',')
        sum = 0
        for i in answer_list:
            sum = sum + self.answer_key[self.answers[i]]
        return sum

Q5 = multiple(Q5P,Q5A,Q5K)
Q6 = multiple(Q6P,Q6A,Q6K)
Q7 = multiple(Q7P,Q7A,Q7K)