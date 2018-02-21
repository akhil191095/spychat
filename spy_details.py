from datetime import datetime

class Spy:
    def __init__(self, name, age, rating ):
        self.name = name
        self.age = age
        self.rating = rating

        self.current_status_message = None

spy = Spy("Mr.Akhil", 24, 4.2  )


class friend:
    def __init__(self, name, age, rating):
        self.name = name
        self.age = age
        self.rating = rating
        self.chat = []
        self.current_status_message = None
friend_one = friend("Mr.Akshay",26,3.6)
friend_two = friend("Mr.Rohit",27,3.8 )
friend_three = friend("Ms.Priya",22,3.2  )

friends = [friend_one,friend_two,friend_three]


class ChatMessage:
    def __init__(self, sender, message_sent_to, message, sent_by_me):
        self.name_of_sender = sender
        self.message_sent_to = message_sent_to
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
