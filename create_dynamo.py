import boto3

def create_dynamodb_table():
    # Manually specifying credentials (replace with your actual credentials)
    dynamodb = boto3.resource(
        'dynamodb',
        region_name='eu-north-1',
        aws_access_key_id='AKIATCKAS5YEAWWUO5AZ',
        aws_secret_access_key='QvCqcrzQ1ruw0BKvyIFPI+og3nvVMHIYLBfGNUh7'
    )

    # Create the DynamoDB table
    table = dynamodb.create_table(
        TableName='StaffRecords',
        KeySchema=[
            {
                'AttributeName': 'name',
                'KeyType': 'HASH'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'name',
                'AttributeType': 'S'  # S for String
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    # Wait until the table exists
    table.meta.client.get_waiter('table_exists').wait(TableName='StaffRecords')
    print(f"Table {table.table_name} is created successfully.")

    return table

if __name__ == '__main__':
    create_dynamodb_table()

