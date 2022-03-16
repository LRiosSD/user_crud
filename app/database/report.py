
from sqlite3 import Cursor
from unittest import result
from app.database import get_db

def get_users_and_vehicles_join():
    stmt = """
    SELECT user.last_name,
    user.firs_name,
    user.hobbies,
    user.active,
    vehicle.license_plate,
    vehicle.color,
    vehicle_typedescription
    FROM user
    INNER JOIN vehicle ON user.id - vehicle.user_id
    INNER JOIN vehicle_type ON vehicle.v_type = vehicle_type.id
    """
    cursor = get_db().execute(stmt,())
    results = cursor.fetchall()
    cursor.close()
    out = []
    for result in results:
        res_dict = {}
        res_dict = {
            "user_first_name": result[0],
            "user_last_name": result[1],
            "user_hobbies": result[2],
            "vehicle_license_plate": [3],
            "vehicle_color": [4],
            "vehicle_type": [5]
        }
