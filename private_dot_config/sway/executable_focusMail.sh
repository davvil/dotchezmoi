#!/bin/bash

#~ WS_NAME="📬"
#~ WS_NAME=""
WS_NAME="Mail"

cd `dirname $0`
currentWs=`./getCurrentWorkspace.py`
if [[ $currentWs != "$WS_NAME" ]]; then
    ./gotoWorkspace.py $WS_NAME
else
    kill -s USR1 `cat ~/.config/i3/wsBackAndForth.pid`
fi
