# Personal AI/ML Portfolio (Streamlit)

This is a Streamlit-based personal website for showcasing your AI/ML projects, skills, and blog posts. It is fully configurable via `config.yaml`.

## Features

- **Hero section** with your name, title, summary, and social links.
- **Projects showcase** with:
  - Live demo links
  - GitHub repositories
  - Tech stack details
  - Key metrics and results
  - Optional screenshots or GIFs
- **Skills matrix** grouped by categories.
- **Contact information** (email, location, availability, optional Calendly).
- **Optional blog section** that links out to your posts.

## Getting Started

1. Create and activate a virtual environment (recommended).

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Customize `config.yaml` with your own:
   - Name, title, summary, avatar image
   - Social links
   - Projects (including links, tech stack, metrics, screenshots)
   - Skills
   - Contact details
   - Blog posts (optional)

4. Run the app:

   ```bash
   streamlit run app.py
   ```

5. Open the URL that Streamlit prints in your terminal (usually `http://localhost:8501`).

You now have a personal AI/ML portfolio website powered by Streamlit and driven entirely by your `config.yaml` configuration.

