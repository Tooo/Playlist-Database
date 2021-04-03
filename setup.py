from sqlsetup import SQLSetup

sqlSetup = SQLSetup()
sqlSetup.create_playlist_database()
sqlSetup.create_all_tables()
sqlSetup.import_songs()
