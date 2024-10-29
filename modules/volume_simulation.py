import random
import time

def simulate_fake_volume(keyword):
    """
    Simulate fake trading volume for a given cryptocurrency keyword.
    """
    print(f"Starting fake volume simulation for: {keyword}")

    # Example simulation of volume increase
    for i in range(5):
        fake_volume = random.randint(1000, 5000)
        print(f"Fake volume for {keyword}: {fake_volume} trades")
        time.sleep(1)

    print(f"Completed fake volume simulation for: {keyword}")
