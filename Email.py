class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}'


emails = []

while True:
    command = input()
    if command == 'Stop':
        break

    tokens = command.split(' ')
    sender = tokens[0]
    receiver = tokens[1]
    content = tokens[2]
    email = Email(sender, receiver, content)
    emails.append(email)

send_emails = list(map(lambda x: int(x), input().split(', ')))

for x in send_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())