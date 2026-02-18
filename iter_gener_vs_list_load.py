import time
import tracemalloc
from datetime import datetime
import random

# -----------------------------------
# Simulate Organisation Mapping
# -----------------------------------
ORG_MAP = {
    "101": "Finance",
    "102": "HR",
    "103": "Engineering",
    "104": "Marketing"
}

# -----------------------------------
# Fake Data Generator (Simulates CSV rows)
# -----------------------------------
def generate_employee_data(n):
    for i in range(n):
        yield {
            "name": f"Emp{i % (n//2)}", # force duplicates
            "supervisor": f"Sup{i%50}",
            "org_code": random.choice(list(ORG_MAP.keys())),
            "dob": "1990-05-12"
        }

# -----------------------------------
# LIST VERSION (Loads Everything)
# -----------------------------------
def process_list_version(n):
    data = list(generate_employee_data(n)) # loads ALL data

    seen = set()
    result = []

    for row in data:
        if row["name"] in seen:
            continue
        seen.add(row["name"])

        # transform DOB
        dt = datetime.strptime(row["dob"], "%Y-%m-%d")
        row["dob"] = dt.strftime("%d/%m/%Y")

        # map organisation
        row["organisation"] = ORG_MAP.get(row["org_code"], "Unknown")

        result.append(row)

    return result


# -----------------------------------
# GENERATOR VERSION (Streaming)
# -----------------------------------
def deduplicate(records):
    seen = set()
    for row in records:
        if row["name"] not in seen:
            seen.add(row["name"])
            yield row

def transform(records):
    for row in records:
        dt = datetime.strptime(row["dob"], "%Y-%m-%d")
        row["dob"] = dt.strftime("%d/%m/%Y")
        row["organisation"] = ORG_MAP.get(row["org_code"], "Unknown")
        yield row

def process_generator_version(n):
    records = generate_employee_data(n)
    records = deduplicate(records)
    records = transform(records)

    count = 0
    for row in records:
        count += 1 # simulate saving to DB
    return count


# -----------------------------------
# TEST FUNCTION
# -----------------------------------
def run_test(n):
    print(f"\n===== Testing with {n} records =====")

    # LIST VERSION
    tracemalloc.start()
    start = time.time()
    process_list_version(n)
    end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("List Version:")
    print(f"Time: {end - start:.2f} seconds")
    print(f"Peak Memory: {peak / 10**6:.2f} MB")

    # GENERATOR VERSION
    tracemalloc.start()
    start = time.time()
    process_generator_version(n)
    end = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("Generator Version:")
    print(f"Time: {end - start:.2f} seconds")
    print(f"Peak Memory: {peak / 10**6:.2f} MB")


# -----------------------------------
# RUN TESTS
# -----------------------------------

if __name__ == "__main__":
    run_test(1000) # 1K
    run_test(1_00_000) # 1 Million