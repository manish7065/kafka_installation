from kafka import KafkaConsumer
import json




if __name__ == "__main__":
    consumer = KafkaConsumer(
        "registered_user",
        bootstrap_server='localhost:9092',
        auto_offset_reset = 'earliest',
        group_id = "consumer-group-a"
    )
    print("Startinf the consumer")
    for msg in consumer:
        print("Registered User = {}".format(json.load(msg.value)))