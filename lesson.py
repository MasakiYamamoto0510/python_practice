# from lesson_package.talk import *
#
# print(animal.sing())
# print(animal.cry())
#
# print(human.sing())
# print(human.cry())

try:
  from lesson.package import tools
except ImportError:
    from lesson_package.tools import utils

utils.say_twice('word')
