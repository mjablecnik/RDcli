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
    def command(cmd):
        if (text.split(" ")[0].upper() == cmd):
            return True


    home = os.environ["HOME"]
    history = FileHistory(home+'/.rdcli-history')
    connection = redis.StrictRedis(host='localhost', port=6379, db=0)
    print("     *** Welcome in RDcli (CLI for Redis) ***")
    print("You can exit program by type QUIT or shortcut C-D \n")
    

    while True:
        try:
            text = prompt('> ', lexer=RedisLexer, completer=get_redis_words(),
                          style=DocumentStyle, history=history,
                          on_abort=AbortAction.RETRY).strip()
        except EOFError:
            break  # Control-D pressed.

        try:
            messages = connection.execute_command(text)
            if command("HGETALL"):
                i=0
                name = ""
                for message in messages:
                    if (i % 2):
                        print("{0}: \t\t\"{1}\"".format(name, message))
                    else:
                        name = message
                    i+=1
            elif command("COMMAND"):
                for message in messages:
                    print message

            elif command("KEYS"):
                for message in messages:
                    print message

                print ""
                print "Number of keys: " + str(len(messages))

            elif command("QUIT"):
                break

            else:
                print(messages)
        except Exception as e:
            print(e)


    print('GoodBye!')

if __name__ == '__main__':
    main()
