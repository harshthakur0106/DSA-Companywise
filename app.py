import streamlit as st
import pandas as pd
import os

# --- Config ---
st.set_page_config(page_title="CompanyWise DSA Q&A", layout="wide")
st.title("💼 Comapny Wise DSA Sheet")

# --- Load Answer CSV (Global for all companies) ---
ANSWER_PATH = "answers/answers.csv"  # single file with answers
answers_df = pd.read_csv(ANSWER_PATH)

# Clean the answer data and ensure column names match
answers_df = answers_df[["Answer", "Question"]]  # Keeping only the required columns
answers_df.columns = ["Answer", "Question"]
answers_df["Question"] = answers_df["Question"].astype(str)  # Ensure 'Question' column is string type

# --- Sidebar Filters ---
st.sidebar.header("🔍 Filter Questions")

# Get the list of companies (CSV files in 'data' folder)
companies = [file.replace(".csv", "") for file in os.listdir("data") if file.endswith(".csv")]
selected_company = st.sidebar.selectbox("Select Company", ["Select a Company"] + companies)

difficulties = st.sidebar.multiselect("Select Difficulty", ["All", "Easy", "Medium", "Hard"])
search_query = st.sidebar.text_input("Search by Question Name")

# --- Load the Selected Company's Questions CSV Dynamically ---
if selected_company != "Select a Company":
    company_file_path = f"data/{selected_company}.csv"
    questions_df = pd.read_csv(company_file_path, header=None)
    questions_df.columns = ["ID", "Question", "Acceptance", "Difficulty", "Frequency", "Link"]
    questions_df["Company"] = selected_company

    # Clean up links if needed
    questions_df["Link"] = questions_df["Link"].apply(lambda x: x if str(x).startswith("http") else "https://" + str(x))

    # --- Ensure 'Question' column is of string type ---
    questions_df["Question"] = questions_df["Question"].astype(str)

    # --- Merge on 'Question ID' ---
    merged_df = pd.merge(questions_df, answers_df, left_on="ID", right_on="Question", how="left")

    # --- Drop Duplicate Question Column After Merge ---
    merged_df = merged_df.drop(columns=["Question_y"])  # Drop 'Question_y' column from answers_df
    merged_df = merged_df.rename(columns={"Question_x": "Question"})  # Rename 'Question_x' to 'Question'

    # --- Apply Filters ---
    filtered_df = merged_df.copy()
    if difficulties != ["All"]:
        filtered_df = filtered_df[filtered_df["Difficulty"].isin(difficulties)]
    if search_query:
        filtered_df = filtered_df[filtered_df["Question"].str.contains(search_query, case=False)]

    # --- UI Display ---
    st.markdown(f"### Showing {len(filtered_df)} Questions")

    for _, row in filtered_df.iterrows():
        with st.expander(f"{row['Question']} ({row['Company']} - {row['Difficulty']})"):
            st.markdown(f"🔗 [LeetCode Link]({row['Link']})")
            st.markdown(f"**Acceptance:** {row['Acceptance']} &nbsp;&nbsp; | &nbsp;&nbsp; **Frequency:** {row['Frequency']}")
            
            if pd.notna(row["Answer"]):
                st.markdown("#### 🧠 Solution:")
                st.code(row["Answer"], language="cpp")
            else:
                st.warning("No answer available for this question.")
else:
    st.warning("Please select a company to view the questions.")
