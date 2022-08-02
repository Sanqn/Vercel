
class NewQueryView(generics.ListCreateAPIView):
    def post(self, request):
        dic_user = request.data  # получаем запрос в виде словаря
        name_class = ''
        for k, v in dic_user.items():
            if k == 'type' and v in li_seria:
                name_class = v

        # ищем созданную модель в models.py,
        # если есть сериализуем и добавляем в созданную таблицу
        if name_class:
            type_serial = eval(name_class)  # приводим строку к классу и подставляем в сериализатор
            serializer = type_serial(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({'message': 'User created',
                             'user': serializer.data})
        else:  # если нет в models  моделей, подключаемся к БД
            name_field = {}
            name_table = ''
            for key, val in dic_user.items():
                if key == 'type':
                    name_table = val
                else:
                    if key != 'type':
                        name_field[key] = name_field.get(key, 'VARCHAR(100)')

            def create_connection(db_name, db_user, db_password, db_host, db_port):
                connection = None
                try:
                    connection = psycopg2.connect(
                        database=db_name,
                        user=db_user,
                        password=db_password,
                        host=db_host,
                        port=db_port,
                    )
                    print('Connection to PosrgresQL DB successfull')
                except OperationalError as e:
                    print(f"The error '{e}' occurred")
                return connection

            con = create_connection("DB1", "postgres", "root", "127.0.0.1", "5432")

            def check_name_db(connection):
                try:
                    cursor = connection.cursor()
                    cursor.execute(
                        "SELECT table_name FROM information_schema.tables WHERE table_schema NOT IN ('information_schema', 'pg_catalog')")
                    find_name_inbd = ''
                    for x in cursor:
                        if name_table in x:
                            find_name_inbd = name_table
                    print(f" DB {find_name_inbd} exists")
                    if find_name_inbd:
                        users = [
                            ("James", "Cameron"),
                        ]
                        user_records = ", ".join(["%s"] * len(users))
                        insert_query = (
                            f"INSERT INTO testperson (first_name, last_name) VALUES {user_records}"
                        )
                        connection.autocommit = True
                        cursor = connection.cursor()
                        cursor.execute(insert_query, users)

                except OperationalError as e:
                    print(f"The error '{e}' occurred")

            check_name_db(con)

            # def execute_query_users(connection):
            #     try:
            #         users = [
            #             ("James", 25, "male", "USA"),
            #             ("Leila", 32, "female", "France"),
            #             ("Brigitte", 35, "female", "England"),
            #             ("Mike", 40, "male", "Denmark"),
            #             ("Elizabeth", 21, "female", "Canada"),
            #         ]
            #
            #         user_records = ", ".join(["%s"] * len(users))
            #
            #         insert_query = (
            #             f"INSERT INTO users (name, age, gender, nationality) VALUES {user_records}"
            #         )
            #
            #         connection.autocommit = True
            #         cursor = connection.cursor()
            #         cursor.execute(insert_query, users)
            #     except OperationalError as e:
            #         print(f"The error '{e}' occurred")
            #
            # execute_query_users(con)

    # def create_table(connection, query):
    #     con.autocommit = True
    #     cursor = connection.cursor()
    #     try:
    #         cursor.execute(query)
    #     except OperationalError as e:
    #         print(f"The error '{e}' occurred")
    #     return Response({'message': 'Table is created'})
    #
    # # проверяем, если нет таблицы в БД, создаем из запроса request
    # result_field = ', '.join(f'{key} {value}' for key, value in name_field.items())
    # create_users_table = f"CREATE TABLE IF NOT EXISTS {name_table} (id SERIAL PRIMARY KEY, {result_field})"
    # create_table(con, create_users_table)