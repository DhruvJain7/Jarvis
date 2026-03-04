- This project was made in order to pratice the Langchain concepts I learned in **Develop Generative AI Applications: Get Started** course which is a part of **IBM RAG and Agentic AI** professional certificate.

# J.A.R.V.I.S. (LangChain Practice)

A streamlined AI assistant built as a practical exercise within the **IBM RAG and Agentic Reasoning** curriculum. This project focuses on mastering **LangChain** fundamentals, specifically implementing conversation memory and multi-model integration via the **Groq API**.

## Overview

This application is a hands-on implementation designed to explore how LangChain orchestrates interactions between a user and various Large Language Models (LLMs). It serves as a foundational step in understanding agentic workflows and memory management in AI applications.

## Core Technologies

* **LangChain**: Used for prompt engineering and managing the conversation flow.
* **Groq API**: Utilized for high-speed inference on open-source models.

## Integrated Models

The project is configured to work with the following models:

* **Llama 3.3 70B Versatile** (`llama-3.3-70b-versatile`)
* **GPT-OSS 120B** (`openai/gpt-oss-120b`)
* **Llama 4 Maverick 17B** (`meta-llama/llama-4-maverick-17b-128e-instruct`)

## Key Features


* **Educational Focus**: Built following the IBM course structure to practice RAG and reasoning patterns.
* **Model Flexibility**: Easily switch between different high-performance models provided by Groq.

## Installation

1. **Clone the Repository**
```bash
git clone https://github.com/DhruvJain7/Jarvis.git
cd Jarvis

```


2. **Environment Setup**
Create a `.env` file in the root directory and add your Groq API key:
```env
GROQ_API_KEY=your_groq_api_key_here

```


3. **Install Dependencies**
```bash
pip install langchain-groq python-dotenv

```



## Usage

Launch the assistant by running:

```bash
python app.py

```

## License

MIT License


