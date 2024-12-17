# Order Prediction

This project aims to predict the number of orders based on features like store type, location type, holiday status, and discount availability. The prediction model uses a dataset containing order information and applies a regression model (Gradient Boosting) to predict the number of orders for different store locations under varying conditions.
## Features

    Order Prediction: Predicts the number of orders based on various features like store type, location type, holiday, and discount.
    Data Visualization: Visualizes data distributions using pie charts for various categorical variables.
    Regression Model: Uses LightGBM (Gradient Boosting) regression to predict the number of orders.

## Requirements

This project requires Python 3.x and the following libraries:

    pandas
    numpy
    plotly
    lightgbm
    scikit-learn

You can install these dependencies using pip:

pip install pandas numpy plotly lightgbm scikit-learn

Installation

    Clone this repository to your local machine.

    git clone https://github.com/yourusername/order-prediction.git
    cd order-prediction

Install the required dependencies.

    pip install -r requirements.txt

    Download the dataset TRAIN.csv (from the specified source or your own dataset) and place it in the project directory.

## Usage

    Load the dataset into a pandas DataFrame.
    Perform basic data exploration (check for missing values, basic statistics).
    Visualize categorical data with pie charts for features like Store_Type, Location_Type, Region_Code, Discount, and Holiday.
    Preprocess categorical variables by mapping them to numeric values.
    Split the dataset into features (X) and target (Y), and then split further into training and testing sets.
    Train the model using LightGBM and make predictions on the test data.
    View the predicted number of orders.

Run the script with the following command:

    python order_prediction.py

## Example Output

    After training the model and making predictions
    data_predic = pd.DataFrame(data={"Predicted Orders": Y_predic.flatten()})
    print(data_predic)

## Data Visualization

Pie charts are generated to show the distribution of various categorical features:

    Store Type: Displays the distribution of orders across different store types (S1, S2, S3, S4).
    Location Type: Shows the distribution of orders based on location type (L1, L2, L3, L4, L5).
    Region Code: Visualizes the distribution of orders across different region codes.
    Discount: Displays the order distribution based on whether a discount is applied (Yes/No).
    Holiday: Visualizes the order distribution during holidays (Yes/No).

## Code Explanation
1. Data Preprocessing

    The dataset is loaded, and missing values are checked.
    Categorical variables such as Store_Type, Location_Type, and Discount are mapped to numerical values (e.g., "S1" -> 1, "S2" -> 2).
    Holiday is mapped to 1 for "Yes" and 0 for "No".

2. Data Visualization

    Pie charts are created for categorical features using plotly.express to provide an overview of how different factors influence the number of orders.

3. Model Training

    The dataset is split into features (X) and the target (Y, number of orders).
    The dataset is further split into training and testing sets using train_test_split from sklearn.model_selection.
    A LightGBM regression model is created and trained on the data.

4. Model Prediction

    After training, the model is used to predict the number of orders for the test set.
    Predictions are displayed in a DataFrame for easier viewing.

