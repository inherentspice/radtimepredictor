from termcolor import colored

def rad_time(test=False):
    """Tell the computer what your plan is for the
    day and it will tell you whether you will have
    a rad time"""

    if test==True:
        return "I see you test."

    string = input(colored("Tell me your plans for the day and I will tell you its raditude:", 'yellow'))
    answer_decoded = string.split(" ")

    rad_time_terms = ['code', 'coding', 'python', 'le wagon',
                'coffee', 'cat']

    for i in answer_decoded:
        if i.lower() in rad_time_terms:
            print(colored("Hell yeah, you're gonna have a rad time.", "green"))
            return
    else:
        print(colored("Man, what a bummer, maybe, like, revise your priorities", "red"))
        return
