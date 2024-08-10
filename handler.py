import pymysql
import boto3

#Configuration Values
endpoint = 'your endpoint'
username = 'your username'
password = 'your password'
database_name = "your db name"
 
#Connection
connection = pymysql.connect(host=endpoint, user=username,
	passwd=password, db=database_name)

dynamodb = boto3.resource('dynamodb').Table('your dynamodb table name')

def lambda_handler(event, context):
	cursor = connection.cursor()
	cursor.execute('SELECT * from table name')
 
	rows = cursor.fetchall()
 
	for row in rows:
		
		id, name, age, city = row
		
		
		response = dynamodb.put_item(
			Item = {
				'Emp Id': {id},
				'Emp Name': {name},
				'Emp Age': {age},
				'Emp City': {city}
			})
		
		print(f'Insert response: {response}')
		
