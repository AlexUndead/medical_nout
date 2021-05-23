from peewee import PostgresqlDatabase, Model, UUIDField, CharField

db = PostgresqlDatabase(
    'postgres',
    user='postgres',
    port=5432,
    host='db',
)


class Loan(Model):
    '''Кредит'''
    id = UUIDField()
    productName = CharField()

    class Meta:
        database = db


if __name__ == '__main__':
    with db:
        db.create_tables([Loan])
