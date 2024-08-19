import sys, os

import speech_recognition as sr

r = sr.Recognizer()

mod_root = "test_audio_files/"
TRAIN_DATA_HOME = mod_root+"wav/"
out_file_path="result_out.txt"

def calling_asr(wav_file,lid):
    AUDIO_FILE=wav_file
    text="cant read wav file"
    try:
        with sr.AudioFile(AUDIO_FILE) as source:
            audio = r.record(source)
        text = r.recognize_google(audio, language=lid)
        #file.write(aud_name +"\t"+text)
        return text
    except:
        #file.write(" "+"Error in segement"+" ")
        return text
    #file.close()

if __name__ == "__main__":
    for path, subdirs, files in os.walk(TRAIN_DATA_HOME):
        for name in files:
            split_filename=name.split(".wav")
            get_sub_dir=split_filename[0].split('-')
            asr_out=calling_asr("{}".format(TRAIN_DATA_HOME+'/'+get_sub_dir[0]+'/'+get_sub_dir[1]+'/'+split_filename[0]+'.wav'),"en_ID")
            with open(out_file_path, 'a') as file:
                    file.write("{}\n".format(asr_out))
    print('Convered voice to text sucussfully.')