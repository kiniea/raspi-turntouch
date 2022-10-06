import logging

from .base_controller import BaseController

class HomeController(BaseController):

    def perform(self, action):
      self.log(action)

    @classmethod
    def help(cls):
      return """
#Echo Module - Echo a string, nothing more.
Usage:
north_press:
  type: echo
  command: Hello North
"""
