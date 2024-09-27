import requests
import streamlit  as st
from audiorecorder import audiorecorder
from random import randrange

from scripts import upload_to_blob

def convert_speech_text(audio_file_path,lang_id):
    API_URL = "https://asrcapapiservice.ambitiousflower-67f41ae4.southeastasia.azurecontainerapps.io/api/audio-file"
    multipart_form_data = {
    'audio_file_path': audio_file_path,
    'lang_id': lang_id
}
 
    response = requests.post(API_URL,  json=multipart_form_data)
    data = response.json()
    return data['out-put-string']

def main():
    size=0
    result=''
    # Commenting for now
    st.set_page_config(page_title="STW Bot...",
                   page_icon="🧬",
                   initial_sidebar_state="expanded")
    
   
    st.title("ASR for English -  :blue[cool] :sunglasses:")
    with st.sidebar.expander("", expanded=True):
        choice = st.radio(
                        label='Available Options',
                        options=[
                            '⏺️ - Record',
                            '📁 - Upload'
                        ],
                        index=None
                    )
        if choice =='⏺️ - Record':
            result=''
            st.subheader("- make notes by recording - ",divider=True)
            audio = audiorecorder("Click to record", "Click to stop recording",)
            
            bytes_to_load=audio.export().read()
            st.audio(bytes_to_load) 
            size=len(audio)

            
        elif choice == '📁 - Upload':
             with st.sidebar.expander("", expanded=True):
 
                uploaded_files = st.file_uploader("Choose a .WAV file", type=["wav","mp3"],accept_multiple_files=True)
                if uploaded_files is not None:
                    bytes_to_load=get_bytes_from_wav_upload(uploaded_files)
                    size =len(bytes_to_load)

    if choice =='⏺️ - Record':
        st.write(f"Duration: {audio.duration_seconds} seconds")

    

    with st.sidebar.expander("", expanded=True):
            lang_id='en-I'
            # lang_sel = st.radio(
            #     "Set text input label visibility 👉",
            #     ["English"],
            # ) 
            if size > 0:    
                    lang_id =""
                    # if lang_sel == 'English':
                    #     lang_id = 'en-IN'

                    rand_audio_number = randrange(100000) 
                    temp_name_value=None

                    if choice =='📁 - Upload':
                        for i in range(len(bytes_to_load)):
                            st.audio(bytes_to_load[i]) 
                            temp_name_value = 'upload_'+str(1980)+'_'+str(i)
                            upload_to_blob.upload_wav_file_content_to_Blob(str(rand_audio_number)+'_'+str(temp_name_value), bytes_to_load[i])
                            result = result+ convert_speech_text(str(rand_audio_number)+'_'+temp_name_value,lang_id)+'\n'
                              
                        
                    elif choice =='⏺️ - Record':
                        temp_name_value=str(audio.duration_seconds)

                        upload_to_blob.upload_wav_file_content_to_Blob(str(rand_audio_number)+'_'+str(temp_name_value), bytes_to_load)

                        result = convert_speech_text(str(rand_audio_number)+'_'+temp_name_value,lang_id)
    
    with st.expander("✍️ :Audio transcription of the audio data: ", expanded=True):
                            text = st.text_area("  ", result, height=500) 

def get_bytes_from_wav_upload(uploaded_files):
    bytes_data=[]
    for uploaded_file in uploaded_files:
        if uploaded_file is not None:
            bytes_data.append(uploaded_file.read())
    return bytes_data    
if __name__ == '__main__':
    main()
