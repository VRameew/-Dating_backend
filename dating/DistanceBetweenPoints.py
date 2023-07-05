from numpy import sin, cos, arccos, pi, round


def rad2deg(radians):
    degrees = radians * 180 / pi
    return degrees


def deg2rad(degrees):
    radians = degrees * pi / 180
    return radians


def getDistanceBetweenPointsNew(latitude1, longitude1, latitude2, longitude2):
    """"Функция для поиска растояния между двумя точками по долгате и широте
    изначально функци написана для поисска как в километрах так и милях
    но оставлена работа только в километрах. Для подключения работы с двумя единицами
    в функцию нужно передовать переменную unit"""
    theta = longitude1 - longitude2

    distance = 60 * 1.1515 * rad2deg(
        arccos(
            (sin(deg2rad(latitude1)) * sin(deg2rad(latitude2))) +
            (cos(deg2rad(latitude1)) * cos(deg2rad(latitude2)) * cos(deg2rad(theta)))
        )
    )

    """Код работы по двум разным единицам измерения
    if unit == 'miles':
        return round(distance, 2)
    if unit == 'kilometers':
        return round(distance * 1.609344, 2)"""
    """Идет округление до двух знаков после запятой"""
    return round(distance * 1.609344, 2)