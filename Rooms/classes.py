

class Solution:
    def __init__(self, values):
        self.dictionary = {}
        self.set_values(values)
    
    def set_values(self, values):
        for i, v in enumerate(values):
            self.dictionary[i+1] = v

    def __repr__(self):
        return str(self.dictionary)

class Person:
    def __init__(self, id, room_id=None):
        self.room_id = room_id
        self.id = id

class Room:
    def __init__(self, id, beds):
        self.id = id
        self.beds = beds

class Bed:
    def __init__(self, id, person_id=None):
        self.id = id
        self.person_id = person_id
        self.taken = False