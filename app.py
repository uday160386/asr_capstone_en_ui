import requests
import os
import streamlit  as st
from audiorecorder import audiorecorder
from random import randrange

TEMP_AUDIO_FILES =  "/Users/udaykumar/Documents/workspace/asr_capstone_en_ui/test_audio_files/tmp"


def convert_speech_text(audio_file_path,lang_id):
    API_URL = "http://localhost:8000/api/audio-file"
    multipart_form_data = {
    'audio_file_path': (None, audio_file_path),
    'lang_id': (None, lang_id)
}
 
    response = requests.post(API_URL,  files=multipart_form_data)
    data = response.json()
    return data['out-put-string']

def main():
   
    # Commenting for now
    st.set_page_config(page_title="Speech Recognizer...",
                   page_icon="🧬",
                   initial_sidebar_state="expanded")
    st.header("STT Bot")
    st.subheader("Make notes by recording")

    col1, col2, col3 = st.columns(3)

    with col1:
        audio = audiorecorder("Click to record", "Click to stop recording")
        rand_audio_number = randrange(100000)
        st.audio(audio.export().read()) 

        lang_sel = st.radio(
            "Set text input label visibility 👉",
            ["English", "Telugu", "Hindi"],
        )

    with col2:
        if len(audio) > 0:
         
        
            audio.export(TEMP_AUDIO_FILES+'/'+str(rand_audio_number)+'_'+str(audio.duration_seconds)+'_audio.wav', format='wav')
            
            st.write(f"Frame rate: {audio.frame_rate}, Frame width: {audio.frame_width}, Duration: {audio.duration_seconds} seconds")
            lang_id =""
            if lang_sel == 'English':
                lang_id = 'en-IN'
            elif lang_sel == 'Telugu':
                lang_id = 'te-IN'
            elif lang_sel == 'Hindi':
                lang_id = 'hi-IN'
          
            result = convert_speech_text(TEMP_AUDIO_FILES+'/'+str(rand_audio_number)+'_'+str(audio.duration_seconds)+'_audio.wav',lang_id)
            text = st.text_area("Audio Transcription:  ", result) 

if __name__ == '__main__':
    main()