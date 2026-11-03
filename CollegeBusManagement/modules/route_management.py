from CollegeBusManagement.database import DATABASE_PATH, connect, transaction
from CollegeBusManagement.models.route import Route
from CollegeBusManagement.utils.validation import positive_integer, require_text


def add_route(route: Route, database_path=DATABASE_PATH) -> int:
    with transaction(database_path) as connection:
        cursor = connection.execute(
            "INSERT INTO routes(route_name, starting_point, destination) VALUES (?, ?, ?)",
            (require_text(route.route_name, "Route name"),
             require_text(route.starting_point, "Starting point"),
             require_text(route.destination, "Destination")),
        )
        return int(cursor.lastrowid)


def update_route(route_id: int, route: Route, database_path=DATABASE_PATH) -> None:
    with transaction(database_path) as connection:
        cursor = connection.execute(
            "UPDATE routes SET route_name=?, starting_point=?, destination=? WHERE id=?",
            (require_text(route.route_name, "Route name"),
             require_text(route.starting_point, "Starting point"),
             require_text(route.destination, "Destination"), route_id),
        )
        if not cursor.rowcount:
            raise LookupError("Route was not found.")


def delete_route(route_id: int, database_path=DATABASE_PATH) -> None:
    with transaction(database_path) as connection:
        connection.execute(
            "UPDATE students SET bus_id=NULL, seat_number=NULL WHERE bus_id IN "
            "(SELECT id FROM buses WHERE route_id=?)", (route_id,),
        )
        connection.execute(
            "UPDATE students SET route_id=NULL, pickup_stop_id=NULL WHERE route_id=?",
            (route_id,),
        )
        connection.execute("UPDATE buses SET route_id=NULL WHERE route_id=?", (route_id,))
        connection.execute("DELETE FROM routes WHERE id=?", (route_id,))


def add_stop(route_id: int, stop_name: str, stop_order: int, database_path=DATABASE_PATH) -> int:
    order = positive_integer(str(stop_order), "Stop order")
    with transaction(database_path) as connection:
        if not connection.execute("SELECT 1 FROM routes WHERE id=?", (route_id,)).fetchone():
            raise LookupError("Route was not found.")
        cursor = connection.execute(
            "INSERT INTO stops(route_id, stop_name, stop_order) VALUES (?, ?, ?)",
            (route_id, require_text(stop_name, "Stop name"), order),
        )
        return int(cursor.lastrowid)


def update_stop(stop_id: int, stop_name: str, stop_order: int, database_path=DATABASE_PATH) -> None:
    with transaction(database_path) as connection:
        cursor = connection.execute(
            "UPDATE stops SET stop_name=?, stop_order=? WHERE id=?",
            (require_text(stop_name, "Stop name"),
             positive_integer(str(stop_order), "Stop order"), stop_id),
        )
        if not cursor.rowcount:
            raise LookupError("Stop was not found.")


def delete_stop(stop_id: int, database_path=DATABASE_PATH) -> None:
    with transaction(database_path) as connection:
        connection.execute("UPDATE students SET pickup_stop_id=NULL WHERE pickup_stop_id=?", (stop_id,))
        connection.execute("DELETE FROM stops WHERE id=?", (stop_id,))


def list_routes(database_path=DATABASE_PATH) -> list:
    with connect(database_path) as connection:
        return connection.execute(
            "SELECT r.*, GROUP_CONCAT(DISTINCT b.bus_number) AS assigned_buses, "
            "COUNT(DISTINCT s.id) AS stop_count "
            "FROM routes r LEFT JOIN buses b ON b.route_id=r.id "
            "LEFT JOIN stops s ON s.route_id=r.id "
            "GROUP BY r.id ORDER BY r.route_name"
        ).fetchall()


def list_stops(route_id: int | None = None, database_path=DATABASE_PATH) -> list:
    with connect(database_path) as connection:
        if route_id is None:
            return connection.execute(
                "SELECT stops.*, routes.route_name FROM stops JOIN routes ON routes.id=stops.route_id "
                "ORDER BY routes.route_name, stops.stop_order"
            ).fetchall()
        return connection.execute(
            "SELECT * FROM stops WHERE route_id=? ORDER BY stop_order", (route_id,)
        ).fetchall()
