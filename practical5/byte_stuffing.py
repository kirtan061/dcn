 # byte_stuffing.py

data = input("Enter data: ")

flag = "F"
escape = "E"

stuffed = ""

for ch in data:
    if ch == flag or ch == escape:
        stuffed += escape
    stuffed += ch

stuffed = flag + stuffed + flag

print("Stuffed data:", stuffed)
