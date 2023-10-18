def get_database_fields(db_name):
    # df = spider_schema[spider_schema["Database name"] == db_name]
    # df = df.groupby(" Table Name")
    # output = ""
    # for name, group in df:
    #     output += "Table " + name + ", columns = ["
    #     for index, row in group.iterrows():
    #         output += row[" Field Name"] + ","
    #     output = output[:-1]
    #     output += "]\n"
    # return output
    return """Table concert, columns = [*,concert_ID,concert_Name,Theme,Stadium_ID,Year]
Table singer, columns = [*,Singer_ID,Name,Country,Song_Name,Song_release_year,Age,Is_male]
Table singer_in_concert, columns = [*,concert_ID,Singer_ID]
Table stadium, columns = [*,Stadium_ID,Location,Name,Capacity,Highest,Lowest,Average]"""


def get_database_foreign_keys(db_name):
    return """Foreign_keys = [concert.Stadium_ID = stadium.Stadium_ID,singer_in_concert.Singer_ID = singer.Singer_ID,singer_in_concert.concert_ID = concert.concert_ID]"""
