import os
import requests

"""
All requests to the LLM require some form of a key.
Other sensitive data has also been hidden through environment variables.
"""
api_key = os.environ['OPENAI_API_KEY']
base_url = os.environ['OPENAI_API_BASE']
deployment = os.environ['OPENAI_API_DEPLOYMENT']
version = os.environ['OPENAI_API_VERSION']
"""
An AI is capable of quickly recognizing patterns based off of a few examples. Let's 
instruct our AI to produce a formatted response, where the input format 
is ____, ____ and output format is 'the ____ is ____' . For instance, we may teach the 
LLM to respond in a certain format with examples such as
input: red, car
output: the car is red
This is known as 'few shot' prompting. 'Few shot' prompting is a trick to obtain
more accurate results according to any pattern. In the real world, an AI may use this
pattern to semantically understand some text and extract or classify data using this
pattern.
"""

"""
TODO: Change the prompt below to allow for the generation of output as described above.
You should provide the LLM with a few examples so that the output is correctly 
formatted.
"""
prompt = ""

"""
There is no need to change the below function. It will properly use the prompt &
user input as needed.
"""


def llm(user_input):
    res = requests.post(f"{base_url}/deployments/{deployment}/chat/completions?api-version={version}",
                        headers={
                            "Content-Type": "application/json",
                            "api-key": f"{api_key}"
                        },
                        json={
                            "messages": [
                                {"role": "system",
                                 "content": f"{prompt}"},
                                {"role": "user",
                                 "content": f"{user_input}"}],
                        })
    message = str(res.json().get("choices")[0].get("message").get("content"))
    return message
