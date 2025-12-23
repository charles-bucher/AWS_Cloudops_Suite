from main import handler

# relative import

# Simulate a Lambda event
event = {"test": "data"}
context = {}

response = handler(event, context)
print("Lambda response:", response)
