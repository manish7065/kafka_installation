"""
code has been tested successfully with producing and consuming i real time
"""








import boto3,os
import json
from dotenv import load_dotenv
load_dotenv(".env")

# Initialize the Kinesis client
kinesis_client = boto3.client(
    'kinesis',
    region_name='ap-south-1',
    # aws_access_key_id='YOUR_ACCESS_KEY',  # Set your AWS access key
    # aws_secret_access_key='YOUR_SECRET_KEY'  # Set your AWS secret key
    aws_access_key_id=os.getenv("DEV_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("DEV_SECRET_KEY")
)

# Define the Kinesis stream name
stream_name = "flink_trial"

# Shard iterator type and position
# shard_iterator_type = "LATEST"
shard_iterator_type = "TRIM_HORIZON"

shard_id = 'shardId-000000000003'  # Replace with the appropriate shard ID

# Get a shard iterator
response = kinesis_client.get_shard_iterator(
    StreamName=stream_name,
    ShardId=shard_id,
    ShardIteratorType=shard_iterator_type
)

shard_iterator = response["ShardIterator"]

# Open a file for writing received data
output_file = open("received_data.json", "a")

# Continuously read data from the stream
while True:
    response = kinesis_client.get_records(
        ShardIterator=shard_iterator,
        Limit=10  # Adjust the batch size as needed
    )

    records = response["Records"]
    

    for record in records:
        data = json.loads(record["Data"])
        print("Received data:", data)
        
        # Write the data to the file
        output_file.write(json.dumps(data) + "\n")

    shard_iterator = response["NextShardIterator"]
