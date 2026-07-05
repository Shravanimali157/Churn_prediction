import streamlit as st
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt 


model = pickle.load(open("model.pkl", "rb"))
df=pd.read_csv("cleaned_data.csv")

st.set_page_config(page_title="Telco Customer Churn Prediction", layout="wide")

st.markdown("""
<h1 style="
    text-align: center;
    font-size: 50px;
    color: #1E88E5;
    font-family: Arial;
    font-weight: bold;">
    📞 Telco Customer Churn Prediction
</h1>
""", unsafe_allow_html=True)


col1,col2=st.columns(2)
with col1:
    # image
    st.markdown(f"""
    <style>
    .image-container {{
        display: flex;
        justify-content: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }}

    .image-container img {{
        width: 500px;
        border-radius: 15px;
        box-shadow: 0px 8px 25px rgba(0,0,0,0.35);
    }}
    </style>

    <div class="image-container">
        <img src="https://static.vecteezy.com/system/resources/thumbnails/072/981/516/small/reaching-financial-heights-business-executive-surveying-data-driven-cityscape-photo.jpeg">
    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    ### About

    This application predicts whether a telecom customer is likely to churn using a machine learning model. Enter the customer information and click **Predict** to see whether the customer is likely to stay or churn.
    """)



st.markdown(f"""
<style>
.image-container {{
    display: flex;
    justify-content: center;
    margin-top: 20px;
    margin-bottom: 20px;
}}

.image-container img {{
    width: 800px;
    border-radius: 15px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.35);
}}
</style>

<div class="image-container">
    <img src="https://cdn.prod.website-files.com/64103d21294ba09537b876c8/698199d3c681249fabbf314f_e8033c1c.jpeg">
</div>
""", unsafe_allow_html=True)


st.markdown("""
## 📞 About Telco Customer Churn Prediction

Customer churn refers to the loss of customers who stop using a telecom company's services and switch to another provider. Predicting customer churn helps telecom companies identify customers who are at risk of leaving and take preventive actions to improve customer satisfaction and retention.

This application uses a Machine Learning model to analyze customer information such as gender, tenure, internet service, contract type, payment method, monthly charges, and other service-related features. Based on these details, the model predicts whether a customer is likely to **Stay** or **Churn**.
""")
            
left,right=st.columns(2)
with left:
    st.markdown("""            
    ### 🎯 Project Objectives
    - Predict customer churn accurately using Machine Learning.
    - Help telecom companies reduce customer loss.
    - Improve customer retention through early identification of high-risk customers.
    - Support better business decision-making using data-driven insights.

    ### 🚀 How to Use
    1. Enter the customer's details in the input fields.
    2. Click the **Predict** button.
    3. The application will display whether the customer is **Likely to Stay** or **Likely to Churn**.
    """)



with right:

    churn = df["Churn"].value_counts()
    fig, ax = plt.subplots(figsize=(2,2))
    colors = ["#0C113C86", "#3F1E5F"]   # Navy Blue, Purple
    ax.pie(
        churn.values,
        labels=churn.index,
        colors=colors,
        autopct='%1.1f%%',
        startangle=90,
        #shadow=True,                  # Shadow effect
    # explode=(0.03, 0.03),         # Slight separation
        wedgeprops=dict(
            width=0.32,               # Ring thickness
            edgecolor='White',
            linewidth=1
        ),
        textprops={
            'fontsize':5,
            'fontweight':'bold',
            'color':'black'
        }
    )
    ax.set_title(
        "Customer Churn Distribution",
        fontsize=6,
        fontweight='bold',
        color='#0A2A66',
        pad=20)

    ax.axis('equal')

    st.pyplot(fig)








st.markdown("""
<style>

/* Sidebar background */
section[data-testid="stSidebar"]{
    background: linear-gradient(180deg, #2563EB, #7C3AED);
}

/* Selectbox background */
section[data-testid="stSidebar"] div[data-baseweb="select"] > div{
    background-color: #F8FAFC !important;
    color: #000000 !important;
    border-radius: 10px;
    border: 2px solid #FFFFFF;
}

/* Selectbox text */
section[data-testid="stSidebar"] div[data-baseweb="select"] span{
    color: #000000 !important;
}

/* Labels */
section[data-testid="stSidebar"] label{
    color: white !important;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)



st.sidebar.title("📞 Telco Customer Churn Prediction")

st.sidebar.write("Enter customer details below to predict whether the customer will churn.")

# Input Fields


gender = st.sidebar.selectbox("Gender",["Male","Female"])

SeniorCitizen = st.sidebar.selectbox("Senior Citizen",["NO","Yes"])

Partner = st.sidebar.selectbox("Partner", ["No","Yes"])

Dependents= st.sidebar.selectbox("Dependents",["No","Yes"])

tenure = st.sidebar.slider("Tenure (Months)", 0, 72, 12)

PhoneService = st.sidebar.selectbox("Phone Service",["No","Yes","No Internet Service"])

MultipleLines = st.sidebar.selectbox("Multiple Lines",["No","Yes","No Internet Service"])

InternetService = st.sidebar.selectbox("Internet Service",["DSL","Fiber optic","No"])

OnlineSecurity = st.sidebar.selectbox("Online Security",["No","Yes","No Internet Service"])

OnlineBackup = st.sidebar.selectbox("Online Backup", ["No","Yes","No Internet Service"])

DeviceProtection = st.sidebar.selectbox("Device Protection",["No","Yes","No Internet Service"])

TechSupport = st.sidebar.selectbox("Tech Support",["No","Yes","No Internet Service"])

StreamingTV = st.sidebar.selectbox("Streaming TV",["No","Yes","No Internet Service"])

StreamingMovies = st.sidebar.selectbox("Streaming Movies",["No","Yes","No Internet Service"])

Contract = st.sidebar.selectbox("Contract", ["Month-to-month","One year","Two year"])

PaperlessBilling = st.sidebar.selectbox("Paperless Billing",["No","Yes"])

PaymentMethod = st.sidebar.selectbox("Payment Method", ["Electronic check","Mailed check","Bank transfer (automatic)","Credit card (automatic)"])

MonthlyCharges = st.sidebar.number_input("Monthly Charges", min_value=0.0)

TotalCharges = st.sidebar.number_input("Total Charges", min_value=0.0)

st.markdown("""
<style>

/* Sidebar button */
section[data-testid="stSidebar"] div.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #2563EB, #7C3AED);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border: none;
    border-radius: 12px;
    padding: 12px;
    transition: all 0.3s ease;
}

/* Hover Effect */
section[data-testid="stSidebar"] div.stButton > button:hover {
    background: linear-gradient(90deg, #7C3AED, #2563EB);
    color: #FFD700;
    transform: scale(1.03);
    box-shadow: 0px 6px 18px rgba(124, 58, 237, 0.6);
    cursor: pointer;
}

/* Click Effect */
section[data-testid="stSidebar"] div.stButton > button:active {
    transform: scale(0.98);
}

</style>
""", unsafe_allow_html=True)

predict = st.sidebar.button("🚀 Predict Customer Churn", use_container_width=True)



# Prediction Button
if predict:
    gender = 0 if gender == "Female" else 1

    SeniorCitizen = 0 if SeniorCitizen == "No" else 1
    
    Partner = 0 if Partner == "No" else 1

    Dependents = 0 if Dependents == "No" else 1

    if PhoneService == "No":
       PhoneService= 0
    elif PhoneService == "Yes":
        PhoneService = 2
    elif PhoneService == "No internet service":
        PhoneService = 1

    if MultipleLines == "No":
       MultipleLines= 0
    elif MultipleLines == "Yes":
        MultipleLines = 2
    elif MultipleLines == "No internet service":
        MultipleLines = 1

    if InternetService == "DSL":
       InternetService= 0
    elif InternetService == "No":
        InternetService = 2
    elif InternetService == "Fiber optic":
        InternetService = 1


    if OnlineSecurity == "No":
       OnlineSecurity= 0
    elif OnlineSecurity == "Yes":
        OnlineSecurity = 2
    elif OnlineSecurity == "No internet service":
        OnlineSecurity = 1

    if OnlineBackup == "No":
       OnlineBackup= 0
    elif OnlineBackup == "Yes":
        OnlineBackup = 2
    elif OnlineBackup == "No internet service":
        OnlineBackup = 1

    if DeviceProtection == "No":
       DeviceProtection= 0
    elif DeviceProtection == "Yes":
        DeviceProtection = 2
    elif DeviceProtection == "No internet service":
        DeviceProtection = 1

    if TechSupport == "No":
       TechSupport= 0
    elif TechSupport == "Yes":
        TechSupport = 2
    elif TechSupport == "No internet service":
        TechSupport = 1

    if StreamingTV == "No":
       StreamingTV= 0
    elif StreamingTV == "Yes":
        StreamingTV = 2
    elif StreamingTV == "No internet service":
        StreamingTV = 1

    if StreamingMovies == "No":
       StreamingMovies= 0
    elif StreamingMovies == "Yes":
        StreamingMovies = 2
    elif StreamingMovies == "No internet service":
        StreamingMovies = 1


    if Contract == "Month-to-month":
       Contract= 0
    elif Contract == "Two year":
        Contract = 2
    elif Contract == "One year":
        Contract = 1

    PaperlessBilling = 0 if PaperlessBilling == "No" else 1
 

    if PaymentMethod == "Electronic check":
       PaymentMethod= 0
    elif PaymentMethod == "Mailed check":
        PaymentMethod = 1
    elif PaymentMethod == "Bank transfer (automatic)":
        PaymentMethod = 2
    elif PaymentMethod == "Credit card (automatic)":
        PaymentMethod = 3
    
    

    input_df = np.array([[
        gender,
        SeniorCitizen,
        Partner,
        Dependents,
        tenure,
        PhoneService,
        MultipleLines,
        InternetService,
        OnlineSecurity,
        OnlineBackup,
        DeviceProtection,
        TechSupport,
        StreamingTV,
        StreamingMovies,
        Contract,
        PaperlessBilling,
        PaymentMethod,
        MonthlyCharges,
        TotalCharges
    ]])

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.error("⚠️ Customer is likely to Churn.")
    else:
        st.success("✅ Customer is likely to Stay.")