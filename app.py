from pathlib import Path
import streamlit as st 
from PIL import Image

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd

css_file = current_dir/"styles"/ "main.css"
resume_file = current_dir/"assets"/"NILANJAN GHOSH.pdf"
profile_pic = current_dir/"assets"/"788.jpg"
social_logo = current_dir/"assets"

PAGE_TITLE = "Digital CV | Nilanjan Ghosh"
PAGE_ICON = ":wave:"
NAME ="Nilanjan Ghosh"
DESCRIPTION ="""
Motivated computer science student specializing in applied machine learning, Python, and Linux, with a focus on crafting data-driven solutions."""
EMAIL ="csz248005@cse.iitd.ac.in"
PROJECTS={
    ":construction: LLM Project":"https://github.com/nil0711/LM_Reseach_Project",
    ":speech_balloon: Chat Analysis with Sentiment Analyzer" :"https://miniproject-senti.streamlit.app/",
    ":file_folder: File Manager":"https://github.com/nil0711/CODE/blob/main/tkinter_test/test5.py"
    
}
st.set_page_config(page_title = PAGE_TITLE,page_icon=PAGE_ICON ,initial_sidebar_state="collapsed")


with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html = True)
with open(resume_file, "rb") as pdf_file:
    PDF = pdf_file.read()
profile_pic = Image.open(profile_pic)

col1 , col2 = st.columns(2,gap="small")

with col1:
    st.image(profile_pic,width = 220)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data = PDF,
        file_name=resume_file.name,
        mime = "application/octet-sream"
        
    )
    st.write("📨", EMAIL)
SOCIAL_MEDIA={
    "LinkedIN":"https://www.linkedin.com/in/nilanjan-ghosh-iitd/",
    "GitHub":"https://github.com/nil0711",
    "X":"https://x.com/nil0711_iitd",
    

}
platform_images = {
    "LinkedIN": "linkedin.png",
    "GitHub": "github.png",
    "X": "x.png",
}

    
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    # Displaying the image with a width of 24
    image_path = f"{social_logo}/{platform_images[platform]}"
    img = Image.open(image_path)
    with cols[index]:
        subcol1, subcol2 = st.columns([0.1,1])
        subcol1.image(img, width=24, use_column_width=False)
        subcol2.write(f"[{platform}]({link})")
        hide_img_fs = '''
        <style>
        button[title="View fullscreen"]{
            visibility: hidden;}
        </style>
        '''

        st.markdown(hide_img_fs, unsafe_allow_html=True)

st.write('#')
st.subheader("About Me")
st.write('''
         
I am an aspiring computer scientist with strong skills in Python, Linux, and applied machine learning. I have demonstrated the ability to create data-driven solutions using statistical modeling and algorithmic optimization techniques. I am passionate about innovation and learning new technologies. I am seeking a challenging role in a forward-thinking organization where I can contribute my expertise, collaborate on impactful projects, and push the technological boundaries.
         ''')
st.write("---")
st.subheader("Experience & Qualifications")
st.write("""
        - 🏅 Qualified in GATE 2024 in CS and DA
        - 🏅 Qualified for JRF in Computer Science in December 2023
        - 🎓 Pursuing Research in Computer Science at the Indian Institute of Technology, Delhi, starting from July 2024
        - 🎓 Earned a Master's degree in Computer Science from Pondicherry University, in June 2024        
        - 🎓 Earned a Bachelor's degree in Mathematics from St. Xavier's College, Kolkata in May 2020
        - 🔎 Strong problem-solving and analytical skills
        - 💬 Good communication and teamwork skills
         """)
st.write("---")

st.subheader("Skills")
st.write(
    '''
    - 🐍 Python Programming: Numpy, Pandas, sklearn, Pytorch, Keras, Streamlit, Seaborn, Mathplotlib, google.generativeai, openai, tensorflow, nltk, Plotly, Faiss, langchain
    - 🧠 Machine Learning: Decision Tree, Neural Networks, Bayesian Network, Markov Model, Hidden Markov Model, Clustering, Classification, Deep Learning, LLM, NLP
    - 🐧 Linux: Linux System Administration, Shell Scripting, Samba, LVM, Git, C/C++/Java/Python coding debugging in terminal
    - 💾 Databases: MongoDB, MySql, ChromaDB

    '''
)
st.write("---")
st.subheader("Projects & Accomplishments")
for project, link in PROJECTS.items():
    st.write(f"- [{project}]({link})")

st.write("---")

