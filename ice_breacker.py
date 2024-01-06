from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from agents.linkedin_agent import lookup
from thirdparty.linkedin import Scrape_linkdin_profile
from output_parsers import person_intel_perser ,PersonalIntel
def ice_brack(name:str)->tuple[PersonalIntel,str]:
    linkedin_profile_url = lookup(name=name)
    linkedin_data = Scrape_linkdin_profile(linkedin_profile_url=linkedin_profile_url)


    summary_template = """
         given the Linkedin information {information} about a person from I want you to create:
         1. a short summary
         2. two interesting facts about them
         3. a topic that may instrest them 
         4. creative ice breckers to open a conversation with them 
         \n{formal_instructions}    
     """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template , 
        partial_variables= {'formal_instructions': person_intel_perser.get_format_instructions()},
                                                                                         
    )   

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    result =chain.run(information=linkedin_data)
    print(result)
    return person_intel_perser.parse(result) , linkedin_data.get('profile_pic_url')
    # return person_intel_perser.parse(result) 
    
if __name__ == "__main__":
    print("Hello LangChain!")
    # linkedin_profile_url='https://gist.githubusercontent.com/pratikshinde115/fd06e5b347f1a630f78902453810d5f5/raw/497316b6b745149c4a6d481d594fb922c57d6651/gistfile1.txt'

    print("Hello LangChain!")
    result = ice_brack(name="Harrison Chase")
    print(result)