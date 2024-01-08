import redis
import os

r = redis.Redis(host=os.environ["REDIS_HOST"])

pubsub = r.pubsub()
pubsub.subscribe('wwtbam')

for message in pubsub.listen():
    pass
