from dotenv import load_dotenv
from imagekitio import ImageKit
import os

load_dotenv()

imagekit = ImageKit(
    private_key=os.environ.get("IMAGEKIT_PRIVATE_KEY")
)

# Store URL endpoint for reuse
URL_ENDPOINT = os.environ.get("IMAGEKIT_URL")
