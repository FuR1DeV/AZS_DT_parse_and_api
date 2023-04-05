import psycopg2

from config import HOST, POSTGRESQL_USER, POSTGRESQL_PASSWORD, DATABASE


class Database:
    """Инициализируем Базу данных"""
    def __init__(self):
        self.connection = psycopg2.connect(host=HOST,
                                           user=POSTGRESQL_USER,
                                           password=POSTGRESQL_PASSWORD,
                                           database=DATABASE)
        self.connection.autocommit = True


class UpdateDB(Database):
    def update(self, latitude, longitude, dt, dt_taneko, dt_winter, dt_arctic):
        """Функция обновления таблицы"""
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO dt_azs (latitude, longitude, dt, dt_taneko, dt_winter, dt_arctic) "
                "VALUES (%(latitude)s, %(longitude)s, %(dt)s, %(dt_taneko)s, %(dt_winter)s, %(dt_arctic)s);", {
                    'latitude': latitude,
                    'longitude': longitude,
                    'dt': dt,
                    'dt_taneko': dt_taneko,
                    'dt_winter': dt_winter,
                    'dt_arctic': dt_arctic,
                }
            )
            self.connection.commit()

    def delete(self):
        """Функция очищения таблицы"""
        with self.connection.cursor() as cursor:
            cursor.execute(
                "TRUNCATE dt_azs;"
            )
            self.connection.commit()


update_obj = UpdateDB()
