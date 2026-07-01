class ConversationMemory:

    def __init__(self):

        self.messages = []

    def add(self, role, message):

        self.messages.append(

            {

                "role": role,

                "message": message

            }

        )

    def clear(self):

        self.messages = []