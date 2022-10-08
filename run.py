# the file that will run when calling from cli
import sqlite3
import sys

from prettytable import PrettyTable

con = None

# main function handles the cli commands
def main():
    global con
    print("project manager")
    print(sys.argv)

    # loading the database
    con = sqlite3.connect(r"D:\programming_me\pmsys\tickets.db")
    cur = con.cursor()

    # making the tables setup
    cur.execute("CREATE TABLE IF NOT EXISTS apps (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, completed INTEGER);")
    
    cur.execute("CREATE TABLE IF NOT EXISTS stories (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, fkapp INTEGER, implemented INTEGER)")

    # what command is given to the program

    # assert the command is of certain length
    
    if len(sys.argv) == 1:
        # if no arguments are given we want the app overview
        app_overview(cur)
    elif len(sys.argv) == 3:
        if sys.argv[1] == "app":
            # $ python .\run.py app x:int
            # the user wants to see the stories from app number ??
            try:
                app_id = int(sys.argv[2])
            except ValueError as e:
                raise ValueError(f"Error: {e}")
            
            story_overview(cur, app_id)
        
        # mockup app information

        # example App (DUMMY)
        # cur.execute("INSERT INTO apps (name, completed) VALUES ('pmsys', 0);")
        # con.commit()

        # example Story (DUMMY)
        # cur.execute("INSERT INTO stories (name, fkapp, implemented) VALUES ('project displays my story', 1, 0);")
        # con.commit()


        

        # print(apps)

def story_overview(cur, app_id):
    # get the name of the app
    cur.execute(f"SELECT name FROM apps WHERE id='{app_id}'")
    app = cur.fetchone()[0]
    if app == None:
        raise Exception(f"There does not seem to be an app with id: {app_id}")
    print("app:", app)
    # get the stories of the app.
    cur.execute(f"SELECT id, name, implemented FROM stories WHERE fkapp='{app_id}'")
    stories = cur.fetchall()

    story_table = PrettyTable()

    story_table.field_names = ["id", "story", "implemented"]
    for id, name, implemented in stories:
        implemented = "yes" if implemented == 1 else "No"
        story_table.add_row([id, name, implemented])

    print(story_table)

    stories

    # # title
    # print(f"{'ID':{id_col}}|{'Name':32}|{'Completed':{complete_col}}")
    # # data
    # for id, story in enumerate(stories):
    #     if story[2] == 1:
    #         story[2] = "Yes"
    #     else:
    #         story[2] = "No"
    #     print(f"{id:{id_col}}|{story[0]:{name_col}}|{story[2]:{complete_col}}")

def app_overview(cur):
    cur.execute("SELECT id, name, completed FROM apps")
    apps = cur.fetchall()

    app_table = PrettyTable()
    app_table.field_names = ["ID", "Name", "Completed"]
    for id, name, completed in apps:
        completed = "yes" if completed == 1 else "No"
        app_table.add_row([id, name, completed])

    print(app_table)




if __name__ == '__main__':
    main()