import streamlit as st
import google.generativeai as genai

# Set page configuration (ensure this is the first Streamlit command)
st.set_page_config(page_title="Generative AI Project", page_icon=":robot_face:", layout="wide")

def display_gemini_models():
    # Sidebar for API key input
    st.sidebar.title('Gemnai API Key')

    # Check if the API key is already in session state
    if "gemnai_api_key" not in st.session_state or not st.session_state.gemnai_api_key:
        # If API key is not set, show input for API key
        api_key = st.sidebar.text_input("Enter your Gemnai API key:", type="password")
        if st.sidebar.button("Submit"):
            st.session_state.gemnai_api_key = api_key
            # Optionally, validate API key here
    else:
        # Configure the Gemnai API key
        api_key = st.session_state.gemnai_api_key
        genai.configure(api_key=api_key)

        def get_gemini_response(prompt):
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            return response.text if response else "No response from the model."

        # Define individual task functions
        def fitness_plan_generator_app():
            prompt_input = st.text_area("Enter details for fitness plan:", "", height=200, max_chars=5000)
            if st.button('Generate Fitness Plan 🏋️‍♂️'):
                if prompt_input:
                    prompt = f"Generate a fitness plan based on the following details:\n{prompt_input}"
                    st.write("**Generated Fitness Plan:**")
                    response = get_gemini_response(prompt)
                    st.write(response)

        def grammar_correction_app():
            text_input = st.text_area("Enter text to correct grammar:", "", height=200, max_chars=5000)
            if st.button('Correct Grammar ✍️'):
                if text_input:
                    prompt = f"Correct the grammar in the following text:\n{text_input}"
                    st.write("**Corrected Text:**")
                    response = get_gemini_response(prompt)
                    st.write(response)

        def keyword_extractor_app():
            text_input = st.text_area("Enter text to extract keywords from:", "", height=200, max_chars=5000)
            if st.button('Extract Keywords 🔑'):
                if text_input:
                    prompt = f"Extract keywords from the following text:\n{text_input}"
                    st.write("**Extracted Keywords:**")
                    response = get_gemini_response(prompt)
                    st.write(response)

        def language_translator_app():
            text_input = st.text_area("Enter text to translate:", "", height=100, max_chars=5000)
            target_language = st.text_input("Enter target language:", "")
            if st.button('Translate 🌐'):
                if text_input and target_language:
                    prompt = f"Translate the following text into {target_language}:\n{text_input}"
                    st.write("**Translated Text:**")
                    response = get_gemini_response(prompt)
                    st.write(response)

        def memo_writer_app():
            prompt_input = st.text_area("Enter details for the memo:", "", height=200, max_chars=5000)
            if st.button('Write Memo 📝'):
                if prompt_input:
                    prompt = f"Write a memo based on the following details:\n{prompt_input}"
                    st.write("**Generated Memo:**")
                    response = get_gemini_response(prompt)
                    st.write(response)

        def personal_tutor_app():
            text_input = st.text_area("Enter topic or question for tutoring:", "", height=200, max_chars=5000)
            if st.button('Get Tutoring 🎓'):
                if text_input:
                    prompt = f"Act as a personal tutor and explain the following topic in detail:\n{text_input}"
                    st.write("**Tutoring Response:**")
                    response = get_gemini_response(prompt)
                    st.write(response)

        def poetry_generator_app():
            prompt_input = st.text_area("Enter details for the poem:", "", height=200, max_chars=5000)
            if st.button('Generate Poem 📜'):
                if prompt_input:
                    prompt = f"Generate a poem based on the following details:\n{prompt_input}"
                    st.write("**Generated Poem:**")
                    response = get_gemini_response(prompt)
                    st.write(response)

        def python_debugger_app():
            code_input = st.text_area("Enter Python code to debug:", "", height=200, max_chars=5000)
            if st.button('Debug Code 🐍'):
                if code_input:
                    prompt = f"Debug the following Python code and provide suggestions for fixes:\n{code_input}"
                    st.write("**Debugging Suggestions:**")
                    response = get_gemini_response(prompt)
                    st.write(response)

        def python_interpreter_app():
            code_input = st.text_area("Enter Python code to interpret:", "", height=200, max_chars=5000)
            if st.button('Interpret Code 🖥️'):
                if code_input:
                    prompt = f"Interpret the following Python code and explain its functionality:\n{code_input}"
                    st.write("**Code Interpretation:**")
                    response = get_gemini_response(prompt)
                    st.write(response)

        def sentiment_analysis_app():
            text_input = st.text_area("Enter text to analyze sentiment:", "", height=200, max_chars=5000)
            if st.button('Analyze Sentiment 🧠'):
                if text_input:
                    prompt = f"Analyze the sentiment of the following text:\n{text_input}"
                    st.write("**Sentiment Analysis Result:**")
                    response = get_gemini_response(prompt)
                    st.write(response)

        def social_media_post_generator_app():
            prompt_input = st.text_area("Enter details for the social media post:", "", height=200, max_chars=5000)
            if st.button('Generate Post 📱'):
                if prompt_input:
                    prompt = f"Generate a social media post based on the following details:\n{prompt_input}"
                    st.write("**Generated Social Media Post:**")
                    response = get_gemini_response(prompt)
                    st.write(response)

        def text_generator_app():
            prompt_input = st.text_area("Enter details for text generation:", "", height=200, max_chars=5000)
            if st.button('Generate Text 📝'):
                if prompt_input:
                    prompt = f"Generate text based on the following details:\n{prompt_input}"
                    st.write("**Generated Text:**")
                    response = get_gemini_response(prompt)
                    st.write(response)

        def text_summarization_app():
            text_input = st.text_area("Enter text to summarize:", "", height=200, max_chars=5000)
            if st.button('Summarize Text 📖'):
                if text_input:
                    prompt = f"Summarize the following text:\n{text_input}"
                    st.write("**Summarized Text:**")
                    response = get_gemini_response(prompt)
                    st.write(response)

        def zero_shot_classification_app():
            text_input = st.text_area("Enter text for zero-shot classification:", "", height=200, max_chars=5000)
            categories = st.text_input("Enter categories (comma-separated):", "")
            if st.button('Classify Text 🏷️'):
                if text_input and categories:
                    prompt = f"Classify the following text into the categories: {categories}.\n\nText: {text_input}"
                    st.write("**Classification Result:**")
                    response = get_gemini_response(prompt)
                    st.write(response)

        def token_classification_app():
            text_input = st.text_area("Enter text for token classification:", "", height=200, max_chars=5000)
            if st.button('Classify Tokens 🔠'):
                if text_input:
                    prompt = f"Classify the tokens in the following text:\n{text_input}"
                    st.write("**Token Classification Result:**")
                    response = get_gemini_response(prompt)
                    st.write(response)

        def feature_extraction_app():
            text_input = st.text_area("Enter text for feature extraction:", "", height=200, max_chars=5000)
            if st.button('Extract Features 🔍'):
                if text_input:
                    prompt = f"Extract features from the following text:\n{text_input}"
                    st.write("**Extracted Features:**")
                    response = get_gemini_response(prompt)
                    st.write(response)

        def interview_question_generation_app():
            prompt_input = st.text_area("Enter details for interview question generation:", "", height=200, max_chars=5000)
            if st.button('Generate Interview Questions 🗣️'):
                if prompt_input:
                    prompt = f"Generate interview questions based on the following details:\n{prompt_input}"
                    st.write("**Generated Interview Questions:**")
                    response = get_gemini_response(prompt)
                    st.write(response)

        def brand_name_generation_app():
            prompt_input = st.text_area("Enter details for brand name generation:", "", height=200, max_chars=5000)
            if st.button('Generate Brand Name 🌟'):
                if prompt_input:
                    prompt = f"Generate a brand name based on the following details:\n{prompt_input}"
                    st.write("**Generated Brand Name:**")
                    response = get_gemini_response(prompt)
                    st.write(response)

        def website_building_app():
            prompt_input = st.text_area("Enter details for website building:", "", height=200, max_chars=5000)
            if st.button('Generate Website Code 💻'):
                if prompt_input:
                    prompt = f"Generate website code based on the following details:\n{prompt_input}"
                    st.write("**Generated Website Code:**")
                    response = get_gemini_response(prompt)
                    st.write(response)

        def custom_task_app():
            prompt_input = st.text_area("Enter details for custom task:", "", height=200, max_chars=5000)
            if st.button('Execute Custom Task ⚙️'):
                if prompt_input:
                    prompt = f"Execute the following custom task based on these details:\n{prompt_input}"
                    st.write("**Custom Task Result:**")
                    response = get_gemini_response(prompt)
                    st.write(response)

        # Sidebar for task selection with radio buttons
        st.sidebar.title('Select Task')
        task = st.sidebar.radio("Choose a task:", [
            "Fitness Plan Generator 🏋️‍♂️", "Grammar Correction ✍️", "Keyword Extractor 🔑",
            "Language Translator 🌐", "Memo Writer 📝", "Personal Tutor 🎓", 
            "Poetry Generator 📜", "Python Debugger 🐍", "Python Interpreter 🖥️", 
            "Sentiment Analysis 🧠", "Social Media Post Generator 📱", "Text Generator 📝", 
            "Text Summarization 📖", "Zero-Shot Classification 🏷️", "Token Classification 🔠", 
            "Feature Extraction 🔍", "Interview Question Generation 🗣️", 
            "Brand Name Generation 🌟", "Website Building 💻", "Custom Task ⚙️"
        ])

        # Main content area with Markdown headings and descriptions
        st.write(f"# Selected Task: {task}")
        
        # Call appropriate function based on selected task
        if task == "Fitness Plan Generator 🏋️‍♂️":
            st.write("## Fitness Plan Generator 🏋️‍♂️")
            st.write("Create personalized fitness plans based on your input details. Ideal for generating workout routines and health plans.")
            fitness_plan_generator_app()
        elif task == "Grammar Correction ✍️":
            st.write("## Grammar Correction ✍️")
            st.write("Correct grammar and improve text readability.")
            grammar_correction_app()
        elif task == "Keyword Extractor 🔑":
            st.write("## Keyword Extractor 🔑")
            st.write("Extract important keywords from your text.")
            keyword_extractor_app()
        elif task == "Language Translator 🌐":
            st.write("## Language Translator 🌐")
            st.write("Translate text into different languages.")
            language_translator_app()
        elif task == "Memo Writer 📝":
            st.write("## Memo Writer 📝")
            st.write("Generate memos based on the provided details.")
            memo_writer_app()
        elif task == "Personal Tutor 🎓":
            st.write("## Personal Tutor 🎓")
            st.write("Get detailed explanations and tutoring on various topics.")
            personal_tutor_app()
        elif task == "Poetry Generator 📜":
            st.write("## Poetry Generator 📜")
            st.write("Create personalized poems based on your input.")
            poetry_generator_app()
        elif task == "Python Debugger 🐍":
            st.write("## Python Debugger 🐍")
            st.write("Debug Python code and get suggestions for fixes.")
            python_debugger_app()
        elif task == "Python Interpreter 🖥️":
            st.write("## Python Interpreter 🖥️")
            st.write("Interpret and explain Python code functionality.")
            python_interpreter_app()
        elif task == "Sentiment Analysis 🧠":
            st.write("## Sentiment Analysis 🧠")
            st.write("Analyze the sentiment of your text.")
            sentiment_analysis_app()
        elif task == "Social Media Post Generator 📱":
            st.write("## Social Media Post Generator 📱")
            st.write("Generate engaging social media posts based on input.")
            social_media_post_generator_app()
        elif task == "Text Generator 📝":
            st.write("## Text Generator 📝")
            st.write("Generate text based on provided details.")
            text_generator_app()
        elif task == "Text Summarization 📖":
            st.write("## Text Summarization 📖")
            st.write("Summarize lengthy text into concise summaries.")
            text_summarization_app()
        elif task == "Zero-Shot Classification 🏷️":
            st.write("## Zero-Shot Classification 🏷️")
            st.write("Classify text into categories without training.")
            zero_shot_classification_app()
        elif task == "Token Classification 🔠":
            st.write("## Token Classification 🔠")
            st.write("Classify tokens in the provided text.")
            token_classification_app()
        elif task == "Feature Extraction 🔍":
            st.write("## Feature Extraction 🔍")
            st.write("Extract features from text data.")
            feature_extraction_app()
        elif task == "Interview Question Generation 🗣️":
            st.write("## Interview Question Generation 🗣️")
            st.write("Generate relevant interview questions based on input.")
            interview_question_generation_app()
        elif task == "Brand Name Generation 🌟":
            st.write("## Brand Name Generation 🌟")
            st.write("Generate creative brand names based on details.")
            brand_name_generation_app()
        elif task == "Website Building 💻":
            st.write("## Website Building 💻")
            st.write("Generate website code based on provided specifications.")
            website_building_app()
        elif task == "Custom Task ⚙️":
            st.write("## Custom Task ⚙️")
            st.write("Execute custom tasks based on user-defined details.")
            custom_task_app()

# Call the function to display the app
display_gemini_models()
