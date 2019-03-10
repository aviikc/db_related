from personal_info_model import dal
from sqlalchemy.sql import insert, select


def insert_subscriber_info(sub_email, subfname, sublname):
    ins = insert(dal.subscribers).values(
        email_id = sub_email,
        first_name = subfname,
        last_name = sublname
    )
    dal.connection.execute(ins)



