import pika

connection_parameters = pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('guest', 'guest'))

try:
    connection = pika.BlockingConnection(connection_parameters)
    print("Connected successfully!")
    connection.close()
except Exception as e:
    print("Connection failed:", type(e).__name__, e)
