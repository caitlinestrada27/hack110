"""helpers class."""

class todo:
    """Docstring."""

    id: int
    title: str
    description: str
    
    def __init__(self, id: int, title: str, description: str):
        """Todo's constructor."""
        self.id = id
        self.title = title
        self.description = description