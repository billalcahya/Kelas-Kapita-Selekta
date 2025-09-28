from pymongo import MongoClient
from bson.objectid import ObjectId

class MongoConnection:
    def __init__(self, connection_string, db_name):
        self.connection_string = connection_string
        self.db_name = db_name
        self.client = None
        self.db = None
        self.__get_connection()

    def __get_connection(self):
        try:
            self.client = MongoClient(self.connection_string)
            self.db = self.client[self.db_name]
            self.client.admin.command("ping")
            print("Berhasil menghubungkan ke mongodb atlas!")
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")

    def find(self, collection, query, project={}, limit=0, sort=[], multi=False):
        result = {
            "status": False,
            "data": None,
            "message": "Terjadi kesalahan saat mengambil data",
        }
        try:
            if multi:
                resultFind = self.db[collection].find(
                    query, projection=project, limit=limit, sort=sort
                )
                resultFind = list(resultFind)
            else:
                resultFind = self.db[collection].find_one(
                    query, projection=project, sort=sort
                )

            if resultFind is not None:
                result["status"] = True
                result["data"] = resultFind
                result["message"] = "Berhasil mengambil data"

        except Exception as e:
            print(f"Error find: {e}")

        return result

    def insert(self, collection, data, multi=False):
        result = {
            "status": False,
            "data": None,
            "message": "Terjadi kesalahan saat menambahkan data",
        }
        try:
            if multi:
                result_insert = self.db[collection].insert_many(data)
            else:
                result_insert = self.db[collection].insert_one(data)

            if result_insert.acknowledged:
                result['status'] = True
                result['message'] = "Berhasil menambahkan data"
                if multi:
                    result['data'] = {'inserted_id': [str(i) for i in result_insert.inserted_ids]}
                else:
                    result['data'] = {'inserted_id': str(result_insert.inserted_id)}

        except Exception as e:
            print(f"Error insert: {e}")

        return result
    
    def update(self, collection, query, data):
        result = {
            "status": False,
            "data": None,
            "message": "Terjadi kesalahan saat memperbarui data"
        }
        try:
            result_update = self.db[collection].update_one(query, {"$set": data})
            if result_update.acknowledged:
                result["status"] = True
                result["data"] = {"matched_count": result_update.matched_count, "modified_count": result_update.modified_count}
                result["message"] = "Berhasil memperbarui data"
        except Exception as e:
            print(f"Error update: {e}")
        return result

    def delete(self, collection, query, multi=False):
        result = {
            "status": False,
            "message": "Terjadi kesalahan saat menghapus data",
        }
        try:
            if multi:
                result_delete = self.db[collection].delete_many(query)
            else:
                result_delete = self.db[collection].delete_one(query)

            if result_delete.acknowledged:
                result["status"] = True
                result["message"] = f"Berhasil menghapus {result_delete.deleted_count} dokumen"
            
        except Exception as e:
            print(f"Error delete: {e}")

        return result

if __name__ == "__main__":
    MONGODB_CONNECTION_STRING = "mongodb+srv://672023165:321Billal.@kapita-selekta.xgg367i.mongodb.net/?retryWrites=true&w=majority&appName=kapita-selekta"
    MONGODB_DATABASE_NAME = "kapita"
    MONGODB_COLLECTION_PRODUCTS = "product"
    MONGODB_COLLECTION_USER = "users"

    mongo = MongoConnection(MONGODB_CONNECTION_STRING, MONGODB_DATABASE_NAME)
    print(mongo.find(MONGODB_COLLECTION_PRODUCTS, {}))

    sample_data = {"_id": "PRO014", "name": "Monitor 24 inch", "category": "Elektronik", "stock": 8, "price": 2500000, "location": "A1-02"}
    result_insert = mongo.insert(MONGODB_COLLECTION_PRODUCTS, sample_data)
    print(result_insert)
    
    sample_multiple_data = [
        {"_id": "PRD015", "name": "Mouse gaming", "category": "Elektronik", "stock": 100, "price": 600000, "location": "A1-03"},
        {"_id": "PRD016", "name": "Mouse pad", "category": "Aksesoris", "stock": 500, "price": 100000, "location": "A1-04"}
    ]

    result_insert_many = mongo.insert(MONGODB_COLLECTION_PRODUCTS, sample_multiple_data, multi=True)
    print(result_insert_many)