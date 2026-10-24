
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Student Profile",
    page_icon="🎓",
    layout="wide"
)

# Sidebar
st.sidebar.title("🎓 Student Profile App")
st.sidebar.write(
    "This app displays student information, skills, "
    "learning goals, progress, and next steps."
)

# Main area
st.title("🎓 Student Profile Page")

st.header("Haroon Usman")
st.subheader("Course: Software Engineering")

st.write("Welcome to my student profile!")

# Two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("💻 My Skills")
    st.write("- Python")
    st.write("- Manual Software Testing")
    st.write("- SQL")
    st.write("- HTML and CSS")

with col2:
    st.subheader("🎯 My Goals")
    st.write("- Learn automation testing")
    st.write("- Improve Python skills")
    st.write("- Get a QA Engineer job")
    st.write("- Build practical projects")

# Expander
with st.expander("📞 Contact Preferences"):
    st.write("Preferred Contact: Email")
    st.write("Best Time: Afternoon")
    st.write("Purpose: Learning and career opportunities")

# Tabs
tab1, tab2, tab3 = st.tabs(
    ["Profile", "Progress", "Next Steps"]
)

with tab1:
    st.subheader("Student Profile")
    st.write("Name: Haroon Usman")
    st.write("Field: Software Engineering")
    st.write("Interest: Software Quality Assurance")

with tab2:
    st.subheader("Learning Progress")
    st.write("Manual Testing: Completed internship training")
    st.write("Python: Learning programming fundamentals")
    st.write("Automation: Preparing to learn Selenium")

    st.progress(60)
    st.caption("Overall learning progress: 60% (sample value)")

with tab3:
    st.subheader("My Next Steps")
    st.write("1. Practice Python daily")
    st.write("2. Learn Selenium with Python")
    st.write("3. Write automated test scripts")
    st.write("4. Apply for QA jobs")

# Empty placeholder
message_placeholder = st.empty()

st.write("Explore the tabs to learn more about the student.")

# Assign a message to the placeholder later
message_placeholder.success(
    "Student profile loaded successfully!"
)
