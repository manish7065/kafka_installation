try:
    import datetime
    import json
    import random
    import boto3
    import os
    import uuid
    import time
    from faker import Faker

    from dotenv import load_dotenv
    load_dotenv(".env")
except Exception as e:
    pass

global faker
faker = Faker()


def getReferrer():
    data = {}
    now = datetime.datetime.now()
    str_now = now.isoformat()
    data['uuid'] = str(uuid.uuid4())
    data['event_time'] = str_now

    data['ticker'] = random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV'])
    price = random.random() * 100
    data['price'] = round(price, 2)
    return data


while True:
    data = json.dumps(getReferrer())

    global kinesis_client

    kinesis_client = boto3.client('kinesis',
                                #   region_name='us-east-1',
                                  region_name='ap-south-1',
                                  aws_access_key_id=os.getenv("DEV_ACCESS_KEY"),
                                  aws_secret_access_key=os.getenv("DEV_SECRET_KEY")
                                  )

    res = kinesis_client.put_record(
        # StreamName="stock-streams",
        StreamName="flink_trial",
        Data=data,
        PartitionKey="1")
    print(data, " " , res)
    time.sleep(2)


