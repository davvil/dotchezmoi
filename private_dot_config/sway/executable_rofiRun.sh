#!/bin/bash

cd $(dirname $0)

source rofiMonitor.sh

monitor=`get_monitor`

rofi -monitor $monitor -modi drun,run -show drun -show-icons -lines 5
