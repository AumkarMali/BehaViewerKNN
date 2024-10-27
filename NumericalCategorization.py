
# Assigning a numerical value for Device_Brand, Device_Plan, Gender, Age in the Pandas DataFrame
brand_mapping = {
    "iPhone 15 Pro Max": 1,
    "Samsung Galaxy S21": 2,
    "Google Pixel 6": 3,
    "OnePlus 9": 4,
    "iPhone 14": 5,
    "Samsung Galaxy Z Flip 3": 6,
    "Xiaomi Mi 11": 7,
    "Sony Xperia 1 III": 8,
    "Nokia G50": 9,
    "Oppo Find X3": 10
}

plan_mapping = {
    "Leasing": 1,
    "Contract": 2,
    "Prepaid": 3
}

# Map Gender to numerical values
gender_mapping = {
    "Male": 0,
    "Female": 1,
    "Other": 2
}

# Mapping provider to numerical values
provider_mapping = {
    "Bell": 0,
    "Rogers": 1,
    "Telus": 2
}