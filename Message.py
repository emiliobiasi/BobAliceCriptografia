class Message:

    def __init__(self, from_x, to_y, message):
        self.from_x = from_x
        self.to_y = to_y
        self.message = message

    def __str__(self):
        return self.from_x, self.to_y, self.message

    def to_json(self):
        json = {
            "from": self.from_x,
            "to": self.to_y,
            "message": self.message
        }
        return json
