#!/usr/bin/env python3
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='test1',
                         exchange_type='fanout')

message = "Msg from A"
channel.basic_publish(exchange='test1',
                      routing_key='a_queue',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()
