#!/usr/bin/env python

class Person():
    def __init__(self, name, sex, age, lover, salary = 0):
        self.name = name
        self.sex = sex
        self.age = age
        self.lover = lover
        self.salary = salary
    def tell(self):
        print "**********\n[%s] My name is %s, I'm %s years old." % (self.name, self.name, self.age)
    def learn(self, school):
        self.school = school
        print "[%s] I learned course at %s." % (self.name, self.school)
    def interview(self, company):
        self.company = company
        print "[%s] So, I got an interview chance from: %s." % (self.name, self.company)
    def change_work(self, company):
        self.company = company
        print "[%s] I got a new job at %s." % (self.name, self.company)
    def add_salary(self, salary):
        self.salary = salary
        print "[%s] My salary is: %s now." % (self.name, self.salary)

class School():
    def __init__(self, name):
        self.name = name

class Company():
    def __init__(self, name):
        self.name = name

def cont():
    if raw_input('Continue...\n'):
        pass

def f_john():
    name = 'John'
    print "**********\n[System] Hi master, you are '%s' now, let me tell your new life..." % name.upper()
    sex = 'Male'
    age = 27
    lover = 'Liz'
    rival = 'Peter'
    p_ds = Person(name, sex, age, lover)

    p_ds.tell()

    cont()
    print "[John] %s is my lover, I meet her first time at high school, we love each other very much..." % lover

    cont()
    print "[John] After we graduated form high school, %s entered the 'Beijing City University' successfully, but I failed..." % lover

    cont()
    print "[John] I love %s very much. I went to Beijing as well, taking part time job at one web club, and paid her 4 year's tuition, just for living with her together." % lover

    cont()
    print "[John] However, the day came badlly for me. After %s graduated from the college and starting her career, she fell in love with his colleague -- %s, finnally, she left me without a word." % (lover, rival)

    cont()
    print "[John] I feel I'm going to die about it, my heart almost broken. How dare she did that to me? Is our is cheaper than money? I feel too tired to love any more..."

    cont()
    print "[John] After several days, I decide take %s back, I know all her want is money, I will hard work to earn much money which she can't spend them in all her life!" % lover

    cont()
    print "[John] For improving my ablity, I attend self-study exam, and go to school for studying."
    while True:
        s = raw_input('[System] Which school are you studying? ')
        if len(s) == 0: continue
        else:
            break
    school = School(s)
    p_ds.learn(school.name)

    cont()
    print "[John] After several months time, I finished my course, and received many company's job introduce."
    while True:
        c = raw_input('[System] Which company you will interview? ')
        if len(c) == 0: continue
        else:
            break
    company = Company(c)
    print "[John] Among them, I like %s best." % company.name
    p_ds.interview(company.name)

    cont()
    print "[John] Easyly, I pass %s's interview, and her send the offer quickly." % company.name
    p_ds.change_work(company.name)

    cont()
    print "[John] Many years later, I became rich, very rich, I am CTO at an Internation Internet company."
    p_ds.salary = int(raw_input("[System] your salary now: "))
    p_ds.add_salary(p_ds.salary)
    print "[John] I can buy anything only if I want, but I can't buy %s which I loved." % lover

    cont()
    print "[John] One day, I meet %s, we have a short conversation, she told me, %s left her, she is alone now." % (lover, rival)

    cont()
    print "[John] I told her..."

def f_peter():
    name = 'Peter'
    print "**********\n[System] Hi master, you are '%s' now, let me tell your new life..." % name.upper()
    sex = 'Male'
    age = 26
    lover = 'Liz'
    p_ds = Person(name, sex, age, lover)

    p_ds.tell()

def f_liz():
    name = 'Liz'
    print "**********\n[System] Hi master, you are '%s' now, let me tell your new life..." % name.upper()
    sex = 'Female'
    age = 26
    lover = 'Liz'
    p_ds = Person(name, sex, age, lover)

    p_ds.tell()

def main():
    print '''
***Welcome to SIMS***
You can play following role:
    J   : John
    P   : Peter
    L   : Liz
***Enjob your new life***
'''
    
    while True:
        cmd = raw_input("Role: ").strip().lower()
        if len(cmd) == 0: continue
        elif cmd == 'j':
            f_john()
        elif cmd == 'p':
            f_peter()
        elif cmd == 'l':
            f_liz()
        elif cmd == 'q':
            print 'See you next time.'
            break

if __name__ == '__main__':
    main()

