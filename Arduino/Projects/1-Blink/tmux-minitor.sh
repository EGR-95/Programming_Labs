#!/bin/bash
tmux new-session -d -s arduino-monitor "screen /dev/ttyUSB0 9600"
tmux attach -t arduino-monitor

