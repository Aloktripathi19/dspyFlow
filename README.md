# 🚀 dspy CLI Tool

A CLI application that refines vague prompts, generates step-by-step answers with chain-of-thought reasoning, and produces concise summaries using DSPy and Typer.

## ✨ Features

### 📝 Prompt Refinement
Automatically rewrites vague prompts into clear, precise questions.

### 🤖 Chain-of-Thought Answering
Generates a detailed reasoning process alongside the final answer.

### 📋 Answer Summarization
Produces a concise bullet-point summary of the final answer.

## 📦 Prerequisites

- 🐍 Python 3.8+  
- 🔑 OpenAI API key with GPT-4 or GPT-3.5 access  
- 📦 `pip` package manager  

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/Aloktripathi19/DSPy.git
cd dspy-cli-tool
```

## Install dependencies

- pip install -r requirements.txt

## Configure environment variables
Create a .env file in the project root:

- OPENAI_API_KEY=your_openai_api_key_here

### Verify setup
python -c "import os; assert os.getenv('OPENAI_API_KEY'), 'API key not set'"

## ⚙️ Configuration
- 🧠 Model Choice: Update the model in main.py when calling dspy.LM() (e.g. openai/gpt-4, openai/gpt-3.5-turbo).
- 🔒 API Key: Automatically loaded from the .env file via python-dotenv.

## 📚 Code Overview

### Signatures

#### PromptRefinementSignature
- `vague_prompt` (Input)  
- `improved_prompt` (Output)  

#### StepwiseAnswerSignature
- `question` (Input)  
- `thought_process` (Output)  
- `final_answer` (Output)  

#### AnswerSummarySignature
- `full_answer` (Input)  
- `concise_summary` (Output)  

### 🏗️ Modules

#### PromptRefiner
Uses `dspy.Predict` to refine prompts.

#### StepwiseAnswerer
Uses `dspy.ChainOfThought` to generate reasoning and answers.

#### AnswerSummarizer
Uses `dspy.Predict` to produce concise summaries.

## 💻 Typer CLI

### `ask` command
- 🎯 Refines the prompt  
- 🧩 Generates thought process and final answer  
- ✂️ Summarizes the answer  

## 📖 Usage

```bash
python main.py ask "Explain microservices architecture."
```
## 🔧 Customization
- 🆕 Define additional dspy.Signature classes for new use cases.
- ➕ Add new dspy.Module implementations and corresponding CLI commands.