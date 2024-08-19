
from pathlib import PurePath
from pydub import AudioSegment
from scipy.io.wavfile import read, write
import io
import wave
from  scipy.io import wavfile 



import wave
# Open a WAV file for reading.
with wave.open("/Users/udaykumar/Documents/workspace/asr_capstone_en/test_audio_files/wav/61/70968/61-70968-0000.wav", 'rb') as wav_file:
    # Read audio frames and get parameters.
    audio_frames = wav_file.readframes(wav_file.getnframes())
    params = wav_file.getparams()
    print(audio_frames)
# Open a new WAV file for writing and set parameters.

with wave.open("/Users/udaykumar/Documents/workspace/asr_capstone_en/test_audio_files/tmp/61-70968-0000.wav", 'wb') as wav_file:
    wav_file.setparams(params)
    # Write audio frames to the new WAV file.
    wav_file.writeframes(audio_frames)


# with wave.open("/Users/udaykumar/Documents/workspace/asr_capstone_en/test_audio_files/wav/61/70968/61-70968-0000.wav", 'rb') as wav_file: 
#     print(wav_file.getnframes().)
#     # for i in range(wav_file.getnframes()):
#     #     frame = wav_file.readframes(i)
#     #     print(frame)
    
# with open("/Users/udaykumar/Documents/workspace/asr_capstone_en/test_audio_files/wav/61/70968/61-70968-0000.wav", 'rb') as audio_file, \
#      open("/Users/udaykumar/Documents/workspace/asr_capstone_en/test_audio_files/tmp/61-70968-0000.txt", 'wb') as write_text:
#         decoded_string = audio_file.read()
#         print(decoded_string)
#         write_text.write(decoded_string)

