from etl import extract_data, transform_data, load_data
def main():
    data = extract_data()
    transformed_data = transform_data(data)
    load_data(transformed_data)

if __name__ == "__main__":
    main()