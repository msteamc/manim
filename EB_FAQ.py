import os
import pyclbr

from manimlib.imports import *
from manimlib.constants import *

class HelloWorld(Scene):
    def construct(self):
        helloWorld = TextMobject("Hello Worl!")
        self.play(Write(helloWorld),run_time = 6)
        self.wait()
