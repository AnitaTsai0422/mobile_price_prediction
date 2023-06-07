class Creator:

    def __init__(self, conn):
        self.conn = conn
        self.cur = self.conn.cursor()

    def create_table(self, sql_syntax):
        if "CREATE" not in sql_syntax and "create" not in sql_syntax:
            raise SyntaxError("create table plzzzz")
        self.cur.execute(sql_syntax)

    def insert_data(self, df, sql_table_name):
        df.to_sql(sql_table_name, self.conn, if_exists='append')