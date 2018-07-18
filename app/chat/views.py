"""___"""
import logging
from flask import render_template, request, flash, session
from flask import make_response
from functools import wraps, update_wrapper
from datetime import datetime
import random
import datetime as dt
from . import controller as controller
from .model import chatbot as chatbot
from .model import human as human
from . import chat

 # conversation_list = []


# start_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# initial_tup = ("......","Hi, I am your chatbot, please say hi",start_time)
# conversation_list.append(initial_tup)




def get_chat_time():
     chat_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     return chat_time


@chat.route('/chat',methods = ['POST', 'GET'])
def result():
    # new controller on visit, remove all global vars
    rv_session = 0
    progress = controller.get_progress()
    robot_data = ""
    conversation_list = []
    start_time = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    initial_tup = ("......","Hi, I am your chatbot, please say hi",start_time)
    conversation_list.append(initial_tup)
    tmp_list = []
    chat_counter = len(conversation_list)
    chat_time = get_chat_time()
    

    tmp_state = controller.get_state()

    if request.method == 'POST':


        if request.form["action"] == "Chat":

            if "conversation" in session:
                session["conversation"] = session.get("conversation") + 1
            else:
                session["conversation"] = 1 #first entry
            rv_session = "Session " + format(session.get("conversation"))
            # user input
            tmp_user_data = request.form["chat_text"]
            user_data = str(tmp_user_data)
            # robot input based on user input
            
            #15.01.2018 moved getstate to before post
            tmp_state = controller.get_state()
            tmp_li = controller.conversation(user_data, tmp_state)
           
           
            robot_data = tmp_li[0]
            tmp_state = tmp_li[1]
            # instances
            #if we need the state for logging
            # human_current = human.Human(user_data + " : (state:" + tmp_state + ")")
            #state is gone, just input
            human_current = human.Human(user_data)
            chatbot_current = chatbot.ChatBot(robot_data)
            # tuple of current conversation
            conversation_tup = (human_current.statment, chatbot_current.statment, get_chat_time())
            # insert at the beginning of the list, to render that first
            conversation_list.insert(0, conversation_tup)
            # debug
        
       
            
            # logger.debug(conversation_list)
        elif request.form["action"] == "Clear":
            conversation_list = []
            start_fresh_tup = ("Human had to think...","Ok, we start again, I am your chatbot. Learning, learning. Please say Hi.",)
            conversation_list.append(start_fresh_tup)
            controller.set_state("initial")
            controller.set_progress(5)
            rv_session = format(session.pop("conversation", None))
        else:
            pass


        # conversation_list.reverse()
    # else:
        # conversation_list.reverse()
        #is GET
        
        # return render_template("chat/chat.html", conversation_list = conversation_list, chat_time = chat_time, progress = progress, rv_session=rv_session)
    return render_template("chat/chat.html", conversation_list = conversation_list, chat_time = chat_time, progress = progress, rv_session=rv_session)
