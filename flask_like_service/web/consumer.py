import json
from typing import List
import pika
from collections import defaultdict
from util import convert_data_dict

params = pika.URLParameters("amqps://ewlujbkd:UdwQym7BRBVve4hBWL08R51_tNJXoBxg@rattlesnake.rmq.cloudamqp.com/ewlujbkd")
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare("main")

print("=================   Started in flasks  ===================")


def callback(ch, method, properties, body):
    products = defaultdict(List[dict])

    print("RECEIVED IN Flask")
    data = convert_data_dict(body)
    print('===========================================')
    print(data)
    print('===========================================')

    if properties.content_type == 'product_created':
        for k, v in data.items():
            products[k] = v
        print(products.items())
        print("=====   CREATED PRODUCTS =====")

    elif properties.content_type == 'product_updated':
        for k, v in data:
            products[k].append(v)

        print(f"PRODUCT UPDATED: {products.items()} ")

    elif properties.content_type == 'product_deleted':
        products.pop(data)
        print(f"PRODUCT DELETED: {products.items()} ")


channel.basic_consume(queue="main", on_message_callback=callback, auto_ack=True)
channel.start_consuming()

channel.close()
