from database.database import Database
from database.queries import INSERT_RESERVATION


class ReservationController:

    def __init__(self):

        self.db = Database()

    def add_reservation(
        self,
        full_name,
        email,
        hotel_name,
        check_in,
        check_out,
        guests
    ):

        self.db.execute(
            INSERT_RESERVATION,
            (
                full_name,
                email,
                hotel_name,
                check_in,
                check_out,
                guests
            )
        )

        self.db.commit()

        return True