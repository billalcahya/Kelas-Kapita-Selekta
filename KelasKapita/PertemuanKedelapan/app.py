import redis
# from requests import delete

# r = redis.Redis(
#     host = '172.19.31.217',
#     port = 6379,
#     db = 0,
#     decode_responses=True
# )

# try:
#     r.ping()
#     print("Koneksi berhasil")
# except redis.ConnectionError:
#     print("Gaga; terhubung ke redis")
    
class SimpleRedis:
    def __init__(self,host='127.0.0.1', port = 6379):
        self.r = redis.Redis(host=host, port=port, decode_responses=True)
        
    def get(self,key):
        return self.r.get(key)
    
    def set(self,key, value):
        return self.r.set(key, value)
    
    def delete(self, key):
        return self.r.delete(key)