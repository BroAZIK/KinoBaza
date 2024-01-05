from tinydb import TinyDB, Query
from tinydb.database import Document
User = Query()

db1 = TinyDB('database/harakat.json', indent=4)
db2 = TinyDB('database/movies.json', indent=4)
db3 = TinyDB('database/Users.json', indent=4)


stage       = db1.table('stage')
users       = db3.table('Users')
movies      = db2.table('kino')

def soni():
    mov = movies.all()
    user = users.all()

    useriss = len(user)
    movs = len(mov)
    return {"users": useriss, "movies": movs}
    

def get(table, user_id):

    if table == "stage":
        return stage.get(doc_id=user_id)
    
    elif table == "users":
        return users.get(doc_id=user_id)
    
    elif table == "movies":
        return movies.get(doc_id=user_id)

def insert(table, user_id, data):

    if table == "stage":
        doc = Document(
            value=data,
            doc_id=user_id
        )
        stage.insert(doc)
    
    elif table == "users":
        doc = Document(
            value=data,
            doc_id=user_id
        )
        users.insert(doc)
    
    elif table == "movies":
        mov = movies.all()
        mov_len = len(mov) + 1
        doc = Document(
            value=data,
            doc_id=mov_len
        )
        movies.insert(doc)

        return mov_len
def update_db(table, user_id, data):


    if table == "stage":
        stage.update(data, doc_ids=[user_id])
    
    elif table == "users":
        users.update(data, doc_ids=[user_id])
    
    elif table == "movies":
        movies.update(data, doc_ids=[user_id])
def delete(table, user_id):

    if table == "movies":
        if movies.contains(doc_id=user_id):
            doc = movies.remove(doc_ids=[user_id])
            print(doc)
        else:
            print("user-not-exist")