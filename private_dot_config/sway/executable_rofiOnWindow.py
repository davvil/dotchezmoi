#!/usr/bin/env python3

import sys

import i3ipc


def look_for_focused(node, output_rect):
  if node.type == "output":
    output_rect = node.rect
  elif node.focused:
    print(
        "anchor: north west; "
        "location: north west; "
        f" x-offset: {node.rect.x - output_rect.x};"
        #~ f" y-offset: {node.rect.y - output_rect.y};"
        f" y-offset: {node.rect.y - output_rect.y - 26};"  # Why 26? I have no clue. Waybar?
        f" height: {node.rect.height};"
        f" width: {node.rect.width};"
    )
    return
  for n in node.nodes:
    look_for_focused(n, output_rect)


def main():
  i3 = i3ipc.Connection()
  tree = i3.get_tree()
  look_for_focused(tree, None)



if __name__ == "__main__":
  main()
