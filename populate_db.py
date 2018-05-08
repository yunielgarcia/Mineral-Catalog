import json
import os


def dict_formatted(dict):
    corrected_dict = {k.replace(' ', '_'): v for k, v in dict.items()}
    return corrected_dict


def load_json_setup():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mineral_catalog.settings")

    # And we need to start up the apps
    from django.core.wsgi import get_wsgi_application

    get_wsgi_application()


def populate_db_with_minerals():
    from minerals.models import Mineral

    mineral_json_data = open('minerals.json')
    minerals = json.load(mineral_json_data)

    for mineral in minerals:
        # import pdb;pdb.set_trace()
        min_dict = dict_formatted(mineral)
        # import pdb;pdb.set_trace()
        Mineral(**min_dict).save()


if __name__ == '__main__':

    load_json_setup()
    populate_db_with_minerals()
