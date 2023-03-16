import streamlit as st
import requests
import json

# Set the page title and favicon
st.set_page_config(page_title="Waves of The Heart", page_icon=":heartbeat:")

st.markdown(
        f"""
        <div style='text-align: center;'>
            <h1 style='font-family: Yasashii Bold; color: red;'>Waves of The Heart</h1>
            <p>Automated Heart Sound Classification Tool</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


#st.image("/home/mer/Pictures/Screenshots/Screenshot from 2023-02-24 16-21-01.png", use_column_width=True, output_format="PNG")
video_file = open('Waves_homepage_header.mp4', 'rb')
video_bytes = video_file.read()
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
st.write('<div style="display: flex; justify-content: center;">', unsafe_allow_html=True)
st.video(data=video_bytes, format='video/mp4')
st.write('</div>', unsafe_allow_html=True)

audio = st.file_uploader('Upload audio file', type=['wav'])

# if audio is not None:
#     st.write('Classifying...')

if audio is not None:
    # st.success('Classifying...')

    url = 'https://waves-bvnb2v37aa-ew.a.run.app/'
    response = requests.post(f'{url}/upload_wav_file',files = {'file':audio.getbuffer()})
    prediction_response = requests.get(f'{url}/predict')
    predictionstring = str(prediction_response.text)
    #prediction = json.loads(response.content.decode('utf-8'))['Prediction']
    # prediction = int(prediction_response.content['prediction'])
    if predictionstring == '{"Prediction":-1}':
        st.success("Your heart sound is normal! Keep up the good work in taking care of your health!")
    else:
        st.success("Your heart sound is abnormal! We recommend you to see a doctor for further investigation. Don't worry, early detection leads to better outcomes!")
    # else:
    #     st.write("Something went wrong with the prediction. Please try again.")

st.markdown(
    f"""
    <div>
        <h2 style='font-family: Yasashii Bold; color: black;'>About Waves of The Heart</h2>
        <p style='font-family: Yasashii Bold;'>
        Waves of The Heart is a project that uses machine learning to classify heart sounds as normal or abnormal. The project is aimed at improving the diagnosis of heart disease, which affects millions of people worldwide.
        </p>
        <p style='font-family: Yasashii Bold;'>
        The human heart produces two distinct sounds, known as S1 and S2, which can be heard using a stethoscope. Abnormal heart sounds, or murmurs, can indicate a variety of heart conditions, including valve problems, heart failure, and congenital heart defects.
        </p>
        <p style='font-family: Yasashii Bold;'>
        The Waves of The Heart project uses a machine learning model trained on a dataset of heart sound recordings to automatically classify heart sounds as normal or abnormal.
        </p>
        <p style='font-family: Yasashii Bold;'>
        By accurately classifying heart sounds as normal or abnormal, the Waves of The Heart project has the potential to improve the accuracy and speed of heart disease diagnosis. This could lead to earlier detection and treatment of heart conditions, and ultimately improve the outcomes for patients with heart disease.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
