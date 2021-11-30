import json
import re

BOOKS_FILE = "books.md"
BOOK_REGEX = ...  # TODO записать ругулярное выражения для поиска книги


def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))


if __name__ == '__main__':
    task()


####\s(?P<position>\d+)\.\s\[(?P<book>.+)]\((?P<book_url>https://amzn\.to/\w+)\) by (?P<author>[a-zA-Z]+ [a-zA-Z]+) \((?P<recommended>\d{1,3}\.\d+%)\srecommended\)\s!\[\]\((?P<cover_url>.+?)\)\s+