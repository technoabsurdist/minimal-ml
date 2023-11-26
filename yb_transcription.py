from langchain.document_loaders import YoutubeLoader

def yb_transcript(url):
    try:
        loader = YoutubeLoader.from_youtube_url(url, add_video_info=False)
        result = loader.load()
        tables = [doc for doc in result]
        return [table.page_content for table in tables]
    except:
        print("Error in Youtube Transcription. Try again later.")
