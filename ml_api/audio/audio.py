import sieve

def enhance_audio(audio_url, speed_boost, steps):
    """
    Enhances an audio file by reducing background noise and adjusting quality.

    This function takes a URL pointing to an audio file, applies audio enhancement techniques using the 'sieve' library, 
    and returns the enhanced audio. The enhancement includes noise reduction and quality adjustments based on specified parameters.

    Parameters:
    - audio_url (str): The URL of the audio file to be enhanced.
    - speed_boost (bool): A flag to determine if the enhancement process should be sped up.
    - steps (int): The number of steps to use in the enhancement process, determining the level of enhancement.

    Returns:
    - Enhanced audio object as returned by the 'sieve/audio_enhancement' function.
    """
    audio = sieve.Audio(url=audio_url)
    audio_enhancement = sieve.function.get("sieve/audio_enhancement")
    return audio_enhancement.run(audio, "all", speed_boost, steps)