import pika, json

params = pika.URLParameters('amqps://ewlujbkd:UdwQym7BRBVve4hBWL08R51_tNJXoBxg@rattlesnake.rmq.cloudamqp.com/ewlujbkd')
connection = pika.BlockingConnection(params)
channel = connection.channel()


# the body is the object we are sending, but we need to connect to json first


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange="", routing_key="admin", body=json.dumps(body), properties=properties)
