"""___"""
import random
import string
import datetime
import logging

from flask import render_template, request, redirect, url_for, session, flash
from flask_login import login_required
# internal
from app.db import db_handler

from . import note


@note.route("/noteview" , methods=['GET', 'POST'])
def note_view():
    note_data = "" # db_handler.db_all_note()
    result = "Null"
    if request.method == 'POST':
        # get by topic
        if request.form["action"] == "GetTopic":
            topic = request.form["selectvaluetopic"]
            topic_result = db_handler.db_get_by_topic(topic)
            if len(topic_result) < 2:
                result = "No data saved for topic: " + format(topic)
            return render_template("note/notes_view.html", note_data=topic_result, result=result)
        # get all
        elif request.form["action"] == "GetAll":
            note_data = db_handler.db_all_note()
            return render_template("note/notes_view.html", note_data=note_data, result=result)
        else:
            pass

    # get plain
    return render_template("note/notes_view.html", note_data=note_data, result=result)
    

@note.route("/noteadmin", methods=['GET', 'POST'])
@login_required
def notes_db():
    note_data = db_handler.db_all_note()
    result = "Get all"
    current_time = datetime.datetime.now()
    if request.method == 'POST':
        if request.form["action"] == "Add":
            print("add admin")
            #db logger add
            note = request.form["nt"]
            # drop = request.form["drop_option"]
            topic = request.form["selectvalueadd"]
            # level_ = request.form["options"]
            topic_url = request.form["url"]
            if len(note) < 5 or len(topic_url) < 6:
                result = "Note must be > 5 and url must be > 6"
            else:
                result = db_handler.db_insert_note(note, topic, topic_url)
               
                
        elif request.form["action"] == "DeleteNote":
                notes_id = request.form["delid"]
                result = db_handler.db_delete_note(notes_id)
                
        else:
            pass
    else:
        result = "GET: " + str(current_time)
           
        return render_template("note/notes_admin.html", note_data=note_data, result=result)

    return render_template("note/notes_admin.html", note_data=note_data, result=result)



