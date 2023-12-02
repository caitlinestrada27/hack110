"""Movie class."""

class Movie:

    title: str
    mcu_year: float
    release_year: int

    def __init__(self, name: str, timeline_point: float, release: int):
        """Movie's constructor."""
        self.title = name
        self.mcu_year = timeline_point
        self.release_year = release