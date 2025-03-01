# Iris Flower Classifier

This is a simple web application for classifying **Iris Flower species** using a **Random Forest Classifier**. The app is built using **Streamlit** and utilizes the **Iris dataset** from `sklearn.datasets`.

---

## Installation

1. **Clone the repository** or download the script:

   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, install required libraries manually:

   ```bash
   pip install pandas scikit-learn streamlit
   ```

3. **Run the application**:

   ```bash
   streamlit run Iris_Flower.py
   ```

---

## How It Works

1. **User Input**:

   - The sidebar contains sliders for adjusting:
     - Sepal length (cm)
     - Sepal width (cm)
     - Petal length (cm)
     - Petal width (cm)

2. **Model Prediction**:

   - A **Random Forest Classifier** is trained using the Iris dataset.
   - The model predicts the **species** of the flower based on user inputs.

3. **Output Display**:

   - **User input values**.
   - **Target class names**.
   - **Predicted species name**.
   - **Prediction probabilities**.

## Dataset Information

The **Iris dataset** is a well-known dataset containing **150 samples** from three different Iris flower species:

- **Setosa**
- **Versicolor**
- **Virginica**

Each sample has **four features**:

- **Sepal length (cm)**
- **Sepal width (cm)**
- **Petal length (cm)**
- **Petal width (cm)**


