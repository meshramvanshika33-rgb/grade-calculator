import streamlit as st

# ----------------- PAGE CONFIG -----------------
st.set_page_config(page_title="Grade Calculator", page_icon="📊", layout="centered")

# ----------------- CUSTOM LAVENDER THEME -----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #e6e6fa, #d8bfd8, #ffffff);
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #4b0082;
}

.bold-text {
    font-weight: bold;
    font-size: 18px;
    color: #2e0854;
}
</style>
""", unsafe_allow_html=True)

# ----------------- TITLE -----------------
st.markdown("<div class='title'>📊 Grade Calculator</div>", unsafe_allow_html=True)

st.write("")

# ----------------- STUDENT DETAILS -----------------
st.markdown("### 🧑 Student Details")

student_name = st.text_input("Enter Student Name")
mother_name = st.text_input("Enter Mother's Name")

# ----------------- SUBJECT MARKS -----------------
st.markdown("### 📚 Enter Marks (Out of 100)")

sub1 = st.number_input("Subject 1", 0, 100)
sub2 = st.number_input("Subject 2", 0, 100)
sub3 = st.number_input("Subject 3", 0, 100)
sub4 = st.number_input("Subject 4", 0, 100)
sub5 = st.number_input("Subject 5", 0, 100)

# ----------------- CALCULATION -----------------
if st.button("Calculate Grade"):
    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = (total / 500) * 100

    if percentage >= 90:
        grade = "A+ (Excellent)"
    elif percentage >= 75:
        grade = "A (Very Good)"
    elif percentage >= 60:
        grade = "B (Good)"
    elif percentage >= 40:
        grade = "C (Pass)"
    else:
        grade = "F (Fail)"

    # ----------------- RESULT -----------------
    st.markdown("## 🎯 Result")

    st.markdown(f"<p class='bold-text'>Student Name: {student_name}</p>", unsafe_allow_html=True)
    st.markdown(f"<p class='bold-text'>Mother's Name: {mother_name}</p>", unsafe_allow_html=True)

    st.markdown(f"<p class='bold-text'>Total Marks: {total}/500</p>", unsafe_allow_html=True)
    st.markdown(f"<p class='bold-text'>Percentage: {percentage:.2f}%</p>", unsafe_allow_html=True)
    st.markdown(f"<p class='bold-text'>Grade: {grade}</p>", unsafe_allow_html=True)
