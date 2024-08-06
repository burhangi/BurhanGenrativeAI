import streamlit as st
import openai

def display_openai_models():
    st.sidebar.title('OpenAI API Key')

    # Check if the API key is already in session state
    if "api_key" not in st.session_state or not st.session_state.api_key:
        # If API key is not set, show input for API key
        api_key = st.sidebar.text_input("Enter your OpenAI API key:", type="password")
        if st.sidebar.button("Submit"):
            st.session_state.api_key = api_key
            # Optionally, validate API key here
    else:
        # Set the OpenAI API key
        openai.api_key = st.session_state.api_key

        # Define model functions (unchanged)
        def text_summarization(text):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Summarize the text."},
                    {"role": "user", "content": f"Summarize this text: {text}"}
                ]
            )
            return response.choices[0].message['content']

        def grammar_correction(text):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Correct the grammar of the text."},
                    {"role": "user", "content": f"Correct the grammar of this text: {text}"}
                ]
            )
            return response.choices[0].message['content']

        def simplify_text(text):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Simplify the text for a second grader."},
                    {"role": "user", "content": f"Simplify this text: {text}"}
                ]
            )
            return response.choices[0].message['content']

        def parse_unstructured_data(text):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Parse the unstructured data into a table."},
                    {"role": "user", "content": f"Parse this data: {text}"}
                ]
            )
            return response.choices[0].message['content']

        def emoji_translation(text):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Translate the text into emoji."},
                    {"role": "user", "content": f"Translate this text to emoji: {text}"}
                ]
            )
            return response.choices[0].message['content']

        def calculate_time_complexity(code):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Calculate the time complexity of the code."},
                    {"role": "user", "content": f"Calculate the time complexity of this code: {code}"}
                ]
            )
            return response.choices[0].message['content']

        def explain_code(code):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Explain the code."},
                    {"role": "user", "content": f"Explain this code: {code}"}
                ]
            )
            return response.choices[0].message['content']

        def extract_keywords(text):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Extract keywords from the text."},
                    {"role": "user", "content": f"Extract keywords from this text: {text}"}
                ]
            )
            return response.choices[0].message['content']

        def generate_product_name(description, seed_words):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Generate product names."},
                    {"role": "user", "content": f"Generate product names from this description: {description} with seed words: {seed_words}"}
                ]
            )
            return response.choices[0].message['content']

        def fix_python_bug(code):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Fix the Python bug in the code."},
                    {"role": "user", "content": f"Fix the bug in this code: {code}"}
                ]
            )
            return response.choices[0].message['content']

        def create_spreadsheet(data):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Create a spreadsheet from the data."},
                    {"role": "user", "content": f"Create a spreadsheet from this data: {data}"}
                ]
            )
            return response.choices[0].message['content']

        def classify_tweet(tweet):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Classify the sentiment of the tweet."},
                    {"role": "user", "content": f"Classify the sentiment of this tweet: {tweet}"}
                ]
            )
            return response.choices[0].message['content']

        def extract_airport_code(text):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Extract airport codes from the text."},
                    {"role": "user", "content": f"Extract airport codes from this text: {text}"}
                ]
            )
            return response.choices[0].message['content']

        def mood_to_color(mood):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Translate the mood to a color."},
                    {"role": "user", "content": f"Translate this mood to a color: {mood}"}
                ]
            )
            return response.choices[0].message['content']

        def vr_fitness_idea():
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Generate VR fitness game ideas."},
                    {"role": "user", "content": "Generate VR fitness game ideas."}
                ]
            )
            return response.choices[0].message['content']

        def sarcastic_chatbot(user_input):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Respond sarcastically."},
                    {"role": "user", "content": f"{user_input}"}
                ]
            )
            return response.choices[0].message['content']

        def turn_by_turn_directions(location):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Provide turn by turn directions."},
                    {"role": "user", "content": f"Provide turn by turn directions to: {location}"}
                ]
            )
            return response.choices[0].message['content']

        def generate_interview_questions(topic):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Generate interview questions."},
                    {"role": "user", "content": f"Generate interview questions on: {topic}"}
                ]
            )
            return response.choices[0].message['content']

        def create_function_from_spec(spec):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Create a Python function from the specification."},
                    {"role": "user", "content": f"Create a Python function from this spec: {spec}"}
                ]
            )
            return response.choices[0].message['content']

        def improve_code_efficiency(code):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Improve the efficiency of the code."},
                    {"role": "user", "content": f"Improve the efficiency of this code: {code}"}
                ]
            )
            return response.choices[0].message['content']

        def create_single_page_website(topic):
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                max_tokens=100,
                messages=[
                    {"role": "system", "content": "Create a single page website."},
                    {"role": "user", "content": f"Create a single page website about: {topic}"}
                ]
            )
            return response.choices[0].message['content']

        # Streamlit app layout
        st.title('OpenAI GPT-3.5 Model Explorer')
        st.markdown('''<style>body {background-color: #f5f5f5;} .stTextInput, .stButton, .stMarkdown {background-color: #ffffff; border-radius: 10px; padding: 10px;}</style>''', unsafe_allow_html=True)

        st.sidebar.title('Model Functions')
        selected_function = st.sidebar.radio('Select a function', [
            'Text Summarization', 'Grammar Correction', 'Simplify Text', 
            'Parse Unstructured Data', 'Emoji Translation', 
            'Calculate Time Complexity', 'Explain Code', 
            'Extract Keywords', 'Generate Product Name', 
            'Fix Python Bug', 'Create Spreadsheet', 
            'Classify Tweet', 'Extract Airport Code', 
            'Mood to Color', 'VR Fitness Idea', 
            'Sarcastic Chatbot', 'Turn by Turn Directions', 
            'Generate Interview Questions', 'Create Function from Spec', 
            'Improve Code Efficiency', 'Create Single Page Website'
        ])

        # Show markdown based on the selected function
        if selected_function == 'Text Summarization':
            st.markdown('### 📄 Text Summarization\nSummarize the given text.')
        elif selected_function == 'Grammar Correction':
            st.markdown('### 📝 Grammar Correction\nCorrect the grammar of the given text.')
        elif selected_function == 'Simplify Text':
            st.markdown('### ✏️ Simplify Text\nSimplify the given text for a second grader.')
        elif selected_function == 'Parse Unstructured Data':
            st.markdown('### 🗂️ Parse Unstructured Data\nParse unstructured data into a table.')
        elif selected_function == 'Emoji Translation':
            st.markdown('### 😀 Emoji Translation\nTranslate the given text into emojis.')
        elif selected_function == 'Calculate Time Complexity':
            st.markdown('### ⏱️ Calculate Time Complexity\nCalculate the time complexity of the given code.')
        elif selected_function == 'Explain Code':
            st.markdown('### 💻 Explain Code\nExplain the given code.')
        elif selected_function == 'Extract Keywords':
            st.markdown('### 🔍 Extract Keywords\nExtract keywords from the given text.')
        elif selected_function == 'Generate Product Name':
            st.markdown('### 🛒 Generate Product Name\nGenerate product names based on the given description and seed words.')
        elif selected_function == 'Fix Python Bug':
            st.markdown('### 🐍 Fix Python Bug\nFix the bug in the given Python code.')
        elif selected_function == 'Create Spreadsheet':
            st.markdown('### 📊 Create Spreadsheet\nCreate a spreadsheet based on the given data.')
        elif selected_function == 'Classify Tweet':
            st.markdown('### 🐦 Classify Tweet\nClassify the sentiment of the given tweet.')
        elif selected_function == 'Extract Airport Code':
            st.markdown('### 🛫 Extract Airport Code\nExtract airport codes from the given text.')
        elif selected_function == 'Mood to Color':
            st.markdown('### 🎨 Mood to Color\nTranslate the given mood to a color.')
        elif selected_function == 'VR Fitness Idea':
            st.markdown('### 🕶️ VR Fitness Idea\nGenerate VR fitness game ideas.')
        elif selected_function == 'Sarcastic Chatbot':
            st.markdown('### 😏 Sarcastic Chatbot\nRespond sarcastically to the given input.')
        elif selected_function == 'Turn by Turn Directions':
            st.markdown('### 🗺️ Turn by Turn Directions\nProvide turn by turn directions to the given location.')
        elif selected_function == 'Generate Interview Questions':
            st.markdown('### ❓ Generate Interview Questions\nGenerate interview questions on the given topic.')
        elif selected_function == 'Create Function from Spec':
            st.markdown('### 🛠️ Create Function from Spec\nCreate a Python function from the given specification.')
        elif selected_function == 'Improve Code Efficiency':
            st.markdown('### ⚙️ Improve Code Efficiency\nImprove the efficiency of the given code.')
        elif selected_function == 'Create Single Page Website':
            st.markdown('### 🌐 Create Single Page Website\nCreate a single page website about the given topic.')

        input_text = st.text_area('Input text/code here:')
        if st.button('Generate'):
            if selected_function == 'Text Summarization':
                output = text_summarization(input_text)
            elif selected_function == 'Grammar Correction':
                output = grammar_correction(input_text)
            elif selected_function == 'Simplify Text':
                output = simplify_text(input_text)
            elif selected_function == 'Parse Unstructured Data':
                output = parse_unstructured_data(input_text)
            elif selected_function == 'Emoji Translation':
                output = emoji_translation(input_text)
            elif selected_function == 'Calculate Time Complexity':
                output = calculate_time_complexity(input_text)
            elif selected_function == 'Explain Code':
                output = explain_code(input_text)
            elif selected_function == 'Extract Keywords':
                output = extract_keywords(input_text)
            elif selected_function == 'Generate Product Name':
                seed_words = st.text_input('Enter seed words (comma-separated):')
                output = generate_product_name(input_text, seed_words)
            elif selected_function == 'Fix Python Bug':
                output = fix_python_bug(input_text)
            elif selected_function == 'Create Spreadsheet':
                output = create_spreadsheet(input_text)
            elif selected_function == 'Classify Tweet':
                output = classify_tweet(input_text)
            elif selected_function == 'Extract Airport Code':
                output = extract_airport_code(input_text)
            elif selected_function == 'Mood to Color':
                output = mood_to_color(input_text)
            elif selected_function == 'VR Fitness Idea':
                output = vr_fitness_idea()
            elif selected_function == 'Sarcastic Chatbot':
                output = sarcastic_chatbot(input_text)
            elif selected_function == 'Turn by Turn Directions':
                output = turn_by_turn_directions(input_text)
            elif selected_function == 'Generate Interview Questions':
                output = generate_interview_questions(input_text)
            elif selected_function == 'Create Function from Spec':
                output = create_function_from_spec(input_text)
            elif selected_function == 'Improve Code Efficiency':
                output = improve_code_efficiency(input_text)
            elif selected_function == 'Create Single Page Website':
                output = create_single_page_website(input_text)

            st.markdown('### Output:')
            st.write(output)

if __name__ == "__main__":
    display_openai_models()
