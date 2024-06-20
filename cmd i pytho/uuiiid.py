import uuid

try:
    print(uuid.uuid1())
except Exception as e:
    print("Error:", e)
