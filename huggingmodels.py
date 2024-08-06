import streamlit as st
import requests

# Set page configuration (must be the first Streamlit command)
# st.set_page_config(page_title="Generative AI Project", page_icon=":robot_face:", layout="wide")

# Function to generate text from the Hugging Face API

def generate_text(model_url, prompt, api_token, max_length=50):
    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": max_length
        }
    }
    
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }
    
    response = requests.post(model_url, headers=headers, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        return result.get('generated_text', "No text generated")
    else:
        return f"Error {response.status_code}: {response.text}"

# Function to handle the main content based on selected model

def app_content(api_token):
    st.sidebar.title("🔧 Model Selection")
    app_selection = st.sidebar.radio(
        "Select a Model",
        [
            "Fitness Plan Generator",
            "Grammar Correction",
            "Keyword Extractor",
            "Language Translator",
            "Memo Writer",
            "Personal Tutor",
            "Poetry Generator",
            "Python Debugger",
            "Python Interpreter",
            "Sentiment Analysis",
            "Social Media Post Generator",
            "Text Generator",
            "Text Summarization",
            "Zero-Shot Classification",
            "Token Classification"
        ]
    )

    # Define model URLs here (replace with actual model URLs)
    model_urls = {
        "Fitness Plan Generator": "https://api-inference.huggingface.co/models/gpt2",
        "Grammar Correction": "https://api-inference.huggingface.co/models/gpt2",
        "Keyword Extractor": "https://api-inference.huggingface.co/models/gpt2",
        "Language Translator": "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-{target_language}",
        "Memo Writer": "https://api-inference.huggingface.co/models/gpt2",
        "Personal Tutor": "https://api-inference.huggingface.co/models/gpt2",
        "Poetry Generator": "https://api-inference.huggingface.co/models/gpt2",
        "Python Debugger": "https://api-inference.huggingface.co/models/gpt2",
        "Python Interpreter": "https://api-inference.huggingface.co/models/gpt2",
        "Sentiment Analysis": "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english",
        "Social Media Post Generator": "https://api-inference.huggingface.co/models/gpt2",
        "Text Generator": "https://api-inference.huggingface.co/models/gpt2",
        "Text Summarization": "https://api-inference.huggingface.co/models/facebook/bart-large-cnn",
        "Zero-Shot Classification": "https://api-inference.huggingface.co/models/facebook/bart-large-mnli",
        "Token Classification": "https://api-inference.huggingface.co/models/bert-base-ner"
    }

    model_url = model_urls.get(app_selection, None)

    if app_selection == "Fitness Plan Generator":
        fitness_plan_generator_app(api_token, model_url)
    elif app_selection == "Grammar Correction":
        grammar_correction_app(api_token, model_url)
    elif app_selection == "Keyword Extractor":
        keyword_extractor_app(api_token, model_url)
    elif app_selection == "Language Translator":
        language_translator_app(api_token, model_url)
    elif app_selection == "Memo Writer":
        memo_writer_app(api_token, model_url)
    elif app_selection == "Personal Tutor":
        personal_tutor_app(api_token, model_url)
    elif app_selection == "Poetry Generator":
        poetry_generator_app(api_token, model_url)
    elif app_selection == "Python Debugger":
        python_debugger_app(api_token, model_url)
    elif app_selection == "Python Interpreter":
        python_interpreter_app(api_token, model_url)
    elif app_selection == "Sentiment Analysis":
        sentiment_analysis_app(api_token, model_url)
    elif app_selection == "Social Media Post Generator":
        social_media_post_generator_app(api_token, model_url)
    elif app_selection == "Text Generator":
        text_generator_app(api_token, model_url)
    elif app_selection == "Text Summarization":
        text_summarization_app(api_token, model_url)
    elif app_selection == "Zero-Shot Classification":
        zero_shot_classification_app(api_token, model_url)
    elif app_selection == "Token Classification":
        token_classification_app(api_token, model_url)

# Function to generate content for each model (similar to above examples)
def fitness_plan_generator_app(api_token, model_url):
    prompt_input = st.text_area("📝 Enter details for fitness plan:", "", height=150, max_chars=5000)
    if st.button('Generate Fitness Plan'):
        if prompt_input:
            prompt = f"Generate a fitness plan based on the following details:\n{prompt_input}"
            response = generate_text(model_url, prompt, api_token)
            st.write("**Generated Fitness Plan:**")
            st.write(response)

def grammar_correction_app(api_token, model_url):
    text_input = st.text_area("📝 Enter text to correct grammar:", "", height=150, max_chars=5000)
    if st.button('Correct Grammar'):
        if text_input:
            prompt = f"Correct the grammar in the following text:\n{text_input}"
            response = generate_text(model_url, prompt, api_token)
            st.write("**Corrected Text:**")
            st.write(response)

def keyword_extractor_app(api_token, model_url):
    text_input = st.text_area("🔍 Enter text to extract keywords from:", "", height=150, max_chars=5000)
    if st.button('Extract Keywords'):
        if text_input:
            prompt = f"Extract keywords from the following text:\n{text_input}"
            response = generate_text(model_url, prompt, api_token)
            st.write("**Extracted Keywords:**")
            st.write(response)

def language_translator_app(api_token, model_url):
    text_input = st.text_area("🌐 Enter text to translate:", "", height=150, max_chars=5000)
    target_language = st.text_input("Enter target language:", "")
    if st.button('Translate'):
        if text_input and target_language:
            model_url = f"https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-{target_language.lower()}"
            response = generate_text(model_url, text_input, api_token)
            st.write("**Translated Text:**")
            st.write(response)

def memo_writer_app(api_token, model_url):
    prompt_input = st.text_area("📝 Enter details for the memo:", "", height=150, max_chars=5000)
    if st.button('Write Memo'):
        if prompt_input:
            prompt = f"Write a memo based on the following details:\n{prompt_input}"
            response = generate_text(model_url, prompt, api_token)
            st.write("**Generated Memo:**")
            st.write(response)

def personal_tutor_app(api_token, model_url):
    text_input = st.text_area("📚 Enter topic or question for tutoring:", "", height=150, max_chars=5000)
    if st.button('Get Tutoring'):
        if text_input:
            prompt = f"Act as a personal tutor and explain the following topic in detail:\n{text_input}"
            response = generate_text(model_url, prompt, api_token)
            st.write("**Tutoring Response:**")
            st.write(response)

def poetry_generator_app(api_token, model_url):
    prompt_input = st.text_area("✍️ Enter details for the poem:", "", height=150, max_chars=5000)
    if st.button('Generate Poem'):
        if prompt_input:
            prompt = f"Generate a poem based on the following details:\n{prompt_input}"
            response = generate_text(model_url, prompt, api_token)
            st.write("**Generated Poem:**")
            st.write(response)

def python_debugger_app(api_token, model_url):
    code_input = st.text_area("🐍 Enter Python code to debug:", "", height=150, max_chars=5000)
    if st.button('Debug Code'):
        if code_input:
            prompt = f"Debug the following Python code and provide suggestions for fixes:\n{code_input}"
            response = generate_text(model_url, prompt, api_token)
            st.write("**Debugging Suggestions:**")
            st.write(response)

def python_interpreter_app(api_token, model_url):
    code_input = st.text_area("🐍 Enter Python code to interpret:", "", height=150, max_chars=5000)
    if st.button('Interpret Code'):
        if code_input:
            prompt = f"Interpret the following Python code and explain its functionality:\n{code_input}"
            response = generate_text(model_url, prompt, api_token)
            st.write("**Code Interpretation:**")
            st.write(response)

def sentiment_analysis_app(api_token, model_url):
    text_input = st.text_area("🔍 Enter text for sentiment analysis:", "", height=150, max_chars=5000)
    if st.button('Analyze Sentiment'):
        if text_input:
            prompt = f"Analyze the sentiment of the following text:\n{text_input}"
            response = generate_text(model_url, prompt, api_token)
            st.write("**Sentiment Analysis Result:**")
            st.write(response)

def social_media_post_generator_app(api_token, model_url):
    prompt_input = st.text_area("📝 Enter details for the social media post:", "", height=150, max_chars=5000)
    if st.button('Generate Post'):
        if prompt_input:
            prompt = f"Generate a social media post based on the following details:\n{prompt_input}"
            response = generate_text(model_url, prompt, api_token)
            st.write("**Generated Social Media Post:**")
            st.write(response)

def text_generator_app(api_token, model_url):
    prompt_input = st.text_area("📝 Enter prompt for text generation:", "", height=150, max_chars=5000)
    if st.button('Generate Text'):
        if prompt_input:
            response = generate_text(model_url, prompt_input, api_token)
            st.write("**Generated Text:**")
            st.write(response)

def text_summarization_app(api_token, model_url):
    text_input = st.text_area("📄 Enter text to summarize:", "", height=150, max_chars=5000)
    if st.button('Summarize'):
        if text_input:
            response = generate_text(model_url, text_input, api_token)
            st.write("**Summary:**")
            st.write(response)

def zero_shot_classification_app(api_token, model_url):
    text_input = st.text_area("📝 Enter text for zero-shot classification:", "", height=150, max_chars=5000)
    labels_input = st.text_input("Enter labels for classification (comma separated):", "")
    if st.button('Classify'):
        if text_input and labels_input:
            labels = labels_input.split(",")
            prompt = {
                "inputs": text_input,
                "parameters": {
                    "candidate_labels": labels
                }
            }
            response = generate_text(model_url, prompt, api_token)
            st.write("**Classification Result:**")
            st.write(response)

def token_classification_app(api_token, model_url):
    text_input = st.text_area("📝 Enter text for token classification:", "", height=150, max_chars=5000)
    if st.button('Classify Tokens'):
        if text_input:
            prompt = f"Classify the tokens in the following text:\n{text_input}"
            response = generate_text(model_url, prompt, api_token)
            st.write("**Token Classification Result:**")
            st.write(response)

# Main function to run the app
def display_huggingface_models():
    st.title("Generative AI Project")
    st.write("Welcome to the Generative AI Project. Select a model from the sidebar to get started.")
    
    api_token = st.sidebar.text_input("API Token", type="password")
    
    if api_token:
        app_content(api_token)
    else:
        st.warning("Please enter your API token.")

if __name__ == "__main__":
    display_huggingface_models()
