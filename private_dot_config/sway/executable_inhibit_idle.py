#!/usr/bin/env python3

import i3ipc
import signal

CHECK_INTERVAL_SEC = 60

def traverseTree(container):
    if not container.nodes:
        yield container
    else:
        for n in container.nodes:
            yield from traverseTree(n)

def inhibitCondition(container):
  # Not sure why we have to test for container.name
  return (container.window_class == "Google-chrome" or container.app_id == "google-chrome") \
    and container.name is not None and container.name.startswith("Meet ")

def checkContinueInhibit(signal_number, stack_frame):
  tree = i3.get_tree()
  inhibiting_windows = []
  should_inhibit = False
  for w in traverseTree(tree):
    should_inhibit = should_inhibit or inhibitCondition(w)
    if w.ipc_data.get("inhibit_idle"):
      inhibiting_windows.append(w)
  if not should_inhibit:
    for w in inhibiting_windows:
      w.command('inhibit_idle fullscreen')
  else:
    # Check again later
    signal.alarm(CHECK_INTERVAL_SEC)

def checkNewInhibit(i3, e):
    if inhibitCondition(e.container):
      e.container.command('inhibit_idle open')
      signal.alarm(CHECK_INTERVAL_SEC)

if __name__ == "__main__":
    i3 = i3ipc.Connection()
    i3.on("window::new", checkNewInhibit)
    i3.on("window::title", checkNewInhibit)
    signal.signal(signal.SIGALRM, checkContinueInhibit)

    i3.main()
