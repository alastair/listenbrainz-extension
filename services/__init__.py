from listenstore import ListenStore
from services.db_service import DBService
from services.redis_service import RedisService

# Things that connect to an external service
db = DBService()
redis = RedisService()

# Our 'service layer'
listenstore = ListenStore()
