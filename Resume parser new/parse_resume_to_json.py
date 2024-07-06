import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'your-api-key'

def parse_resume_to_json(resume_content):
    prompt = f"""
    You are an expert in parsing text into structured data. I have a resume that I need to convert into JSON format. Please take the following resume content as input and parse it into a structured JSON format, with sections for summary, education, internships, projects, assessments/certifications, seminars/trainings/workshops, co-curricular activities, extra-curricular activities, and personal interests/hobbies.

    Resume Content:
    \"\"\"{resume_content}\"\"\"

    Expected JSON Format:
    {{
      "summary": "...",
      "education": [
        {{
          "institution": "...",
          "degree": "...",
          "start_date": "...",
          "end_date": "...",
          "details": "..."
        }},
        ...
      ],
      "internships": [
        {{
          "company": "...",
          "role": "...",
          "start_date": "...",
          "end_date": "...",
          "details": "..."
        }},
        ...
      ],
      "projects": [
        {{
          "title": "...",
          "description": "...",
          "technologies": "...",
          "link": "..."
        }},
        ...
      ],
      "assessments_certifications": [
        {{
          "title": "...",
          "organization": "...",
          "date": "..."
        }},
        ...
      ],
      "seminars_trainings_workshops": [
        {{
          "title": "...",
          "organization": "...",
          "date": "..."
        }},
        ...
      ],
      "co_curricular_activities": [
        {{
          "activity": "...",
          "role": "...",
          "date": "..."
        }},
        ...
      ],
      "extra_curricular_activities": [
        {{
          "activity": "...",
          "role": "...",
          "date": "..."
        }},
        ...
      ],
      "personal_interests_hobbies": [
        {{
          "interest": "..."
        }},
        ...
      ]
    }}
    """

    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=1500
    )

    return response.choices[0].text.strip()

# Example usage
resume_content = """
[Your Resume Content Here]
"""

parsed_json = parse_resume_to_json(resume_content)
print(parsed_json)
