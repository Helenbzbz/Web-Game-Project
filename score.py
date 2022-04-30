# This code wll read the result file and return the days an individual can survive

from single import Q1,Q2,Q3,Q4,Q8,Q9,Q10,Q11
from multiple import Q5, Q6, Q7

def score():
    f = open('result.txt')
    words = f.readlines()
    a = Q1.score(words[0].strip())
    b = Q2.score(words[1].strip())
    c = Q3.score(words[2].strip())
    d = Q4.score(words[3].strip())
    e = Q5.score(words[4].strip())
    f = Q6.score(words[5].strip())
    g = Q7.score(words[6].strip())
    h = Q8.score(words[7].strip())
    i = Q9.score(words[8].strip())
    j = Q10.score(words[9].strip())
    k = Q11.score(words[10].strip())
    days = int(((a+b+c+d+e+f+g+h)*(1+i)+j)*(1+k))
    return days
score()

def day_year(a):
    year = int(a/365)
    day = a%365
    return f'{year} year(s), {day} days'

def category(a):
    if a <=10:
        return'You died fast with most people at the beginninng of the diaster./n'
    if 10 <a <=60:
        return'You tried but failed. What were you thinking when you died?'
    if 60 < a <= 180:
        return 'Months passed. Do you feel lonely when you died?'
    if 180 < a <= 360:
        return 'You\'ve utilized all the resources you can. Where is the future of human?'
    if 360 < a:
        return 'It\'s just one year, but you feel the normal life was that away from you.'