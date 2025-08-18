import streamlit as st
from analyzer.style_checker import check_flake8, check_black, auto_format_black
from analyzer.complexity_checker import check_radon
from analyzer.utils import save_code_to_tempfile

# Page configuration
st.set_page_config(
    page_title="🧠 AI Code Reviewer",
    layout="wide",
    initial_sidebar_state="auto"
)

# Inject custom style for better visuals
st.markdown("""
    <style>
    .main {background-color: #f9f9f9;}
    .report-title {
        font-size: 28px;
        font-weight: 600;
        color: #4B8BBE;
        margin-bottom: 10px;
    }
    .stCodeBlock {background-color: #f1f1f1;}
    .css-1aumxhk {font-size: 18px;}
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title Section
st.markdown("<div class='report-title'>🧑‍💻 AI Code Reviewer</div>", unsafe_allow_html=True)
st.write("Paste Python code below to get a style check, formatting, and complexity report.")

# Input area for code
code_input = st.text_area("📄 Paste your Python code here:", height=300)

# Button to trigger analysis
if st.button("🚀 Analyze Code"):

    if not code_input.strip():
        st.warning("⚠️ Please paste some Python code first.")
    else:
        code_path = save_code_to_tempfile(code_input)

        # Layout with columns
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🎯 Style Analysis (flake8)")
            flake8_output = check_flake8(code_path)
            st.code(flake8_output, language="text")

            st.subheader("🎨 Format Check (black)")
            black_output = check_black(code_path)
            st.code(black_output, language="text")

        with col2:
            st.subheader("🧼 Auto-formatted Code")
            auto_format_black(code_path)  # modifies the file
            with open(code_path, "r", encoding="utf-8") as f:
                formatted_code = f.read()
            st.code(formatted_code, language="python")

            st.subheader("📊 Code Complexity (radon)")
            radon_output = check_radon(code_path)
            st.code(radon_output, language="text")
