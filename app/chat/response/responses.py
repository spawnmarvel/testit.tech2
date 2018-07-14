import random

class Responses():

    def __init__(self):
        self.link = ""

    def get_bad_response(self):
        response = ["Say what dog?... ", "Eh...almost.. ", "Nope, hihi ", "Who the heck was your teacher? ", "Come on"]
        answer = random.choice(response)
        return answer

    def get_nan_response(self):
        response = ["A number is from 0 to 999999999, or just 42 ", "No, no, no..are you getting old, a number please ", "Wow, you can write letters, is that the answer to the question? ", "That was not a number... ", "Type a nr... "]
        answer = random.choice(response)
        return answer

    def set_reward(self, valid):
        if valid:
            self.link = " https://www.psychologytoday.com/blog/eyes-the-brain/201101/how-grow-new-neurons-in-your-brain"
        else:
            self.link = ""
        return self.link

    def get_response_reward(self):
        return self.link

