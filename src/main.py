#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import redis
import os

from prompt_toolkit import prompt, AbortAction
from prompt_toolkit.history import FileHistory
from prompt_toolkit.contrib.completers import WordCompleter

from redis_lexer import RedisLexer
from redis_words import get_redis_words
from style import DocumentStyle




def main():
    home = os.environ["HOME"]
    history = FileHistory(home+'/.rdcli-history')
    connection = redis.StrictRedis(host='localhost', port=6379, db=0)

    while True:
        try:
            text = prompt('> ', lexer=RedisLexer, completer=get_redis_words(),
                          style=DocumentStyle, history=history,
                          on_abort=AbortAction.RETRY).strip()
        except EOFError:
            break  # Control-D pressed.

        messages = connection.execute_command(text)
        if (text.split(" ")[0].upper() == "HGETALL"):
            i=0
            name = ""
            for message in messages:
                if (i % 2):
                    print("{0}: \t\t\"{1}\"".format(name, message))
                else:
                    name = message
                i+=1
        elif (text.split(" ")[0].upper() == "COMMAND"):
            for message in messages:
                print message


        else:
            print(messages)



    print('GoodBye!')

if __name__ == '__main__':
    main()
