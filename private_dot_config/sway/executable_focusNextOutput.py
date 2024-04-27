#!/usr/bin/env python3
"""Temporary solution until ""focus output next" is supported in sway."""


import i3ipc


def main():
  i3 = i3ipc.Connection()
  for c in i3.get_tree().nodes:
    if c.type != "output":
      # Probably doesn't happen
      continue
    if c.name == "__i3":
      continue
    if c.find_focused() is None:
      i3.command(f"focus output {c.name}")
      break


if __name__ == "__main__":
  main()
