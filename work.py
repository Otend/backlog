# -*- coding: utf-8 -*-
#import random
import time


class Work():
    def __init__(self, name):
        self.name = name
        self.addedTime = time.time()
        self.wasViewed = False

    def changeName(self, newName):
        self.name = newName
