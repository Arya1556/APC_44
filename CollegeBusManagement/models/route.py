from dataclasses import dataclass


@dataclass
class Route:
    route_name: str
    starting_point: str
    destination: str


@dataclass
class Stop:
    stop_name: str
    route_id: int
    stop_order: int
