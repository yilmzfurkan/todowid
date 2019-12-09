class TodoNotFoundException(Exception):
    """Raised when when there is no to do item"""

    def __init__(self, message):
        super().__init__(message)
