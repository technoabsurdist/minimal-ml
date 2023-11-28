import sieve


def enhance_audio(audio_url, speed_boost, steps):
    audio = sieve.Audio(url=audio_url)
    audio_enhancement = sieve.function.get("sieve/audio_enhancement")
    return audio_enhancement.run(
        audio, 
        "all", 
        speed_boost, 
        steps 
    )