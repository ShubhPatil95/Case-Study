import os
import time

for i in range(10):
    # Read values from environment variables
    a = int(os.getenv('A', '10'))  # Default value is 10 if not found in ConfigMap
    b = int(os.getenv('B', '20'))  # Default value is 20 if not found in ConfigMap

    print(a + b)
    time.sleep(1)
