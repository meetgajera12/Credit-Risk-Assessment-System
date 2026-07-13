import streamlit as st
import requests
import base64

API_URL = 'http://127.0.0.1:8000/predict'


# Initialize Session State
if "step" not in st.session_state:
    st.session_state.step = 0

if "input_data" not in st.session_state:
    st.session_state.input_data = {}


# background image
def set_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg(r"C:\Users\meet.gajera\OneDrive\Desktop\hcdr__\images\background_img1.jpeg")


# Time Line
if st.session_state.step > 0:
    steps = [
        ("👤", "Personal"),
        ("💼", "Employment"),
        ("🏦", "Loan"),
        ("📊", "Bureau"),
        ("📄", "Previous"),
        ("🔍", "Predict")
    ]

    timeline = ""

    for i, (icon, name) in enumerate(steps, start=1):

        if i < st.session_state.step:
            status = "✔"
        elif i == st.session_state.step:
            status = "●"
        else:
            status = "○"

        timeline += f"""
        <div style="display:inline-block;
                    text-align:center;
                    width:16%;">
            <div style="font-size:22px">{status}</div>
            <div style="font-size:19px">{icon}</div>
            <div style="font-size:13px">{name}</div>
        </div>
        """

    st.markdown(timeline, unsafe_allow_html=True)
    st.divider()



# Home Page
if st.session_state.step == 0:
    st.title("🏦 Home Credit Default Risk Prediction")
    st.caption(
        "Predict the probability of loan default using Machine Learning."
    )

    st.markdown("""
    ### Welcome!

    This application predicts the probability that a loan applicant will default using a **LightGBM machine learning model** trained on the **Home Credit Default Risk** dataset.

    The prediction considers multiple factors, including:

    - 👤 Personal & Family Information
    - 💼 Employment & Income Details
    - 🏦 Loan Information
    - 📊 Credit Bureau History
    - 📄 Previous Home Credit Applications
    - 🔍 Loan Default Prediction

    Navigate through each section, provide the required information, and receive an AI-powered credit risk assessment along with the predicted default probability.
    """)

    st.divider()
    left,center,right = st.columns([1,6,1])
    with center:
        if st.button("Start", use_container_width=True):
            st.session_state.step = 1
            st.rerun()


# Input Field
if st.session_state.step == 1:

    st.subheader("👤 Personal Information")
    st.caption("Basic applicant and family details")
   
    col1,col2 = st.columns(2)

    with col1:
        gender = st.selectbox('Gender:',['Male', 'Female'], index=0)
        age = st.number_input('Age:',min_value=18.0, max_value=100.0)
        edu_type = st.selectbox('Education Type:', 
                                ['Secondary / secondary special', 'Higher education',
                                    'Incomplete higher', 'Lower secondary', 'Academic degree'])
        family_type = st.selectbox('Family Status:',
                                        ['Single / not married', 'Married', 'Civil marriage', 'Widow',
                                            'Separated', 'Unknown'])
        housing_type = st.selectbox('Housing Type:',
                                    ['House / apartment', 'Rented apartment', 'With parents',
                                        'Municipal apartment', 'Office apartment', 'Co-op apartment'])

    with col2:
        children = st.number_input('No. of Children:', step=1)
        family_mem = st.number_input('Total Family Member:', step=1)
        car = st.selectbox("Car Own:", ['No','Yes'])
        reality = st.selectbox("Realty Own", ['No','Yes'])
        curr_phone = st.number_input("Since how many years you have current Phone:")

    st.divider()
    left,center,right = st.columns([1,6,1])
    with left:
        if st.button("↶ᯓ"):
            st.session_state.step = 0
            st.rerun()
    with right:
        if st.button("ᯓ➤"):

            st.session_state.input_data["CODE_GENDER"] = gender
            st.session_state.input_data["AGE"] = age
            st.session_state.input_data["NAME_EDUCATION_TYPE"] = edu_type
            st.session_state.input_data["NAME_FAMILY_STATUS"] = family_type
            st.session_state.input_data["NAME_HOUSING_TYPE"] = housing_type
            st.session_state.input_data["CNT_CHILDREN"] = children
            st.session_state.input_data["CNT_FAM_MEMBERS"] = family_mem
            st.session_state.input_data["FLAG_OWN_CAR"] = car
            st.session_state.input_data["FLAG_OWN_REALTY"] = reality
            st.session_state.input_data["YEARS_CURRENT_PHONE"] = curr_phone            

            st.session_state.step = 2
            st.rerun()



if st.session_state.step == 2:
    
    st.subheader("💼 Employment Details")
    st.caption("Employment status and income information")
    
    col1,col2, = st.columns(2)

    with col1:
        income_type = st.selectbox('Income Type:',
                                    ['Working', 'State servant', 'Commercial associate', 'Pensioner',
                                        'Unemployed', 'Student', 'Businessman', 'Maternity leave'])
        occupation_type = st.selectbox('Occupation',
                                    ['Laborers', 'Core staff', 'Accountants', 'Managers', 'Unknown',
                                        'Drivers', 'Sales staff', 'Cleaning staff', 'Cooking staff',
                                        'Private service staff', 'Medicine staff', 'Security staff',
                                        'High skill tech staff', 'Waiters/barmen staff',
                                        'Low-skill Laborers', 'Realty agents', 'Secretaries', 'IT staff',
                                        'HR staff'])
        org_type = st.selectbox('Organization:',
                            ['Business & Corporate', 'Education', 'Government', 'Other',
                                'Manufacturing', 'Healthcare', 'Trade & Self-employed',
                                'Transport', 'Construction', 'Hospitality', 'Banking & Finance',
                                'IT & Telecom'])

    with col2:
        year_emp = st.number_input('Years Employed:',step=0.5)
        income = st.number_input("Annual Income:",min_value=0.00, step=1.0)


    st.divider()
    left,center,right = st.columns([1,6,1])
    with left:
        if st.button("↶ᯓ"):
            st.session_state.step = 1
            st.rerun()
    with right:
        if st.button("ᯓ➤"):

            st.session_state.input_data["NAME_INCOME_TYPE"] = income_type
            st.session_state.input_data["OCCUPATION_TYPE"] = occupation_type
            st.session_state.input_data["ORG_GROUP"] = org_type
            st.session_state.input_data["YEARS_EMPLOYED"] = year_emp
            st.session_state.input_data["AMT_INCOME_TOTAL"] = income

            st.session_state.step = 3
            st.rerun()


        
if st.session_state.step == 3:
    
    st.subheader("🏦 Loan Details")
    st.caption("Requested loan and financial information")
    
    contract_type = st.selectbox('Contract Type:', ['Cash loans', 'Revolving loans'])
    credit = st.number_input("Credit Amount:", step=1.0)
    annuity =  st.number_input("Annuity:", step=1.0)
    goods_price = st.number_input("Godds Price:", step=1.0)

    st.divider()
    left,center,right = st.columns([1,6,1])
    with left:
        if st.button("↶ᯓ"):
            st.session_state.step = 2
            st.rerun()
    with right:
        if st.button("ᯓ➤"):

            st.session_state.input_data["NAME_CONTRACT_TYPE"] = contract_type
            st.session_state.input_data["AMT_CREDIT"] = credit
            st.session_state.input_data["AMT_ANNUITY"] = annuity
            st.session_state.input_data["AMT_GOODS_PRICE"] = goods_price

            st.session_state.step = 4
            st.rerun()


if st.session_state.step == 4:
    
    st.subheader("📊 Credit Bureau History")
    st.caption("Existing credit history and bureau records")

    bureau_history = st.radio("Do you have previous credit history?",['No','Yes'])

    if bureau_history == 'Yes':
        with st.expander('📈 Credit History',expanded=True):
            col3,col4 = st.columns(2)

            with col3:
                Average_Credit_Age = st.number_input("Average Credit Age:")
                Minimum_Credit_Age = st.number_input("Minimum Credit Age:")
                Maximum_Credit_Age = st.number_input("Maximum Credit Age:")

                Maximum_Debt_Ratio = st.number_input("Maximum Debt Ratio:")
                Average_Debt_Ratio = st.number_input("Average Debt Ratio:")

                Total_Credit_Amount = st.number_input("Total Credit Amount:")
                Average_Credit_Amount = st.number_input("Average Credit Amount:")
                Maximum_Credit_Amount = st.number_input("Maximum Credit Amount:")

            with col4:
                Total_Outstanding_Debt = st.number_input("Total Outstanding Debt:")
                Average_Outstanding_Debt = st.number_input("Average Outstanding Debt:")

                Total_Credit_Limit = st.number_input("Total Credit Limit:")

                Credit_Utilization = st.number_input("Credit Utilization:")

                Number_Active_Loans = st.number_input("Number of Active Loans:")
                Number_closed_Loans = st.number_input("Number of Closed Loans:")
                Number_Sold_Loans = st.number_input("Number of Sold Loans:")
                Number_Bad_Debt_Accounts = st.number_input("Number of Bad Debt Accounts:")
        
    else:
        Average_Credit_Age = 0
        Minimum_Credit_Age = 0
        Maximum_Credit_Age = 0

        Maximum_Debt_Ratio = 0
        Average_Debt_Ratio = 0

        Total_Credit_Amount = 0
        Average_Credit_Amount = 0
        Maximum_Credit_Amount = 0

        Total_Outstanding_Debt = 0
        Average_Outstanding_Debt = 0

        Total_Credit_Limit = 0

        Credit_Utilization = 0

        Number_Active_Loans = 0
        Number_closed_Loans = 0
        Number_Sold_Loans = 0
        Number_Bad_Debt_Accounts = 0

    st.divider()
    left,center,right = st.columns([1,6,1])
    with left:
        if st.button("↶ᯓ"):
            st.session_state.step = 3
            st.rerun()
    with right:
        if st.button("ᯓ➤"):

            st.session_state.input_data['HAS_BUREAU_HISTORY'] = bureau_history
            st.session_state.input_data["YEARS_CREDIT_mean"] = Average_Credit_Age
            st.session_state.input_data["YEARS_CREDIT_min"] = Minimum_Credit_Age
            st.session_state.input_data["YEARS_CREDIT_max"] = Maximum_Credit_Age

            st.session_state.input_data["DEBT_RATIO_mean"] = Average_Debt_Ratio  
            st.session_state.input_data["DEBT_RATIO_max"] = Maximum_Debt_Ratio 

            st.session_state.input_data["AMT_CREDIT_SUM_sum"] = Total_Credit_Amount 
            st.session_state.input_data["AMT_CREDIT_SUM_mean"] = Average_Credit_Amount 
            st.session_state.input_data["AMT_CREDIT_SUM_max"] = Maximum_Credit_Amount 

            st.session_state.input_data["AMT_CREDIT_SUM_DEBT_sum"] = Total_Outstanding_Debt 
            st.session_state.input_data["AMT_CREDIT_SUM_DEBT_mean"] = Average_Outstanding_Debt 

            # Automatically set these
            st.session_state.input_data["AMT_CREDIT_SUM_DEBT_MISSING_sum"] = 0
            st.session_state.input_data["AMT_CREDIT_SUM_DEBT_MISSING_mean"] = 0

            st.session_state.input_data["AMT_CREDIT_SUM_LIMIT_sum"] = Total_Credit_Limit

            # Automatically set these
            st.session_state.input_data["AMT_CREDIT_SUM_LIMIT_MISSING_sum"] = 0
            st.session_state.input_data["AMT_CREDIT_SUM_LIMIT_MISSING_mean"] = 0

            st.session_state.input_data["CREDIT_UTILIZATION_mean"] = Credit_Utilization 

            st.session_state.input_data["HAS_DEBT_sum"] = 0 
            st.session_state.input_data["IS_ACTIVE_sum"] = Number_Active_Loans 
            st.session_state.input_data["IS_CLOSED_sum"] = Number_closed_Loans 
            st.session_state.input_data["IS_SOLD_sum"] = Number_Sold_Loans 
            st.session_state.input_data["IS_BAD_DEBT_sum"] = Number_Bad_Debt_Accounts 

            st.session_state.step = 5
            st.rerun()
        

    
if st.session_state.step == 5:
    
    st.subheader("📄 Previous Home Credit Applications")
    st.caption("Previous Home Credit loan application history")

    pre_app = st.radio("Have you previously applied for a Home Credit loan?", ['No','Yes'])

    if pre_app == 'Yes':
        with st.expander("📄 Previous Application Details", expanded=True):
            num_prev_app = st.number_input(
                "Number of Previous Applications",
                min_value=1,
                step=1
            )

            Approval_Rate = st.number_input(
                "Approval Rate",
                min_value=0.0,
                max_value=1.0,
                step=0.01
            )
    else:
        num_prev_app = 0
        Approval_Rate = 0


    st.divider()
    left,center,right = st.columns([1,6,1])
    with left:
        if st.button("↶ᯓ"):
            st.session_state.step = 4
            st.rerun()
    with right:
        if st.button("ᯓ➤"):

            st.session_state.input_data["PREV_APP_COUNT"] = num_prev_app
            st.session_state.input_data["APPROVAL_RATE"] = Approval_Rate

            st.session_state.step = 6
            st.rerun()


if st.session_state.step == 6:
    
    st.subheader("🔍 Loan Default Prediction")
    st.caption("Review all information and generate prediction")

    if st.button("🔍 Assess Credit Risk"):
        
        with st.spinner("Predicting..."):
            try:
                response = requests.post(API_URL, json=st.session_state.input_data)

                if response.status_code == 200:
                    
                    result = response.json()

                    prediction = result["prediction"]
                    risk = result["risk"]
                    confidence = result["confidence"]
                    class_prob = result["class_probabilities"]

                    st.success(f"Prediction : {prediction}")

                    st.info(f"Risk : {risk}")

                    st.metric(
                        "Confidence",
                        f"{confidence*100:.2f}%"
                    )

                    st.write("### Class Probabilities")

                    st.write(
                        f"🟢 No Default : {class_prob['No Default']*100:.2f}%"
                    )

                    st.write(
                        f"🔴 Default : {class_prob['Default']*100:.2f}%"
                    )

                else:

                    st.error(response.text)

            except requests.exceptions.ConnectionError:

                st.error("FastAPI server is not running.")

    st.divider()
    left,center,right = st.columns([3,6,3])

    with left:
        if st.button('🔄 Evaluate Another Applicant'):
            st.session_state.step = 1
            st.rerun()

    with right:
        if st.button('🏠 Back to Home'):
            st.session_state.step = 0
            st.rerun()
