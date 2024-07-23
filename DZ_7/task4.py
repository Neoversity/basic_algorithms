class Comment:
    def __init__(self, text, author):
        """
        Ініціалізує коментар з текстом, автором та списком відповідей.
        
        Аргументи:
        text: Текст коментаря.
        author: Автор коментаря.
        """
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        """
        Додає відповідь до коментаря.
        
        Аргументи:
        reply: Об'єкт класу Comment, який є відповіддю.
        """
        self.replies.append(reply)

    def remove_reply(self):
        """
        Видаляє коментар, змінюючи його текст на "Цей коментар було видалено."
        та встановлюючи прапорець is_deleted в True.
        """
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, indent=0):
        """
        Рекурсивно виводить коментар та всі його відповіді з відповідними відступами.
        
        Аргументи:
        indent: Кількість відступів для відображення ієрархічної структури.
        """
        print("    " * indent + f"{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(indent + 1)