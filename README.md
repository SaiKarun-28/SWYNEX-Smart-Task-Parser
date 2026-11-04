# SWYNEX-Smart-Task-Parser

An AI-powered utility that converts natural language task descriptions into structured, categorised data for productivity applications.

## Overview

The Smart Task Parser is a prototype designed to reduce the friction of manual data entry in task management systems. By leveraging Large Language Models (LLMs), it interprets unstructured user input—such as "Finish the budget report by next Tuesday"—and extracts core components including the task description, logical category, priority level, and inferred deadlines. This project demonstrates robust API integration, precise prompt engineering, and structured data validation using Pydantic.

## Features

- **Natural Language Understanding:** Interprets colloquial time expressions and vague task descriptions.
- **Automated Categorisation:** Assigns tasks to logical buckets like Work, Personal, Shopping, or Errands.
- **Priority Inference:** Determines task urgency based on context and keywords.
- **Structured JSON Output:** Returns valid, schema-enforced JSON ready for integration into any database or UI.
- **Ambiguity Handling:** Flags inputs that lack sufficient context for confident parsing.

## Technical Stack

- **Language:** Python 3.12+
- **Inference:** OpenAI or Anthropic API
- **Validation:** Pydantic
- **Interface:** Command Line Interface (CLI)

## Setup

Ensure you have Python 3.12 or higher installed. Clone the repository and install the required dependencies.

```bash
git clone https://github.com/SaiKarun-28/SWYNEX-Smart-Task-Parser.git
cd SWYNEX-Smart-Task-Parser
pip install -r requirements.txt
```

You must provide your own API key in a `.env` file (not included in the repository for security).

```env
API_KEY=your_secret_key_here
```

## Usage

Run the parser directly from the terminal with your task string as an argument.

```bash
python parser.py "Pick up groceries after the gym tomorrow at 6pm"
```

The tool will output a structured JSON object representing the parsed task.

## License

This project is for educational purposes as part of the SWYNEX Internship programme.
