# Recru AI Content Studio

## Project Overview

This project is a beginner-friendly Gradio app for creating recruitment and employer-brand content for the creative industry.

It combines:

- A primary knowledge base with Recru AI brand information
- A secondary knowledge base with recruitment market context
- Optional source inputs such as article links, uploaded PDFs, and white-label company logos

Then it sends that information to an AI model and generates content that fits the selected format and brand mode.

## What the App Does

The app can:

- Launch a dark, premium Gradio interface
- Let you choose from six content types:
  - LinkedIn Post
  - LinkedIn Card
  - Instagram Card
  - Instagram Caption
  - Blog Post
  - Email Newsletter
- Switch between `Manual Prompt` and `Create from Source`
- Generate content from a topic, article link, PDF, or uploaded company logo
- Switch into white-label mode when a company logo is uploaded
- Generate branded visual posts for LinkedIn Card and Instagram Card
- Let you pick visual style, background color, pastel swatches, and logo background color
- Preview the generated content and visual output inside the app
- Save generated content as Markdown and PDF
- Save visual posts as PNG
- Keep all generated files in the `outputs/` folder

## Tech Stack

- Python
- Markdown
- OpenAI API
- python-dotenv
- Gradio
- ReportLab
- Pillow
- VS Code
- GitHub

## Folder Structure

```text
ai-content-creator/
│
├── src/
│   ├── document_processor.py
│   ├── knowledge_base.py
│   ├── prompt_templates.py
│   ├── llm_integration.py
│   ├── visual_post_generator.py
│   ├── content_pipeline.py
│   └── main.py
│
├── knowledge_base/
│   ├── primary/
│   │   ├── brand_voice.md
│   │   ├── audience.md
│   │   ├── services.md
│   │   └── past_content.md
│   │
│   └── secondary/
│       ├── market_trends.md
│       ├── competitor_analysis.md
│       ├── audience_pain_points.md
│       └── industry_news.md
│
├── prompts/
│   ├── linkedin_prompt.md
│   ├── instagram_prompt.md
│   ├── blog_prompt.md
│   └── email_prompt.md
│
├── outputs/
├── config/
├── screenshots/
├── PROJECT_REQUIREMENTS.md
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

## Setup Instructions

### 1. Open the project folder in VS Code

Open the folder called:

```bash
ai-content-creator
```

### 2. Create a virtual environment

A virtual environment is a private Python workspace for this project.

Run:

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

On Mac:

```bash
source venv/bin/activate
```

### 4. Install packages

Packages are extra Python tools your project needs.

Run:

```bash
pip install -r requirements.txt
```

### 5. Create your `.env` file

Copy `.env.example`.

Rename the copy to:

```text
.env
```

Add your OpenAI API key:

```text
OPENAI_API_KEY=your_api_key_here
```

Do not upload `.env` to GitHub.

### 6. Run the app

Run:

```bash
python src/main.py
```

This launches the Gradio UI in your browser at `http://127.0.0.1:7860`.

## Example Use

The app gives you two creation paths:

- `Manual Prompt` for writing from scratch
- `Create from Source` for article links, PDFs, and white-label logo uploads

Content type examples:

- LinkedIn Post
- LinkedIn Card
- Instagram Card
- Instagram Caption
- Blog Post
- Email Newsletter

Visual post options include:

- Recru AI logo or uploaded company logo
- Background color swatches
- Logo background color swatches
- PNG preview in the app
- Download/save buttons for PNG and PDF

Generated files are saved in `outputs/` with clean names based on the selected content type.

## Uniqueness Strategy

This project avoids generic AI output by using:

- Recru AI brand voice
- Architecture and design recruitment context
- Audience pain points
- Market trends
- Competitor positioning
- Optional source material from articles and PDFs
- White-label support for company logos

## Final Deliverables

- GitHub repo
- Working Python app
- Knowledge base markdown files
- Prompt templates
- Generated content output in Markdown, PDF, and PNG
- Uniqueness comparison
- README.md
- PROJECT_REQUIREMENTS.md
- Trello screenshots
