# Analyze user input audio
# Use OpenSMILE to extract audio features

import subprocess

def extract_features(audio_path):
    # Call OpenSMILE to extract features
    # Assumes OpenSMILE is installed and accessible
    output_path = "data/features/audio_features.csv"
    subprocess.run([
        "SMILExtract", "-C", "config/emobase.conf",
        "-I", audio_path,
        "-O", output_path
    ])
    print(f"Features extracted to {output_path}")
    return output_path