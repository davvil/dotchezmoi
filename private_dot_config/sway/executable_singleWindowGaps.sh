#!/bin/bash

screenWidth=$(swaymsg -t get_outputs | jq -r '.[] | select(.focused) | .rect | .width')
swaymsg gaps horizontal current toggle $((screenWidth * 20/100))

