from prometheus_client import start_http_server, Counter

# Create a Counter metric
requests_total = Counter('your_application_requests_total', 'Total number of HTTP requests')

# Increment the metric when a request is made
def handle_request():
    requests_total.inc()

if __name__ == '__main__':
    # Start an HTTP server to expose the metrics
    start_http_server(8000)