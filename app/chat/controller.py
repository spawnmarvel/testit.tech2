
import random

from .response import responses, stack
ai_response = responses.Responses()

math_stack = stack.Stack()
math_stack.push(2)
math_stack.push(2)

state = "initial"

first = 0
second = 0
progress = 0


def set_response_reward(valid):
    ai_response.set_reward(valid)

def get_response_reward():
    return ai_response.get_response_reward()

def clear_response_reward():
    ai_response.set_reward(False)
def get_progress():
    global progress
    return progress


def set_progress(amount):
    global progress
    progress = amount

def get_state():
    global state
    return state

def set_state(new_state):
    global state
    state = new_state

def greeting(): 
    output_response = ["Hi you", "Hello to you too", "At last, someone is here", "Finally, not just me.."]
    rv = random.choice(output_response) + ", please just say something..."
    return rv

def answer_positive(): 
    output_response = ["Nice, me too", "Ok, deal"]
    rv = random.choice(output_response)
    return rv

def answer_negative(): 
    output_response = ["Why the long face?", "Really?", "Sorry for that"]
    rv = random.choice(output_response)
    return rv

def number_check(data_in):
    return any(i.isdigit() for i in data_in)

def check_answer(data_in):
    rv = "Ah, ...no answer, huh.."
    input_ans_pos = ["yes", "agree", "ok", "deal"]
    for ans in input_ans_pos:
        if ans in data_in.lower():
            rv = answer_positive()

    input_ans_neg = ["no", "nope", "never", "sorry"]
    for ans in input_ans_neg:
        if ans in data_in.lower():
            rv = answer_negative()
    return rv

def check_greeting(data_in):
    rv = "Hm...no even a duplicate Hi?"
    input_hi = ["hi", "hello", "good day", "greetings", "how"]
    for greet in input_hi:
        if greet == data_in.lower():
            rv = greeting()
    return rv

def validate_input(data_in):
    valid = False
    try:
        if len(data_in) > 1:
            valid = True
    except TypeError:
        pass
    return valid

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def multiplication():
    mult_li = []
    x = random.randint(1,11)
    y = random.randint(1,11)
    answer = x * y
    mult_li.append(x)
    mult_li.append(y)
    mult_li.append(answer)
    return mult_li

def conversation(data_in, state_in):
    #use sentence here
    li = []
    rv = ""
    # state
    if state_in == "initial":
        rv = "Waking up, be-bo-di"
        set_state("start")

    # work
    if state_in == "start":
        if validate_input(data_in):
            result_response = check_greeting(data_in)
            rv = result_response
            set_progress(5)
            set_state("greeting")
        else:
            rv = "A malfunction, error, error, please say Hi"
            set_state("start")  
    
    elif state_in == "greeting":
        rv = "Greeting...."
        if validate_input(data_in):
            rv = "Let's do math, multiplication, type yes or no"
            set_state("math")
        else:
            rv = "Eh, math now, type math or whatever you like."
            set_state("greeting")

    elif state_in == "math":
        if validate_input(data_in):
            rv = "You typed something, great, let's do multiplication"
            set_state("mult")
        else:
            wait_response = ["So you like to say nothing?", "Ah, the silent one, may the force be with you", "Come on....", "Are you human?", "Look at yourself, hu..", "Questions is, can you handle it?"]
            wait = random.choice(wait_response)
            rv = wait+  ". Yes or no, please!"
            set_state("math")
    
    elif state_in == "mult":
        global first
        global second
        m_li = multiplication()
        first = m_li[0]
        second = m_li[1]
        rv = "What is " + str(first) + " *  " + str(second)
        #rv = "Get ready for math"
        set_state("thinking")
        

    elif state_in == "thinking":
        global first
        global second
        
        bad_user = ai_response.get_bad_response()
        answer_this = " What is " + str(first) + " * " + str(second)
        if is_number(data_in):
            answer = int(first) * int(second)
            user_try = int(data_in)
            if get_progress() >= 20:
                rv = "We have a champion with " + str(get_progress()) + " points."
                set_response_reward(True)
                set_state("math")
            else:
                try:
                    if user_try == answer:
                        rv = "Great, you did it, ready for next, press chat"
                        set_state("mult")
                        set_progress(get_progress() + 5)
                    else:
                        if user_try > answer:
                            rv = bad_user +  ". Sorry, try again, to high. " + answer_this # + " result " + str(answer)
                            set_state("thinking")
                        else:
                            rv =  bad_user +  ". Sorry, try again, to low. " + answer_this # + " result " + str(answer)
                            set_state("thinking")
                except ValueError:
                    rv = "Please give a number. " + answer_this #  + " result " + str(answer)
                    set_state("thinking")
                except TypeError:
                    rv = "You did not pass anything. " + answer_this # + " result " + str(answer)
                    set_state("thinking")
        else:
            rv = ai_response.get_nan_response() + answer_this
            set_state("thinking")
        
    # rv += " (" + data_in + ")"
    li.append(rv)
    li.append(get_state())
    return li




        