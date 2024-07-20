import streamlit as st
from PIL import Image
import json
import requests
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
# Navigation
with st.sidebar:
  selected = option_menu(
            menu_title="Resume",  # required
            options=["Home","Education" ,"Work Experience","Projects","Skills", "Social Media"],  # required
            
            default_index=0,  # optional
            
            styles={
                "container": {"padding": "55!important", "background-color": "#fafafa"},
                "icon": {"color": "blue"},
                "nav-link": {
                    "text-align": "left",
                    "font-size": "20px",
                    "margin": "10px",
                  
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "pink"},
            },
        )

#####################


#####################


#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)
##############################
# Header 
#####################3
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_edu = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_hxart9lz.json")
lottie_hello = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_calza6zj.json")
lottie_work1 = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_cmaqoazd.json")
lottie_work2 = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_acryqbdv.json")
lottie_project1=load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_odkqqok3.json")
lottie_project2=load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_dsmgi54l.json")
lottie_project3=load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_4b8xfsqj.json")
if selected == "Home":
  st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
     # canvas
    height=300,
    width=700,
    key=None,
)
  st.markdown('<h1 style="text-align:center;">Deepak Chothe</h1>',unsafe_allow_html=True)
  st.markdown('<h5 style="text-align:center;">Data Analyst</h5>',unsafe_allow_html=True)

   
  summ = '<p style="background-color: #16A2CB ;text-align:center ;font-size:32px" > Summary </p>'
  st.markdown(summ, unsafe_allow_html=True)


  st.info('''
  - To work in an organization that provides me with ample opportunities to enhance my skills and knowledge along with contributing to the growth of the organization
  - Strong statistical skill 
  ''')

#####################
# Education
if selected == "Education":
  left_col , right_col =st.columns([1.5,3])
  with right_col:
   summ = '<p style="background-color: #16A2CB ;text-align:center ;font-size:32px" > Education </p>'
   st.markdown(summ, unsafe_allow_html=True)
  with left_col:
    st_lottie(
    lottie_edu,
    speed=1,
    reverse=False,
    loop=True,
    quality="high", # medium ; high
     # canvas
    height=70,
    width=None,
    key=None,
   )
  txt('**POST- GRADUATION** (Statistics)','2019 – 2021')
  txt('*Jilha Maratha Vidya Prasarak Samaj New Arts Commerce Science College *', 'Ahmednagar Maharashtra')
  st.markdoewn('''
  - Completed post-graduation in Statistics with 8.1 CGPA
  ''')
  txt('**GRADUATION** (Statistics)','2016 – 2019')
  txt('*Jilha Maratha Vidya Prasarak Samaj New Arts Commerce Science College *', 'Ahmednagar Maharashtra')
  st.markdown('''
  - Completed graduation in Statistics with 81.75 %
  ''')
  txt('**H.S.C** (Statistics)','2014 – 2016')
  txt('*Loknete Ramdas Patil Dhumal Arts Science & Commerce College Rahuri*', 'Rahuri Ahmednagar Maharashtra')
  
  st.markdown('''
  - 67.54%

  ''')

#####################
# Work Experience

if selected == "Work Experience":
  summ = '<p style="background-color: #16A2CB ;text-align:center ;font-size:32px" > Work Experience </p>'
  st.markdown(summ, unsafe_allow_html=True)
  txt('**Subject Matter Expert (Statistics)**, UpThink Experts, Pune Maharashtra',
  'Sep-2021 -- April-2022')
  left_col , right_col =st.columns([1.5,3])
  with right_col:
    st_lottie(
    lottie_work1,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
     # canvas
    height=300,
    width=None,
    key=None,
   )
  with left_col:

    st.markdown('''
    - Working with students to help them understand key concepts, especially those learned in the classroom.
    - Contributes to student learning, growth, and advancement.
    - Technology used Excel , Ti - 84/83 (scientific calculator) ,  Stat-Crunch 
    ''')
  txt('**Senior Data Analyst**, Capgemini, Pune Maharashtra',
  'April 2022  to Present')
  left_col , right_col =st.columns([1.5,3])
  with right_col:
    st_lottie(
    lottie_work2,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
     # canvas
    height=200,
    width=None,
    key=None,
   )
  with left_col:
    st.markdown('''
  - Analyzing data using statistical techniques and providing reports.
  - Identifying, analyzing, and interpreting trends or patterns in complex data sets.
  - Filtering and cleaning data
  ''')
  
    
  
  

#####################
#Projects
if selected == "Projects":

  summ = '<p style="background-color: #16A2CB ;text-align:center ;font-size:32px" > Projects </p>'
  st.markdown(summ, unsafe_allow_html=True)
  txt('**Systematic Study of Effect of PUBG Game**',' ')
  left_col , right_col =st.columns([1.5,3])
  with left_col:
    st.markdown('''
    Comparison of Aggression, Addiction, and Extraversion in
    PUBG playing person and non PUBG playing
    person. 
    Using various Statistical technique
    - Z test
    - Chi-square test
    ''')
  with right_col:
    st_lottie(
    lottie_project1,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
     # canvas
    height=200,
    width=None,
    key=None,
   )
  txt('**Flower image classification using CNN**',' ')
  left_col , right_col =st.columns([1.5,3])
  with left_col:
    st.markdown('''
  Classification of flowers image into relevant classes.
  - Model accuracy on train set is 85%
  - Model accuracy on test set is 80%
  ''')
  with right_col:
    st_lottie(
    lottie_project2,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
     # canvas
    height=200,
    width=None,
    key=None,
   )
  
  txt('**Prediction for Credit Card**',' ')
  left_col , right_col =st.columns([1.5,3])
  with left_col:
    st.markdown('''
  Prediction of credit card using various features
  - Algorithm use
  - Knn
  - Support vector machines
  - Random forest
  - ANN
  ''')
  with right_col:
    st_lottie(
    lottie_project3,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
     # canvas
    height=200,
    width=None,
    key=None,
   )
  


#####################
#Skills
if selected == "Skills":
  summ = '<p style="background-color: #16A2CB ;text-align:center ;font-size:32px" > Skills </p>'
  st.markdown(summ, unsafe_allow_html=True)
  txt3('Programming', '`Python`, `R`')
  txt3('Data processing/wrangling','`Pandas`, `Numpy`')
  txt3('Data visualization', '`Matplotlib`, `Seaborn`, `Plotly`')
  txt3('Machine Learning', '`Scikit-learn`')
  txt3('Deep Learning', '`TensorFlow`')


#####################
#Social Media
if selected == "Social Media":
  summ = '<p style="background-color: #16A2CB ;text-align:center ;font-size:32px" > Social Media </p>'
  st.markdown(summ, unsafe_allow_html=True)
  txt2('LinkedIn', 'https://www.linkedin.com/in/deepak-chothe-46738b193/')
  txt2('Twitter', 'https://twitter.com/DEEPAKCHOTHE1')
  txt2('GitHub', 'https://github.com/DeepakChothe')