import cv2
from pyzbar.pyzbar import decode
import requests
import time
import re
import tkinter as tk
from tkinter import messagebox

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
camera = True

pattern = r"seat=(\d+-\d+)"

while camera:
    success, frame = cap.read()

    for code in decode(frame):
        if code.data.decode('utf-8').startswith('completeBooking'):
            grabbed_data = code.data.decode('utf-8')
            grabbed_data = grabbed_data.replace('~', '&')
            # print(grabbed_data)
            url = "http://localhost/Cinema/classes/booking.class.php?" + grabbed_data
            response = requests.get(url)
            matches = re.findall(pattern, grabbed_data)
            row, col = matches[0].split('-')
            print("Valid Ticket | Seats: row {0}, col {1}".format(row, col))
            time.sleep(2)
        else:
            pass

    cv2.imshow('Cinema Verify', frame)
    cv2.waitKey(1)
