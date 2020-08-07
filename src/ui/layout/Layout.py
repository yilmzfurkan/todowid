from abc import ABC, abstractmethod


# Created by orhantgrl
# created on 8/7/20

class Layout(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def __draw__(self):
        pass
