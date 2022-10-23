{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from machine import Pin\
import utime\
 \
relay = Pin(18, Pin.OUT)\
led = Pin(25, Pin.OUT)\
\
# Initialize: led and circuite closed\
relay(1)\
led.value(1)\
 \
while True:\
    utime.sleep(86400)\
    \
    # Turn off and back on again\
    relay(0)\
    led.value(0)\
    print('turn circuit off')\
    \
    utime.sleep(0.5)\
    relay(1)\
    led.value(1)\
    print('turn circuit back on')\
}