import requests
from urllib.parse import quote


api_url = "https://nandha-api.onrender.com/"

class Nandha:
    
    def __init__(self) -> None:
        nandha = """
        Python API tool:
        \nSupport Group: NandhaSupport.t.me\n
        Support Channel: NandhaBots.t.me
        """    
        return print(nandha)

    
    
    @staticmethod
    def ai(model: str, query: str):
        example = (
        "from NandhaAPI import ai\n"
        "print(ai('gpt', 'hello'))"
        )

        avb = ['gpt', 'palm', 'bard']
        if not model in avb:
            return example
        prompt = quote(query)
        end_point = f'ai/{model}/{prompt}'
        nandha = requests.get(api_url + end_point).json()
        return nandha

    @staticmethod
    def imagine(query: str):
        prompt = quote(query)
        end_point = f"imagine?prompt={prompt}"
        nandha = requests.get(api_url + end_point).json()
        return nandha

    @staticmethod
    def stylefont(text: str):
        prompt = quote(text)
        end_point = f"styletext?query={prompt}"
        nandha = requests.get(api_url + end_point).json()
        return nandha
    
    @staticmethod
    def run_code(code: str, lang: str):
        end_point = f"run?code={quote(code)}&language={lang}"
        nandha = requests.get(api_url + end_point).json()
        return nandha
    
    @staticmethod
    def zerochan(query: str):
        prompt = quote(query)   
        end_point = f"zerochan?name={prompt}"
        nandha = requests.get(api_url + end_point).json()
        return nandha

    @staticmethod
    def couples():
        end_point = "couples"
        #https://nandha-api.onrender.com/couples
        nandha = requests.get(api_url + end_point).json()
        return nandha
        
    @staticmethod
    def ud(query: str, limit: int = 5):
         query = quote(query)
         end_point = f'ud?query={query}&max={limit}'
         nandha = requests.get(api_url + end_point).json()
         return nandha

    @staticmethod
    def anime_quote():
        end_point = "animequote"
        nandha = requests.get(api_url + end_point).json()
        return nandha

    @staticmethod
    def sof(query: str):
        prompt = quote(query)
        end_point = f"stackoverflow?query={prompt}"
        nandha = requests.get(api_url + end_point).json()
        return nandha
    
    @staticmethod
    def pit_video(url: str):
        end_point = f"vidpinterest?pinterest_url={url}"
        nandha = requests.get(api_url + end_point).json()
        return nandha
           
    @staticmethod
    def pit_images(query: str):
        prompt = quote(query)
        end_point = f"pinterest?query={prompt}"
        nandha = requests.get(api_url + end_point).json()
        return nandha  

    @staticmethod
    def reverse(url: str):
        end_point = f"reverse?img_url={url}"
        nandha = requests.post(api_url + end_point).json()
        return nandha    
