
from database.meteo_dao import MeteoDao


class Model:
    def __init__(self):
        pass

    def get_umidita_media(self, mese):
        res = MeteoDao.get_umidita_media(mese)
        print("Sono arrivato al modelll")
        pass