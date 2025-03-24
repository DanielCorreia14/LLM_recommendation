<<<<<<< HEAD
# LLM_recommendation
=======
# llm_recommendation

A simple Python script that uses OpenAI’s GPT‑3.5‑turbo model to generate product recommendations via the ChatCompletion API.

## 📝 Description

This project demonstrates how to call OpenAI’s chat endpoint from Python to retrieve and display recommendations for running shoes targeted at beginner runners. It covers environment setup, API configuration, and basic cost estimation. 

Note: The output and csv may vary

## 🚀 Features

- Loads API key securely from a `.env` file  
- Sends user prompt to GPT‑3.5‑turbo via ChatCompletion  
- Prints a formatted, objective recommendation list with purchase links  
- Configurable max tokens & temperature  


## 📦 Requirements

- Python 3.10+  
- An OpenAI API key with usage credit  

## ⚙️ Installation

1. Clone the repository  
   ```bash
   ```git clone https://github.com/<your‑username>/llm_recommendation.git```
   ```cd llm_recommendation/src```


2. Create & activate a virtual environment
    ```python -m venv venv```
    ```source venv/bin/activate   # Linux/macOS```
    ```venv\Scripts\activate      # Windows```

3. Install dependencies
    ```pip install -r ../requirements.txt```


# 🔐 Configuration
    Create a .env file in src/ with:
        ```OPENAI_API_KEY=sk-...```


# ▶️ Usage
Run the script:

    ```python llm_recommendation.py```

Adjust prompt, model, max_tokens, and temperature directly in the code.

# 📊 Output Schema
Each JSON object has:

Field	Type	Description
model	string	Shoe model name
brand	string	Always “Nike”
link	string	Short URL (domain + slug)
source	string	Website or marketplace name
valid	boolean	True if HTTP status = 200

# 📈 Domain Breakdown
CSV columns:

domain	percentage
example.com	50.0
another.com	50.0


# 💲 Cost Estimation
    GPT‑3.5‑turbo pricing (Mar 2025):

    $0.0015 per 1K tokens (input + output)

    ```Example: 100 tokens prompt + 200 tokens response → 300 tokens → $0.00045 per request```


# 🛠️ Customization
    - Change model to "gpt-4" for higher quality (higher cost)
    - Lower temperature (0–0.3) for deterministic answers
    - Increase temperature (0.7+) for more creative responses


# 🤝 Contributing
    - Fork repo
    - Create a feature branch
    - Submit a pull request

# 📄 License
MIT © 2025 Daniel Mangabeira Correia


>>>>>>> master
