function get_monitor() {
  local geo_string=$(swaymsg -t get_outputs | jq -r '.[] | select(.focused) | .rect | (.width | tostring) + "x" + (.height | tostring) + "+" + (.x | tostring) + "+" + (.y | tostring)')
  xrandr | grep $geo_string | cut -d " " -f 1
}

