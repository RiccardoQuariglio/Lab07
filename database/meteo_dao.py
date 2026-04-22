from database.DB_connect import DBConnect
from model.situazione import Situazione


class MeteoDao():

    @staticmethod
    def get_all_situazioni():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT s.Localita, s.Data, s.Umidita
                        FROM situazione s 
                        ORDER BY s.Data ASC"""
            cursor.execute(query)
            for row in cursor:
                result.append(Situazione(row["Localita"],
                                         row["Data"],
                                         row["Umidita"]))
            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_umidita_media(mese):
        cnx = DBConnect.get_connection()

        if cnx is None:
            print("Connessione fallita")
            return

        cursor = cnx.cursor(dictionary = True)
        res = []
        query = """
                    select Localita as citta, AVG(Umidita) as umiditaMedia
                    from situazione s 
                    where extract(month from Data) = %s
                    group by Localita
                """
        cursor.execute(query)
        for row in cursor:
            res.append((row[0], row[1]))

        return res


if __name__ == "__main__":
    print(get_umidita_media(5))