import os
import moviepy.editor as mp

input_path = "/home/user/project/trevor-daniel-falling_189856.mp4"

if input_path:
    # Extract the file name and extension
    file_name, ext = os.path.splitext(input_path)

    # The output audio file path
    output_path = f"{file_name}.mp3"

    # Convert the video to audio using MoviePy
    video = mp.VideoFileClip(input_path)
    audio = video.audio
    audio.write_audiofile(output_path)

    print(f"Audio file saved to {output_path}")
else:
    print("***No input file***")



import nltk
nltk.download('punkt')
import whisper
from tkinter import Tk
from tkinter.filedialog import askopenfilename

model=whisper.load_model('base')

# Show a file dialog to select an audio file
Tk().withdraw()
filename = askopenfilename()

# Transcribe the audio file
result = model.transcribe(filename, fp16=False)

# Split the transcribed text into sentences based on both full stops and commas
sentences = '\n'.join(result['text'].replace('.', '\n').replace(',', '\n').split('\n'))

# Write each sentence to a new line in a text file
with open("Output.txt", "w") as f:
    f.write(sentences)