import time

class APIPaginationIterator:
    def __init__(self, total_pages):
        self.current_page = 0
        self.total_pages = total_pages
        self.buffer = [] # Acts as a small cache for current page data

    def __iter__(self):
        return self

    def __next__(self):
        # If buffer is empty, fetch the next page (simulation)
        if not self.buffer:
            if self.current_page >= self.total_pages:
                raise StopIteration
            
            # Simulate fetching data from an external API
            print(f"--- Fetching Page {self.current_page + 1} from API ---")
            self.buffer = [f"Record A{self.current_page}", f"Record B{self.current_page}"]
            self.current_page += 1

        # Return one item from the buffer
        return self.buffer.pop(0)

# Usage
api_stream = APIPaginationIterator(total_pages=2)

# The user (you) just sees a continuous stream of records
# The complex "page fetching" logic is hidden inside the iterator
for record in api_stream:
    print(f"Processing: {record}")
