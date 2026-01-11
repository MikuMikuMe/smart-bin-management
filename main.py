Creating a smart-bin management system involves several components, including IoT devices for gathering real-time data from bins, a server for processing data, and possibly a frontend for visualization. For simplicity, I'll provide a basic Python program simulating some key components, focusing on managing bin data and optimizing collection routes based on bin statuses. Real IoT integration and additional backend and frontend implementations would be required for a complete system.

Here is a Python script to simulate the backend data processing for a smart-bin management system:

```python
import random
import logging
from typing import List, Dict, Tuple

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SmartBin:
    def __init__(self, bin_id: int, location: Tuple[float, float]):
        self.bin_id = bin_id
        self.location = location
        self.capacity = 100  # In percentage
        self.current_fill = 0  # In percentage
    
    def get_status(self) -> Dict[str, any]:
        return {
            "bin_id": self.bin_id,
            "location": self.location,
            "current_fill": self.current_fill,
            "capacity": self.capacity
        }
    
    def update_fill(self, fill_level: int):
        try:
            if not 0 <= fill_level <= 100:
                raise ValueError("Fill level must be between 0 and 100.")
            
            self.current_fill = fill_level
            logging.info(f"Updated bin {self.bin_id} fill level to {self.current_fill}%.")
        except Exception as e:
            logging.error(f"Error updating fill level of bin {self.bin_id}: {e}")

def generate_random_fill_level() -> int:
    """Simulate the fill level of a bin."""
    return random.randint(0, 100)

def main():
    # Create a list of smart bins with random locations
    bins = [SmartBin(bin_id=i, location=(random.uniform(-90, 90), random.uniform(-180, 180))) for i in range(10)]

    # Simulate random updates to the fill level of each bin
    for bin in bins:
        try:
            fill_level = generate_random_fill_level()
            bin.update_fill(fill_level)
        except Exception as e:
            logging.error(f"Error simulating bin data: {e}")

    # Display current status of all bins
    logging.info("Current status of all bins:")
    for bin in bins:
        logging.info(bin.get_status())

    # Optimizing trash collection
    # Collect bins that need attention, e.g., bins with fill level above a certain threshold
    threshold = 75
    bins_to_collect = [bin for bin in bins if bin.current_fill >= threshold]
    logging.info(f"Bins that need to be collected (threshold {threshold}%): {[bin.bin_id for bin in bins_to_collect]}")

if __name__ == "__main__":
    main()
```

### Explanation:

1. **SmartBin Class**: Represents each bin with its unique ID, location, capacity, and current fill level. Offers methods to update the fill level with error handling.

2. **Logging**: Essential for tracking the system's operation and troubleshooting. Includes info and error levels for relevant events.

3. **Data Simulation**: The program generates random fill levels for bins, simulating real-time data from an IoT device.

4. **Optimization Logic**: Identifies bins that need collection based on a predefined fill level threshold, indicative of a strategic collection plan to optimize costs.

5. **Error Handling**: Includes error handling for updating fill levels and simulating data.

This program serves as a basic starting point for the backend logic. To develop a full-fledged smart-bin management system, you would integrate actual IoT device data inputs, deploy a database for persistent storage, develop more sophisticated route optimization algorithms, and potentially create a user interface for monitoring the system.