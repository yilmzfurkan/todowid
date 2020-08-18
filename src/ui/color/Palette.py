from abc import ABC, abstractmethod


# Created by orhantgrl
# created on 8/17/20

class Palette(ABC):
    def __init__(self, ):
        super().__init__()

    @abstractmethod
    def __getpalette__(self):
        pass
