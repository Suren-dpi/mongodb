import pymongo

#Connect to mongo db using Atlas connection string
try:
    client = pymongo.MongoClient("mongodb+srv://rocksunil546:lTI9nB0xM0nNDvVX@cluster0.6zm5kur.mongodb.net/?retryWrites=true&w=majority")
except BaseException as e:
    print("An Invalid URI host error was received. Is your Atlas host name correct in your connection string?")
    print(e)

#Create a database 'demo0'
db = client.demo0

# Create a collection 'users'
my_collection = db["users"]

def create_users():
    user_details = [{
        "username": "admin",
        "email": "admin@innoviti.com",
        "full_name": "admin admin",
        "disabled": False,
        "hashed_password": "$2b$12$GGmqcnztAyCYNtKlY4sfzubXTnu4nGLV/hjwi8lcSMfGk96FDb1jS"
    },{
        "username": "administrator",
        "email": "administrator@innoviti.com",
        "full_name": "administrator administrator",
        "disabled": False,
        "hashed_password": "$2b$12$0ttEMW21Lwg.rFwW2tR4xudF0CgxzHXOsEPXSwNUN/byrL4GKeaZG"
    },{
        "username": "innoviti",
        "email": "innoviti@innoviti.com",
        "full_name": "innoviti Technologies",
        "disabled": False,
        "hashed_password": "$2b$12$UmQgzVuAvqP.7LJZgae7NePASmfDd6fx/qiHbZGKSDd9y7TLncIva"
    },{
        "username": "user002",
        "email": "user002",
        "full_name": "user002 user002",
        "disabled": False,
        "hashed_password": "$2b$12$3dXguIc3DMqOrsol1O1PzO0lqndNHFKNoEnv94CWVSLm4cfztZhnq"
    }]

    try:
        # drop the collection in case it already exists
        my_collection.drop()
        result = my_collection.insert_many(user_details)

    # return a friendly error if the operation fails
    except BaseException as e:
        print(
            "An authentication error was received. Are you sure your database user is authorized to perform write operations?")
        print(e)
    else:
        inserted_count = len(result.inserted_ids)
        print("I inserted %x documents." % (inserted_count))

        print("\n")
    finally:
        client.close()

def read_users():
    #result = my_collection.find({'username':'admin'}) for sepcific user
    result = my_collection.find()
    if result:
        for doc in result:
            my_user = doc
            print(my_user)
    else:
        print("No documents found.")
    print("\n")
    client.close()

# UPDATE A DOCUMENT
# You can update a single document or multiple documents in a single call.
# Here we update the prep_time value on the document we just found.
# Note the 'new=True' option: if omitted, find_one_and_update returns the
# original document instead of the updated one.
def update_users():
    my_doc = my_collection.find_one_and_update({"username": "user001"}, {"$set": {"email": "user001@innoviti.com"}}, new=True,upsert=True)
    if my_doc is not None:
        print("Here's the updated user:")
        print(my_doc)
    else:
        print("I didn't find any users named 'suren'")
    print("\n")
    client.close()

def insert_users():
    user_details = [{
        "username": "user003",
        "email": "user003",
        "full_name": "user003 user003",
        "disabled": False,
        "hashed_password": "$2b$12$3dXguIc3DMqOrsol1O1PzO0lqndNHFKNoEnv94CWVSLm4cfztZhnq"
    }]
    try:
        result = my_collection.insert_many(user_details)

    # return a friendly error if the operation fails
    except BaseException as e:
        print(e)
    else:
        inserted_count = len(result.inserted_ids)
        print("I inserted %x documents." % (inserted_count))
    finally:
        client.close()

def delete_users():
    my_result = my_collection.delete_many({"$or": [{"username": "user002"}, {"email": "user003"}]})
    print("I deleted %x records." % (my_result.deleted_count))
    print("\n")
    client.close()



read_users()