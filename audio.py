import sieve


def enhance_audio(audio_url, speed_bost, steps):
    audio = sieve.Audio(url=audio_url)
    filter_type = "all"
    enhance_speed_boost = speed_bost 
    enhancement_steps = steps

    audio_enhancement = sieve.function.get("sieve/audio_enhancement")
    output = audio_enhancement.run(audio, filter_type, enhance_speed_boost, enhancement_steps)
    return output