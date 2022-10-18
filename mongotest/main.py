import pymongo

db_url1 = "mongodb://localhost:27021/?directConnection=true"
db_url2 = "mongodb://localhost:27001/?directConnection=true"
db_url3 = "mongodb://qwe:666777@194.67.109.158:27020/?authMechanism=DEFAULT&directConnection=true"
db_url4 = "mongodb://localhost:27017/?directConnection=true"

db_url5 = "mongodb://mongo:mongo@localhost:27005/?directConnection=true"

db_url6 = "mongodb://mongo:mongo@mongodb:27005/?directConnection=true"

db_url7 = "mongodb://mongo:mongo@net:27005/?directConnection=true"

def f1():
    db_url = db_url5

    print("Пробуем подключение")
    client = pymongo.MongoClient(db_url)
    db = client.GPdata
    print("Создали объект клиента")

    db["user"].insert_one({"_id":"1"})
    print("Успешно воспользовались бд")
    var = db["user"].find().to_list()
    print("Вот список в качестве примера")
    print(var)


if __name__=="__main__":
    f1()
