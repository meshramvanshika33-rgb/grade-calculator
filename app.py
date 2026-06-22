import streamlit as st

st.set_page_config(
    page_title="Grade Calculator",
    page_icon="🧮",
    layout="centered"
)

# ---------- CSS ----------

st.markdown("""
<style>

.stApp{
background: linear-gradient(
135deg,
#dff6ff,
#bde0fe,
#ffc8dd,
#ffffff);
}

/* Title */
.title{
text-align:center;
font-size:42px;
font-weight:bold;
color:#0077b6;
margin-bottom:20px;
}

/* Glass Card */
.card{
background:rgba(255,255,255,0.60);
backdrop-filter:blur(15px);
padding:25px;
border-radius:25px;
box-shadow:0px 8px 20px rgba(0,119,182,0.15);
}

/* Labels */
.label{
font-size:22px;
font-weight:bold;
color:#0077b6;
}

/* Result Card */
.result{
background:linear-gradient(
135deg,
#dff6ff,
#ffc8dd);
padding:25px;
border-radius:20px;
box-shadow:0px 8px 20px rgba(0,0,0,0.08);
margin-top:20px;
text-align:center;
color:#000000;
}

/* Grade */
.grade{
font-size:35px;
font-weight:bold;
color:#000000;
}

/* Badge */
.badge{
font-size:22px;
font-weight:bold;
color:#000000;
}

/* Stars */
.star{
font-size:28px;
}

</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------

st.markdown(
'<div class="title">🧮 Grade Calculator 🎓</div>',
unsafe_allow_html=True
)

# ---------- INPUT SECTION ----------

st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown(
'<p class="label">👩‍🎓 Student Name</p>',
unsafe_allow_html=True
)

name = st.text_input("")

st.markdown(
'<p class="label">📚 Enter Marks (Out of 100)</p>',
unsafe_allow_html=True
)

sub1 = st.number_input("📘 Subject 1", 0, 100)
sub2 = st.number_input("📗 Subject 2", 0, 100)
sub3 = st.number_input("📕 Subject 3", 0, 100)
sub4 = st.number_input("📙 Subject 4", 0, 100)
sub5 = st.number_input("📓 Subject 5", 0, 100)

if st.button("💖 Calculate Grade"):
    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
        badge = "🏆 Outstanding"
        stars = "⭐⭐⭐⭐⭐"

    elif percentage >= 80:
        grade = "A"
        badge = "🥇 Excellent"
        stars = "⭐⭐⭐⭐"

    elif percentage >= 70:
        grade = "B"
        badge = "🌟 Very Good"
        stars = "⭐⭐⭐"

    elif percentage >= 60:
        grade = "C"
        badge = "👍 Good"
        stars = "⭐⭐"

    elif percentage >= 50:
        grade = "D"
        badge = "🙂 Average"
        stars = "⭐"

    else:
        grade = "F"
        badge = "📚 Need Improvement"
        stars = "❌"

    st.markdown(f"""
    <div class="result">

        <h2 style="color:#000000;">👩‍🎓 {name}</h2>

        <p style="font-size:22px;font-weight:bold;color:#000000;">
            📊 Total Marks : {total}/500
        </p>

        <p style="font-size:22px;font-weight:bold;color:#000000;">
            🎯 Percentage : {percentage:.2f}%
        </p>

        <p style="font-size:35px;font-weight:bold;color:#000000;">
            🎓 Grade : {grade}
        </p>

        <p style="font-size:22px;font-weight:bold;color:#000000;">
            {badge}
        </p>

        <p style="font-size:28px;">
            {stars}
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.progress(int(percentage))

st.markdown("</div>", unsafe_allow_html=True)
