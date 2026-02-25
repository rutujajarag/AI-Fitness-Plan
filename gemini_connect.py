
from click import prompt
from google import genai

client = genai.Client(api_key="AIzaSyCBfqP1i--RV4cz5s18QAYHAAN2Qe2fA28")


def create_prompt(fitness_goal,workout_per_week,minutes_per_day,diet_preference):
    prompt= f"Generate a fitness plan for me to {fitness_goal},where I can workout for {workout_per_week} times a weak and I have {minutes_per_day} and give me strict  diet plane {diet_preference}. Mandatorily return the response in HTML format only,and the tags to be placed within body tag only"
    return prompt


def get_response(prompt):
    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=prompt   # ← removed quotes
    )
    return response.text


# You must create the prompt first
prompt = create_prompt("lose weight",4,45,"vegetarian")

response=get_response(prompt)
print(response)