import streamlit as st
from analyzer.code_quality import run_flake8, run_black, run_radon

st.title('🧑‍💻 AI Code Reviewer')

uploaded_file = st.file_uploader('Upload Python file', type=['py'])

if uploaded_file:
    code = uploaded_file.read().decode('utf-8')
    st.code(code, language='python')

    with open('temp_code.py', 'w', encoding='utf-8') as f:
        f.write(code)

    st.header('Linting with flake8')
    flake8_result = run_flake8('temp_code.py')
    st.text(flake8_result or 'No issues found.')

    st.header('Formatting check with black')
    black_result = run_black('temp_code.py')
    st.text(black_result or 'No issues found.')

    st.header('Complexity with radon')
    radon_result = run_radon('temp_code.py')
    st.text(radon_result or 'No issues found.')
