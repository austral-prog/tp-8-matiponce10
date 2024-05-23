"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate.

    :param record: tuple - with a (treasure, coordinate) pair.
    :return: str - the extracted map coordinate.
    """

    _, coordinate = record
    return coordinate


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components.

    :param coordinate: str - a string map coordinate
    :return: tuple - the string coordinate split into its individual components.
    """

    return (coordinate[:-1], coordinate[-1])


def compare_records(treasure_coordinate, location_record):
    treasure, t_coordinate = treasure_coordinate
    location, l_coordinate, quadrant = location_record

    # Convertir las coordenadas a un formato común para comparación
    t_coordinate_converted = convert_coordinate(t_coordinate)
    return t_coordinate_converted == l_coordinate


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group.

    :param azara_record: tuple - a (treasure, coordinate) pair.
    :param rui_record: tuple - a (location, coordinate, quadrant) trio.
    :return: tuple or str - the combined record (if compatible), or the string "not a match" (if incompatible).
    """

    treasure, t_coordinate = azara_record
    location, l_coordinate, quadrant = rui_record

    if compare_records(azara_record, rui_record):
        return (treasure, t_coordinate, location, l_coordinate, quadrant)
    else:
        return "not a match"
