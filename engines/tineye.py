from bs4 import BeautifulSoup

from . import ReverseImageSearchEngine

__all__ = ['TinEyeReverseImageSearchEngine']

class TinEyeReverseImageSearchEngine(ReverseImageSearchEngine):

    def __init__(self):
        super(TinEyeReverseImageSearchEngine, self).__init__(
            url_base='https://tineye.com',
            url_path='/search?url={image_url}',
            url_path_upload='',
            name='TinEye'
        )
