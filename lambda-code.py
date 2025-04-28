import json
import base64
import boto3

# S3 bucket name where records will be saved
BUCKET_NAME = 'bucket-for-streams'

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # Loop through the incoming records
    for record in event.get('Records', []):
        try:
            # Decode the base64-encoded record data
            payload = base64.b64decode(record['kinesis']['data'])
            
            # Convert the payload to a string (assuming it's JSON)
            payload_str = payload.decode('utf-8')
            
            # Log the decoded payload for debugging purposes
            print("Decoded Payload:", payload_str)
            
            # Save the decoded payload to S3
            s3.put_object(
                Bucket=BUCKET_NAME,
                Key=f"record-{record['kinesis']['sequenceNumber']}.txt",
                Body=payload_str
            )
            
        except Exception as e:
            # Log any errors for debugging
            print(f"Error processing record: {e}")

    return {
        'statusCode': 200,
        'body': json.dumps('Processing completed')
    }
