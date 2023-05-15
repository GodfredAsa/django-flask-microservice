import json
import os

import django
import pika
from admin.products.models import Product

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

params = pika.URLParameters("amqps://ewlujbkd:UdwQym7BRBVve4hBWL08R51_tNJXoBxg@rattlesnake.rmq.cloudamqp.com/ewlujbkd")
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare("admin")


def callback(ch, method, properties, body):
    print("RECEIVED BY ADMIN ")
    product_id = json.loads(body)
    print(F"Message: {product_id}")
    product = Product.objects.get(id=product_id)
    product.likes += 1
    product.save()
    print(f'product title: {product.title}')


channel.basic_consume(queue="admin", on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()