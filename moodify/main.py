# App entrypoint (where recording, mood selection, and generation flow happens)

from moodify.record.recorder import record_audio
from moodify.mood.mood_selector import get_user_mood
from moodify.analysis.feature_extraction import extract_features
from moodify.generation.music_generator import generate_music
from moodify.output.player import play_music
import moodify.config as config

def main():
    audio_file = record_audio(config.INPUT_AUDIO_PATH)
    mood = get_user_mood(config.ALLOWED_MOODS)
    features = extract_features(audio_file)
    soundtrack = generate_music(features, mood)
    play_music(soundtrack)

if __name__ == "__main__":
    main()