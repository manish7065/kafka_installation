from kafka import KafkaProducer
from data import get_registered_user
import json
import time

# Define the Kafka broker address
bootstrap_servers = '172.21.60.47:9092'

# Define a topic name
topic_name = 'registered_user'

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

# Create a KafkaProducer instance
producer = KafkaProducer(
    bootstrap_servers=bootstrap_servers,
    value_serializer=json_serializer
)

if __name__ == "__main__":
    try:
        while True:
            registered_user = get_registered_user()
            producer.send(topic_name, registered_user)
            print(f"Sent message to {topic_name}: {registered_user}")
            time.sleep(3)
    except KeyboardInterrupt:
        producer.close()
