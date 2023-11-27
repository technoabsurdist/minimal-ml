from langchain.document_loaders import YoutubeLoader
import sieve
import shutil

def yb_transcript(url: str):
    loader = YoutubeLoader.from_youtube_url(url, add_video_info=False)
    result = loader.load()
    tables = [doc for doc in result]
    return [table.page_content for table in tables]

def yb_download(url: str):
    youtube_to_mp4 = sieve.function.get("sieve/youtube_to_mp4")
    output = youtube_to_mp4.run(url, True)
    destination_path = "downloads/yb_download.mp4"
    shutil.copy(output.path, destination_path)
