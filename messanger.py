class MessageBox():

    def __init__(self):
        self.operation_list = []

    def receive(self):
        self.operation_list.append(1)

    def send(self):
        self.operation_list.append(2)

    def operations(self):
        return self.operation_list

    def count_message_received(self):
        count = 0

        for o in self.operation_list:
            if o == 1:
                count += 1
        return count

    def count_message_sent(self):
        count = 0

        for o in self.operation_list:
            if o == 2:
                count += 1

        return count


mb = MessageBox()
mb.send()
mb.send()
mb.receive()
mb.receive()
mb.send()

print("List of operations:", mb.operations())
print("Number of messages recieved:", mb.count_message_received())
print("Number of messages sent:", mb.count_message_sent())
