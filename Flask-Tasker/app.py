from flask import Flask, request
from rq import Queue
from worker import conn

app = Flask(__name__)
q = Queue(connection=conn)

def background_task(n):
    """Function that returns len(n) and simulates a delay."""
    delay = 2
    print("Task running")
    print(f"Simulating a {delay} second delay")
    time.sleep(delay)
    print(len(n))
    print("Task complete")
    return len(n)

@app.route("/task", methods=['POST'])
def add_task():
    data = json.loads(request.data.decode('utf-8'))
    if 'n' not in data:
        return "No n"
    job = q.enqueue(background_task, data['n'])
    return f"Task ({job.id}) added to queue at {job.enqueued_at}"