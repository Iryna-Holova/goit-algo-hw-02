"""
A program that simulates a service center for handling requests using a queue.
New requests are automatically generated and added to the queue, then
processed in a FIFO manner.

The program continues to generate and process requests until manually stopped
by the user. Each request is identified by a unique ID, and the processing
time is simulated using a random delay.
"""

import queue
import random
import time

# Create a request queue
request_queue = queue.Queue()


def generate_request(request_id):
    """
    Generates a new request and adds it to the queue.

    Parameters:
    request_id (int): The unique identifier for the request.

    Returns:
    None
    """
    print(f"Generating request #{request_id}")
    request_queue.put(f"Request #{request_id}")


def process_request():
    """
    Processes the next request in the queue.
    If the queue is not empty, it retrieves and processes a request.
    If the queue is empty, it prints a message indicating that there are no
    requests.

    Returns:
    None
    """
    if not request_queue.empty():
        request = request_queue.get()
        print(f"Processing {request}")
        # Simulate the time taken to process the request
        time.sleep(1)
        print(f"{request} has been processed")
    else:
        print("No requests to process, the queue is empty.")


def main():
    """
    Main function to simulate the continuous generation and processing of
    requests.

    Generates new requests with a unique ID and processes them in sequence.
    Uses random delays to simulate the time interval between new requests.

    Returns:
    None
    """
    request_id = 1
    while True:
        # Generate a new request and process it
        generate_request(request_id)
        request_id += 1

        # Process the request
        process_request()

        # Simulate the interval between requests
        time.sleep(random.uniform(0.5, 2))


# Entry point for the program
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nService stopped by user.")
