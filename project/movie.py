import moviepy.editor

def convert(videoFilename, outfilename="extractedaudio.mp3"):
    video = moviepy.editor.VideoFileClip(videoFilename)
    audio = video.audio
    audio.write_audiofile(outfilename)