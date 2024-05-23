import unittest
from tuples import (get_coordinate,
                    convert_coordinate,
                    create_record)


class TisburyTreasureTest(unittest.TestCase):

    def test_get_coordinate(self):
        input_data = [('Scrimshawed Whale Tooth', '2A'),
                      ('Brass Spyglass', '4B'),
                      ('Robot Parrot', '1C'),
                      ('Glass Starfish', '6D'),
                      ('Vintage Pirate Hat', '7E'),
                      ('Pirate Flag', '7F'),
                      ('Crystal Crab', '6A'),
                      ('Model Ship in Large Bottle', '8A'),
                      ('Angry Monkey Figurine', '5B'),
                      ('Carved Wooden Elephant', '8C'),
                      ('Amethyst  Octopus', '1F'),
                      ('Antique Glass Fishnet Float', '3D'),
                      ('Silver Seahorse', '4E')]

        result_data = ['2A', '4B', '1C', '6D', '7E', '7F', '6A', '8A', '5B', '8C', '1F', '3D', '4E']

        for variant, (item, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', item=item, expected=expected):
                actual_result = get_coordinate(item)
                error_message = (f'Called get_coordinate({item}). '
                                 f'The function returned "{actual_result}", but '
                                 f'the tests expected "{expected}" as the coordinates.')

                self.assertEqual(actual_result, expected, msg=error_message)

    def test_convert_coordinate(self):
        input_data = ['2A', '4B', '1C', '6D', '7E', '7F',
                      '6A', '8A', '5B', '8C', '1F', '3D', '4E']
        result_data = [('2', 'A'),
                       ('4', 'B'),
                       ('1', 'C'),
                       ('6', 'D'),
                       ('7', 'E'),
                       ('7', 'F'),
                       ('6', 'A'),
                       ('8', 'A'),
                       ('5', 'B'),
                       ('8', 'C'),
                       ('1', 'F'),
                       ('3', 'D'),
                       ('4', 'E')]

        for variant, (item, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', item=item, expected=expected):
                actual_result = convert_coordinate(item)
                error_message = (f'Called convert_coordinate({item}). '
                                 f'The function returned {actual_result}, but the '
                                 f'tests expected {expected} as the converted coordinate.')

                self.assertEqual(actual_result, expected, msg=error_message)

    def test_create_record(self):
        input_data = [
            (('Angry Monkey Figurine', '5B'), ('Stormy Breakwater', ('5', 'B'), 'Purple')),
            (('Carved Wooden Elephant', '8C'), ('Foggy Seacave', ('8', 'C'), 'Purple')),
            (('Amethyst  Octopus', '1F'), ('Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow')),
            (('Antique Glass Fishnet Float', '3D'), ('Spiky Rocks', ('3', 'D'), 'Yellow')),
            (('Silver Seahorse', '4E'), ('Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow')),
            (('Amethyst  Octopus', '1F'), ('Seaside Cottages', ('1', 'C'), 'Blue')),
            (('Angry Monkey Figurine', '5B'), ('Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow')),
            (('Antique Glass Fishnet Float', '3D'), ('Deserted Docks', ('2', 'A'), 'Blue')),
            (('Brass Spyglass', '4B'), ('Spiky Rocks', ('3', 'D'), 'Yellow')),
            (('Carved Wooden Elephant', '8C'), ('Abandoned Lighthouse', ('4', 'B'), 'Blue'))
        ]
        result_data = [
            ('Angry Monkey Figurine', '5B', 'Stormy Breakwater', ('5', 'B'), 'Purple'),
            ('Carved Wooden Elephant', '8C', 'Foggy Seacave', ('8', 'C'), 'Purple'),
            ('Amethyst  Octopus', '1F', 'Aqua Lagoon (Island of Mystery)', ('1', 'F'), 'Yellow'),
            ('Antique Glass Fishnet Float', '3D', 'Spiky Rocks', ('3', 'D'), 'Yellow'),
            ('Silver Seahorse', '4E', 'Hidden Spring (Island of Mystery)', ('4', 'E'), 'Yellow'),
            'not a match',
            'not a match',
            'not a match',
            'not a match',
            'not a match'
        ]

        for variant, (item, expected) in enumerate(zip(input_data, result_data), start=1):
            with self.subTest(f'variation #{variant}', item=item, expected=expected):
                actual_result = create_record(item[0], item[1])
                error_message = (f'Called create_record({item[0]},{item[1]}). '
                                 f'The function returned '
                                 f'{actual_result}, but the tests expected '
                                 f'{expected} for the record.')

                self.assertEqual(actual_result, expected, msg=error_message)
