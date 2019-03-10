from sqlalchemy import ( create_engine, MetaData, String, Integer,
                        Table, Column )
class DataAccessLayer:
    def __init__(self):
        self.connection = None
        self.engine = None
        self.metadata = MetaData()
        self.conn_string = None
        self.subscribers = Table(
            'subscribers', self.metadata, 
            Column('subscriber_id', Integer(),primary_key = True, autoincrement = True),
            Column('email_id', String(255), nullable = False),
            Column('first_name', String(255), nullable = False),
            Column('last_name', String(255), nullable = False)
        )
        self.db_init(self.conn_string)


    def db_init(self, conn_string):
        self.engine = create_engine('sqlite:///subscriberdb.db')
        self.metadata.create_all(self.engine)
        self.connection = self.engine.connect()

dal = DataAccessLayer()