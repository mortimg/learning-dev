import pandas as pd
import numpy as np

# Define the number of rows
num_rows = 10

# Manually create mock data
data = {
    'Name': [
        'Alice Johnson', 'Bob Smith', 'Charlie Brown', 'David Wilson', 'Emma Davis',
        'Frank Miller', 'Grace Lee', 'Hannah Walker', 'Ivy Turner', 'James Harris'
    ],
    'Email': [
        'alice.johnson@example.com', 'bob.smith@example.com', 'charlie.brown@example.com', 
        'david.wilson@example.com', 'emma.davis@example.com', 'frank.miller@example.com', 
        'grace.lee@example.com', 'hannah.walker@example.com', 'ivy.turner@example.com', 
        'james.harris@example.com'
    ],
    'Address': [
        '123 Elm St', '456 Oak St', '789 Pine St', '101 Maple St', '202 Birch St',
        '303 Cedar St', '404 Spruce St', '505 Fir St', '606 Willow St', '707 Ash St'
    ],
    'City': [
        'Springfield', 'Riverside', 'Lakeside', 'Hillsboro', 'Greenville',
        'Woodland', 'Bristol', 'Franklin', 'Clinton', 'Hamilton'
    ],
    'Country': [
        'USA', 'USA', 'USA', 'USA', 'USA',
        'USA', 'USA', 'USA', 'USA', 'USA'
    ],
    'Phone': [
        '+1-555-1234', '+1-555-5678', '+1-555-8765', '+1-555-4321', '+1-555-6789',
        '+1-555-3456', '+1-555-7890', '+1-555-2345', '+1-555-6780', '+1-555-9876'
    ],
    'Age': np.random.randint(18, 80, size=num_rows),
    'Salary': np.random.randint(30000, 120000, size=num_rows),
    'Joining Date': [
        '2020-01-15', '2019-03-22', '2021-07-10', '2018-11-30', '2022-05-18',
        '2020-08-25', '2019-12-15', '2021-02-20', '2018-07-04', '2022-03-12'
    ],
    'Score': np.random.uniform(0, 100, size=num_rows)
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save DataFrame to a CSV file
df.to_csv('manual_mock_data.csv', index=False)

print("Mock data has been created and saved to 'manual_mock_data.csv'")
