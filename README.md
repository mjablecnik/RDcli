# rdcli

Redis command line interface with auto-completion and syntax highlighting.

Inspirated by: [mycli](http://mycli.net) and [pgcli](http://pgcli.net) 




# Local setup:

  Fork project from github and clone it:
  git clone <git-repository>
  
  go to repository:
  cd rdcli
  
  create virtualenv:
  mkdir rdcli-dev
  virtualenv rdcli-dev
  source ./rdcli-dev/bin/activate
  
  pip install -r requirements.txt
  
  python src/main.py



# Special thanks:

 - [Pygments](http://pygments.org/): Syntax highlighter.
 - [redis-py](https://github.com/andymccurdy/redis-py) : Python Redis client.
 - [Python Prompt Toolkit](https://github.com/jonathanslenders/python-prompt-toolkit): Library for building interactive command line interface.



# Authors:

 - Martin Jablečník
