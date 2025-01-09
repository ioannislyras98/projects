import yt_dlp
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def list_formats(url):
    try:
        logging.debug(f"Listing formats for URL: {url}")
        
        # Define options to list formats
        ydl_opts = {
            'listformats': True,
        }
        
        # List formats
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=False)
        
        logging.info("Listed formats successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

def download_youtube_video(url, output_path):
    try:
        logging.debug(f"Attempting to download video from URL: {url}")
        
        # Define download options
        ydl_opts = {
            'format': '136',# 'bestvideo+bestaudio/best' change it with the best id from listformats
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',  # Ensure the output is in MP4 format
        }
        
        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        logging.info("Download completed.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=4ty9C9pNuwM&list=PL2fVdBh-ziSzIcrdb7vdb3tlSHC2u51Ub&index=4"
    output_path = "C:/Users/glyras/Downloads"
    
    # List available formats
    list_formats(youtube_url)
    
    # Download the video
    download_youtube_video(youtube_url, output_path)