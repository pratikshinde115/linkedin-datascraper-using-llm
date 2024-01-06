import os
import requests

def Scrape_linkdin_profile(linkedin_profile_url:str):
    """
    used to scrap information linkdin profile
    """
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    hedder_dict = {"Authorization":f'Bearer{os.environ.get("PROXYCURL_API_KEY")}'}



    response = requests.get(
        api_endpoint,params={'url':linkedin_profile_url},headers=hedder_dict
    )
    # response = requests.get(f'{linkedin_profile_url}')


    data = response.json()
    data = {
        k:v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k not in ['pelple_also_viewed','certifications']
        

    }
    if data.get('groups'):
        for group_dict in data.get('groups'):
            group_dict.pop('profile_pic_url')

  

    return data