#!/bin/bash
tmux send-keys "source rdcli-dev/bin/activate" Enter
tmux send-keys "pip install -r requirements.txt" Enter
tmux send-keys "clear" Enter
tmux send-keys "python src/main.py" Enter

