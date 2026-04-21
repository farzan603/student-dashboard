import streamlit as st
import pandas as pd

df = pd.read_csv('student_dropout_behavior_dataset.csv')
print(df.columns)

# Sidebar
st.sidebar.title('📊 Dashboard')
page = st.sidebar.selectbox(
    'Select Option',
    ['HOME','Student Search Page','Performance Analysis Page']
)


# ---------------- HOME ----------------


if page == 'HOME':
    st.title("🏠 Home")

    st.title("🎓 Student Dashboard")
    st.write("Welcome! Yaha aap students ka overall performance dekh sakte ho.")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Students", len(df))
    col2.metric("Avg Marks", round(df['final_marks'].mean(), 2))
    col3.metric("Avg CGPA", round(df['previous_gpa'].mean(), 2))

    st.write("### 👨‍🎓 Gender Distribution")
    st.bar_chart(df['gender'].value_counts())

    top_students = df.sort_values('final_marks', ascending=False).head(5)
    st.write("### 🏆 Top Performers")
    st.dataframe(top_students)

    avg = df['final_marks'].mean()

    if avg > 70:
        st.success("Overall performance is good 👍")
    else:
        st.warning("Students need improvement ⚠️")

    st.info("👉 Sidebar se different sections explore karo")













# ---------------- SEARCH ----------------

elif page == 'Student Search Page':
    st.title("🔍 Student Search")

    st.write("### 🔍 Search Student")
    search = st.text_input("Enter Student Name or Id")
    results = df[df['name'].str.contains(search,case=False)]
    if not results.empty:
        st.write("### 📄 Student Details")
        st.dataframe(results)
    else:
        st.warning("No student found")

    if len(results) == 1:
        student = results.iloc[0]
        st.write("### 🎓 Student Info")
        st.write("Name:", student['name'])
        st.write("ID:", student['student_id'])
        st.write("Age:", student['age'])
        st.write("Marks:", student['final_marks'])
        st.write("CGPA:", student['previous_gpa'])

    if len(results) == 1:
        st.write("### 📊 Performance")
        st.bar_chart({
            "Marks": [student['final_marks']],
            "CGPA": [student['previous_gpa']]

        })

    if len(results) == 1:
        if student['final_marks'] > 25:
            st.success("Great performance 🎯")
        else:
            st.info("Can improve 👍")



# ---------------- ANALYSIS ----------------

elif page == 'Performance Analysis Page':
    st.title("📊 Performance Analysis")

    st.write("### 📊 Overall Performance")

    col1, col2, col3 = st.columns(3)
    col1.metric("Average Marks",df['final_marks'].mean())
    col2.metric("Highest Marks:",df['final_marks'].max())
    col3.metric("Lowest Marks:",df['final_marks'].min())

    st.write("### 📈 Marks Distribution")
    st.bar_chart(df['final_marks'])

    st.write("### 📊 CGPA vs Marks")
    st.scatter_chart(df[['previous_gpa', 'final_marks']])

    st.write("### 🏆 Top 5 Students")
    top = df.sort_values('final_marks', ascending=False).head(5)
    st.write(top)

    st.write("### ⚠️ Low Performers")
    low = df.sort_values('final_marks',ascending=True).head(5)
    st.write(low)

    st.write("### 👨‍🎓 Gender Performance")
    gender_perf = df.groupby('gender')['final_marks'].mean()
    st.bar_chart(gender_perf)

    avg = df['final_marks'].mean()
    if avg > 75:
        st.success("Overall performance is excellent 🎯")
    elif avg > 50:
        st.info("Performance is average 👍")
    else:
        st.warning("Performance is low ⚠️ Need improvement")





