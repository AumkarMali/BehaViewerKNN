import json
import pandas as pd
from sklearn.ensemble import HistGradientBoostingClassifier
from NumericalCategorization import brand_mapping, plan_mapping, gender_mapping, provider_mapping
#

# Load JSON data from the file
def load_user_data(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data['details']

# Function to train and use the HistGradientBoostingClassifier
def gradientBoostingClassifier(new_user_json):
    user_data = load_user_data('data.json')  # get json file of large user data

    # Create pandas DataFrame
    df = pd.DataFrame(user_data)

    # numeric features for the device brand and device plan of each user based on mappings
    df['brand'] = df['Device_Brand'].map(brand_mapping)
    df['plan'] = df['Device_Plan'].map(plan_mapping)
    df['Gender'] = df['Gender'].map(gender_mapping)
    df['Age'] = df['Age']  # Age is already numeric

    # Predictions will be made for provider based on user data!
    df['class'] = df['provider'].map(provider_mapping)

    # This is an array used as the feature matrix for the machine learning model
    userDataQueries = df[['brand', 'plan', 'Gender', 'Age']].values

    predictorVal = df['class'].values  # Classes (provider) will be what is predicted

    # HistGradientBoostingClassifier, handles missing values NaN.
    model = HistGradientBoostingClassifier()
    model.fit(userDataQueries, predictorVal)

    # Builds new user data point
    new_user = json.loads(new_user_json)

    # Update mappings if new values are found
    new_brand = new_user['Device_Brand']
    if new_brand not in brand_mapping:
        brand_mapping[new_brand] = len(brand_mapping) + 1  # Assign new numeric value

    new_plan = new_user['Device_Plan']
    if new_plan not in plan_mapping:
        plan_mapping[new_plan] = len(plan_mapping) + 1  # Assign new numeric value

    new_gender = new_user['Gender']
    if new_gender not in gender_mapping:
        gender_mapping[new_gender] = len(gender_mapping)  # Assign new numeric value

    # Convert new user data to numerical values
    new_user_x = brand_mapping[new_brand]
    new_user_y = plan_mapping[new_plan]
    new_user_gender = gender_mapping[new_gender]
    new_user_age = new_user['Age']
    new_user_point = [[new_user_x, new_user_y, new_user_gender, new_user_age]]

    # Predicted class labels for the user
    predicted_class = model.predict(new_user_point)
    # Map predicted class, [0] represents the number 1 prediction
    predicted_provider = [k for k, v in provider_mapping.items() if v == predicted_class[0]][0]

    return int(predicted_class[0]), str(predicted_provider)


