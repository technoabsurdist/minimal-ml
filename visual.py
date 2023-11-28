import sieve

def visual_question_answering(image_url: str, prompt: str):
    image = sieve.Image(url=image_url)
    top_p = 1
    temperature = 0.2
    max_tokens = 1024
    llava_vl_13b = sieve.function.get("sieve/llava-vl-13b")
    return llava_vl_13b.run(image, prompt, top_p, temperature, max_tokens)