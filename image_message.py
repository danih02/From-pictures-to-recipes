import base64
from typing import List
from langchain_core.messages import HumanMessage

# function to wrap llm input
def image_message(query: str, image : bytes) -> List[HumanMessage]:

    pic_encoded = base64.b64encode(image).decode("utf-8")

    multimodal_content = [
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{pic_encoded}"
            }
        },
        {
            "type": "text",
            "text": query
        }
    ]

    return [HumanMessage(content=multimodal_content)]