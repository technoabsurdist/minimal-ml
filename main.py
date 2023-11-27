import argparse
from detect_language import detect
from text_to_speech import convert_text_to_speech
from translate_and_talk import translate_and_talk
from translation import detect_and_translate, translate
import interfaces
from yb import yb_download, yb_transcript

def main():
    parser = argparse.ArgumentParser(description="Language processing and YouTube utilities CLI")

    # Subparsers for each functionality
    subparsers = parser.add_subparsers(dest='command')

    # Transcription
    transcription_parser = subparsers.add_parser('transcription', help='Transcribe YouTube video')
    transcription_parser.add_argument('url', type=str, help='URL of the YouTube video')

    # Translation
    translation_parser = subparsers.add_parser('translation', help='Translate text from one language to another')
    translation_parser.add_argument('text', type=str, help='Text to translate')
    translation_parser.add_argument('source', type=str, help='Source language')
    translation_parser.add_argument('target', type=str, help='Target language')

    # Detect Language
    detect_language_parser = subparsers.add_parser('detect_language', help='Detect language of the given text')
    detect_language_parser.add_argument('text', type=str, help='Text to detect language')

    # Detect and Translate
    detect_and_translate_parser = subparsers.add_parser('detect_and_translate', help='Detect language and translate text')
    detect_and_translate_parser.add_argument('text', type=str, help='Text to detect and translate')
    detect_and_translate_parser.add_argument('target', type=str, help='Target language for translation')

    # Text to Speech
    text_to_speech_parser = subparsers.add_parser('text_to_speech', help='Convert text to speech')
    text_to_speech_parser.add_argument('text', type=str, help='Text to convert to speech')

    # Translate and Talk
    translate_and_talk_parser = subparsers.add_parser('translate_and_talk', help='Translate text and convert to speech')
    translate_and_talk_parser.add_argument('text', type=str, help='Text to translate and convert to speech')
    translate_and_talk_parser.add_argument('target', type=str, help='Target language for translation')

    # YouTube Download MP4
    youtube_download_mp4_parser = subparsers.add_parser('youtube_download_mp4', help='Download YouTube video as MP4')
    youtube_download_mp4_parser.add_argument('url', type=str, help='URL of the YouTube video to download')

    args = parser.parse_args()

    if args.command == 'transcription':
        result = yb_transcript(args.url)
        print(result)
    elif args.command == 'translation':
        result = translate(args.text, args.source, args.target)
        print(result)
    elif args.command == 'detect_language':
        result = detect(args.text)
        print(result)
    elif args.command == 'detect_and_translate':
        result = detect_and_translate(args.text, args.target)
        print(result)
    elif args.command == 'text_to_speech':
        result = convert_text_to_speech(args.text)
        print(result)
    elif args.command == 'translate_and_talk':
        result = translate_and_talk(args.text, args.target)
        print(result)
    elif args.command == 'youtube_download_mp4':
        result = yb_download(args.url)
        print(result)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
