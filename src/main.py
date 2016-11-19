#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import redis

from prompt_toolkit import prompt, AbortAction
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.contrib.completers import WordCompleter

from redis_lexer import RedisLexer
from redis_words import get_redis_words
from style import DocumentStyle




def main():
    history = InMemoryHistory()
    connection = redis.StrictRedis(host='localhost', port=6379, db=0)

    while True:
        try:
            text = prompt('> ', lexer=RedisLexer, completer=get_redis_words(),
                          style=DocumentStyle, history=history,
                          on_abort=AbortAction.RETRY)
        except EOFError:
            break  # Control-D pressed.
        messages = connection.execute_command(text.strip())
        print(messages)
    print('GoodBye!')

if __name__ == '__main__':
    main()
