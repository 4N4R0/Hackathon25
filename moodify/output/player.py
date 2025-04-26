# Play and save outputs
# Play generated track

import simpleaudio as sa

def play_music(file_path):
    print(f"Playing {file_path}...")
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()