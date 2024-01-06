from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel , Field
from typing import List

class PersonalIntel(BaseModel):
    summary:str = Field(description="summary of th person")
    facts:List[str] = Field(description="instresting facts about the person")
    topic_of_instret:List[str] = Field(description="Topics that may instrest the person")
    ice_brackers:List[str] = Field(description="create ice bracker to open a conversion with the person")



    def to_dict(self):
        return {'summary':self.summary,
                 'facts':self.facts,
                 'topic_of_instret':self.topic_of_instret,
                 'ice_brackers':self.ice_brackers
                 }
        
person_intel_perser:PydanticOutputParser  = PydanticOutputParser(pydantic_object=PersonalIntel)     