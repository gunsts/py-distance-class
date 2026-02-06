from typing import Any


class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers"

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Distance:
        new_km = other.km if isinstance(other, Distance) else other
        return Distance(self.km + new_km)

    def __iadd__(self, other: Any) -> Distance:
        new_km = other.km if isinstance(other, Distance) else other
        return Distance(self.km + new_km)

    def __mul__(self, other: Any) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: Any) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: Any) -> bool:
        new_km = other.km if isinstance(other, Distance) else other
        return self.km < new_km

    def __gt__(self, other: Any) -> bool:
        new_km = other.km if isinstance(other, Distance) else other
        return self.km > new_km

    def __eq__(self, other: Any) -> bool:
        new_km = other.km if isinstance(other, Distance) else other
        return self.km == new_km

    def __le__(self, other: Any) -> bool:
        new_km = other.km if isinstance(other, Distance) else other
        return self.km <= new_km

    def __ge__(self, other: Any) -> bool:
        new_km = other.km if isinstance(other, Distance) else other
        return self.km >= new_km
