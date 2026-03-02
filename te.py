import json

tasks = '{"studentName": "John Doe", "tasks": ["task1", "task2", "task3"]}'

converted_task = json.loads(tasks)

print(converted_task)


market_list = ["apple", "tomato", "pepper", "carrot", "mango"]

items  = json.dumps(market_list)

print(items)