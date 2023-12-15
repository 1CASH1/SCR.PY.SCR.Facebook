from selenium.common.exceptions import TimeoutException
import random


class SleepTime:
    def __init__(self):
        pass

    def generate_wait_time(self, wait_type):
        if wait_type == "fast":
            # Generates a random time in milliseconds between 2000 and 4000
            return int(random.uniform(2000, 4000))/1000
        elif wait_type == "medium":
            return int(random.uniform(5000, 9000))/1000
        elif wait_type == "long":
            return int(random.uniform(10000, 15000))/1000
        elif wait_type == "very_long":
            return int(random.uniform(20000, 30000))/1000
        else:
            raise ValueError("Invalid wait type")

    def generate_wait_time_random(self):
        # Generate a random wait type
        wait_type_list = ["fast", "medium", "long", "very_long"]
        random_wait_type = random.choice(wait_type_list)

        # Call generate_wait_time with the random wait type
        return self.generate_wait_time(random_wait_type)
    
    def generate_wait_time_random_f(self):
        # Generate a random wait type
        wait_type_list = ["fast", "medium"]
        random_wait_type = random.choice(wait_type_list)

        # Call generate_wait_time with the random wait type
        return self.generate_wait_time(random_wait_type)
    
    
    def generate_wait_time_random_m(self):
        # Generate a random wait type
        wait_type_list = [ "medium", "long"]
        random_wait_type = random.choice(wait_type_list)

        # Call generate_wait_time with the random wait type
        return self.generate_wait_time(random_wait_type)
    
    def generate_wait_time_random_m(self):
        # Generate a random wait type
        wait_type_list = ["long", "very_long"]
        random_wait_type = random.choice(wait_type_list)

        # Call generate_wait_time with the random wait type
        return self.generate_wait_time(random_wait_type)
