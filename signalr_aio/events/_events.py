#!/usr/bin/python
# -*- coding: utf-8 -*-

# signalr_aio/events/_events.py
# Stanislav Lazarov

# Structure inspired by https://github.com/TargetProcess/signalr-client-py


class EventHook(object):
    def __init__(self):
        self._handlers = []

    def __iadd__(self, handler):
        self._handlers.append(handler)
        return self

    def __isub__(self, handler):
        self._handlers.remove(handler)
        return self

    async def fire(self, *args, **kwargs):
        for handler in self._handlers:
            try:
                await handler(*args, **kwargs)
            except Exception as e:
                print(f"🔥 Handler {handler.__name__} crashed with: {e}")

    #async def fire(self, *args, **kwargs):
     #   print(self._handlers)
      #  print(args)
       # for handler in self._handlers:
        #    await handler(*args, **kwargs)
