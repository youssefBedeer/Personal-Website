import pathlib
from typing import Any, Dict, List

import requests
import streamlit as st
import yaml


@st.cache_data
def load_config(path: str = "config.yaml") -> Dict[str, Any]:
    config_path = pathlib.Path(path)
    if not config_path.exists():
        st.error(
            "Configuration file `config.yaml` not found. "
            "Please create it based on the template included in this project."
        )
        return {}
    with config_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def inject_global_styles() -> None:
    """Add custom CSS for a dark theme with premium orange accents."""
    st.markdown(
        """
        <style>
        /* Global layout */
        .stApp {
            background: #020617;
            color: #e5e7eb;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }
        .block-container {
            max-width: 1100px;
            padding-top: 1.6rem;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background: #020617;
            border-right: 1px solid rgba(55, 65, 81, 0.7);
        }
        section[data-testid="stSidebar"] .stHeading {
            font-weight: 700;
        }
        section[data-testid="stSidebar"] button {
            border-radius: 999px !important;
        }

        /* Hero card */
        .hero-card {
            padding: 2.3rem 2.5rem;
            border-radius: 20px;
            background: linear-gradient(135deg, #0b1120, #020617);
            border: 1px solid rgba(248, 153, 59, 0.55);
            box-shadow: 0 26px 60px rgba(15, 23, 42, 0.85);
        }
        .hero-title {
            font-size: 2.4rem;
            font-weight: 750;
            letter-spacing: -0.03em;
            margin-bottom: 0.25rem;
        }
        .hero-subtitle {
            font-size: 1.05rem;
            font-weight: 500;
            color: #fed7aa;
            margin-bottom: 0.8rem;
        }
        .hero-summary {
            font-size: 0.97rem;
            color: #e5e7eb;
            line-height: 1.7;
        }
        .hero-meta {
            font-size: 0.9rem;
            color: #cbd5f5;
            margin-top: 0.8rem;
        }

        /* Pills / chips */
        .pill {
            display: inline-flex;
            align-items: center;
            padding: 0.25rem 0.7rem;
            border-radius: 999px;
            font-size: 0.75rem;
            font-weight: 500;
            background: rgba(15, 23, 42, 0.9);
            color: #e5e7eb;
            margin-right: 0.35rem;
            margin-bottom: 0.3rem;
            border: 1px solid rgba(248, 153, 59, 0.7);
        }

        /* Section heading accent */
        .section-title {
            font-weight: 700 !important;
            color: #e5e7eb;
        }
        .section-title span.accent {
            color: #f97316;
        }
        .section-title::before {
            content: "";
            display: inline-block;
            width: 6px;
            height: 18px;
            border-radius: 999px;
            background: linear-gradient(180deg, #f97316, #ea580c);
            margin-right: 0.45rem;
            vertical-align: middle;
        }

        /* Project cards */
        .project-card {
            border-radius: 18px;
            padding: 1.3rem 1.4rem;
            border: 1px solid rgba(55, 65, 81, 0.8);
            background: #020617;
            box-shadow: 0 18px 45px rgba(15, 23, 42, 0.9);
            margin-bottom: 1rem;
            transition: transform 140ms ease-out, box-shadow 140ms ease-out, border-color 140ms ease-out;
        }
        .project-card:hover {
            transform: translateY(-3px);
            border-color: rgba(248, 153, 59, 0.9);
            box-shadow: 0 26px 60px rgba(15, 23, 42, 0.98);
        }
        .project-title {
            font-size: 1.05rem;
            font-weight: 600;
            margin-bottom: 0.1rem;
            color: #e5e7eb;
        }
        .project-tagline {
            font-size: 0.86rem;
            color: #9ca3af;
            margin-bottom: 0.45rem;
        }
        .project-description {
            font-size: 0.9rem;
            color: #d1d5db;
            margin-bottom: 0.3rem;
        }

        /* Skills */
        .skill-name {
            font-size: 0.9rem;
            font-weight: 600;
            color: #e5e7eb;
        }
        .skill-meta {
            font-size: 0.8rem;
            color: #9ca3af;
            margin-bottom: 0.15rem;
        }
        /* Skill progress override for a thinner bar */
        div[data-testid="stProgress"] div[role="progressbar"] {
            height: 5px;
            border-radius: 999px;
        }

        /* Blog */
        .blog-content h1, .blog-content h2, .blog-content h3 {
            margin-top: 0.9rem;
            color: #e5e7eb;
        }
        .blog-content p {
            font-size: 0.92rem;
            line-height: 1.7;
            color: #d1d5db;
        }

        /* Tabs styling (blog) */
        div[data-baseweb="tab-list"] {
            gap: 0.25rem;
        }
        div[data-baseweb="tab"] {
            border-radius: 999px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero(cfg: Dict[str, Any]) -> None:
    profile = cfg.get("profile", {})
    name = profile.get("name", "Your Name")
    title = profile.get("title", "AI/ML Engineer specializing in LLMs & MLOps")
    summary = profile.get(
        "summary",
        "I design, build, and deploy AI/ML systems with a focus on large "
        "language models, MLOps, and production-grade data pipelines.",
    )
    location = profile.get("location")
    current_role = profile.get("current_role")

    with st.container():
        col_main, col_side = st.columns([2.4, 1])

        with col_main:
            st.markdown(
                f"""
                <div class="hero-card">
                    <div class="hero-title">{name}</div>
                    <div class="hero-subtitle">{title}</div>
                    <div class="hero-summary">{summary}</div>
                    <div class="hero-meta">
                        {" • ".join(filter(None, [current_role, location]))}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        with col_side:
            social = cfg.get("social_links", {})
            st.markdown("#### Connect")
            for label, url in social.items():
                st.link_button(label, url, use_container_width=True)

            metrics = cfg.get("hero_metrics", [])
            if metrics:
                st.markdown("#### Snapshot")
                for metric in metrics:
                    st.metric(
                        label=metric.get("label", ""),
                        value=metric.get("value", ""),
                        delta=metric.get("delta"),
                    )


def render_home(cfg: Dict[str, Any]) -> None:
    """Home page: just hero + a very simple overview."""
    render_hero(cfg)

    st.markdown("")
    st.markdown(
        "#### What you will find here"
    )
    st.write(
        "- Projects I’ve built end-to-end.\n"
        "- The skills I use day to day.\n"
        "- Longer-form notes and blog posts."
    )


def render_projects(cfg: Dict[str, Any]) -> None:
    st.markdown('### <span class="section-title">Highlighted <span class="accent">Projects</span></span>', unsafe_allow_html=True)
    st.caption("Selected projects that combine solid engineering with machine learning impact.")

    projects = cfg.get("projects", [])
    if not projects:
        st.info("Add your projects in `config.yaml` under the `projects` section.")
        return

    # One project per row, with optional image on the right
    for project in projects:
        st.markdown('<div class="project-card">', unsafe_allow_html=True)
        col_left, col_right = st.columns([2.3, 1])

        with col_left:
            st.markdown(
                f"<div class='project-title'>{project.get('name', 'Untitled Project')}</div>",
                unsafe_allow_html=True,
            )
            if project.get("tagline"):
                st.markdown(
                    f"<div class='project-tagline'>{project['tagline']}</div>",
                    unsafe_allow_html=True,
                )

            if project.get("description"):
                st.markdown(
                    f"<div class='project-description'>{project['description']}</div>",
                    unsafe_allow_html=True,
                )

            tech_stack = project.get("tech_stack", [])
            if tech_stack:
                st.markdown("**Tech stack**")
                st.markdown(
                    " ".join(
                        f"<span class='pill'>{t}</span>" for t in tech_stack
                    ),
                    unsafe_allow_html=True,
                )

            metrics = project.get("metrics", [])
            if metrics:
                st.markdown("**Key metrics & results**")
                for m in metrics:
                    st.write(f"- {m}")

            links = project.get("links", {})
            buttons: List[tuple[str, str]] = []
            demo_url = links.get("demo")
            github_url = links.get("github")
            docs_url = links.get("docs")
            if demo_url:
                buttons.append(("Live Demo", demo_url))
            if github_url:
                buttons.append(("GitHub", github_url))
            if docs_url:
                buttons.append(("Docs", docs_url))

            if buttons:
                btn_cols = st.columns(len(buttons))
                for col, (label, url) in zip(btn_cols, buttons):
                    with col:
                        st.link_button(label, url, use_container_width=True)

        with col_right:
            if project.get("image"):
                st.image(project["image"], use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)


def render_skills(cfg: Dict[str, Any]) -> None:
    st.markdown('### <span class="section-title">Skills <span class="accent">Matrix</span></span>', unsafe_allow_html=True)
    st.caption("What I’m comfortable using to ship ML and AI systems.")

    skills = cfg.get("skills", {})
    if not skills:
        st.info("Define your skills matrix in `config.yaml` under the `skills` section.")
        return

    for category_name, category in skills.items():
        st.subheader(category_name)
        items: List[Dict[str, Any]] = category.get("items", []) if isinstance(
            category, dict
        ) else category

        if not items:
            continue

        cols = st.columns(3)
        for i, skill in enumerate(items):
            with cols[i % len(cols)]:
                label = skill.get("name") if isinstance(skill, dict) else str(skill)
                level = skill.get("level") if isinstance(skill, dict) else None
                years = skill.get("years") if isinstance(skill, dict) else None

                st.markdown(f"<div class='skill-name'>{label}</div>", unsafe_allow_html=True)
                details: List[str] = []
                if level:
                    details.append(level)
                if years:
                    details.append(f"{years}+ yrs")
                if details:
                    st.markdown(
                        f"<div class='skill-meta'>{' • '.join(details)}</div>",
                        unsafe_allow_html=True,
                    )
                # Simple visual indicator based on level
                if level:
                    level_lower = level.lower()
                    if "expert" in level_lower:
                        progress = 0.95
                    elif "advanced" in level_lower:
                        progress = 0.8
                    elif "intermediate" in level_lower:
                        progress = 0.6
                    else:
                        progress = 0.4
                    st.progress(progress)


def render_contact(cfg: Dict[str, Any]) -> None:
    st.markdown('### <span class="section-title">Let’s <span class="accent">Connect</span></span>', unsafe_allow_html=True)
    contact = cfg.get("contact", {})

    email = contact.get("email")
    location = contact.get("location")
    availability = contact.get("availability")
    calendly = contact.get("calendly")
    phone_1 = contact.get("phone_1")
    phone_2 = contact.get("phone_2")

    col1, col2 = st.columns(2)

    with col1:
        if email:
            st.markdown(f"**Email:** [{email}](mailto:{email})")
        if location:
            st.markdown(f"**Location:** {location}")
        if availability:
            st.markdown(f"**Availability:** {availability}")
        if phone_1 or phone_2:
            st.markdown("**Phone:**")
            if phone_1:
                st.write(phone_1)
            if phone_2:
                st.write(phone_2)

    with col2:
        if calendly:
            st.markdown(f"**Book a call:** [{calendly}]({calendly})")
        st.markdown(
            "You can also reach out via any of the social links in the sidebar."
        )


@st.cache_data(ttl=3600)  # Cache for 1 hour
def fetch_readme_content(url: str) -> str:
    """Fetch README content from a URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        return f"Error fetching content: {str(e)}"


def render_blog(cfg: Dict[str, Any]) -> None:
    st.markdown('### <span class="section-title">Writing & <span class="accent">Notes</span></span>', unsafe_allow_html=True)
    st.caption("Deep dives into projects, MLOps, and AI systems thinking.")

    posts = cfg.get("blog_posts", [])
    if not posts:
        st.info("Add blog posts in `config.yaml` under `blog_posts` (optional).")
        return

    titles = [post.get("title", "Untitled post") for post in posts]

    # Simple structure: choose article from a dropdown, then show full content
    selected_title = st.selectbox("Select an article", titles, index=0)

    selected_post = next(
        (p for p in posts if p.get("title") == selected_title), posts[0]
    )
    title = selected_post.get("title", "Untitled post")
    date = selected_post.get("date")
    tags = selected_post.get("tags", [])
    
    # Check if we have readme_path or content
    readme_path = selected_post.get("readme_path")
    content = selected_post.get("content") or selected_post.get("summary", "")
    
    # If readme_path is provided, fetch content from URL
    if readme_path:
        with st.spinner("Loading content..."):
            content = fetch_readme_content(readme_path)

    st.subheader(title)

    meta: List[str] = []
    if date:
        meta.append(date)
    if tags:
        meta.append(", ".join(f"`{t}`" for t in tags))
    if meta:
        st.caption(" • ".join(meta))

    if content:
        st.markdown(f"<div class='blog-content'>{content}</div>", unsafe_allow_html=True)

    # Show a very small "Other articles" list below
    if len(posts) > 1:
        st.markdown("---")
        st.markdown("#### Other articles")
        for post in posts:
            if post.get("title") == selected_title:
                continue
            st.markdown(f"- {post.get('title', 'Untitled post')}")



def main() -> None:
    cfg = load_config()

    st.set_page_config(
        page_title=cfg.get("profile", {}).get(
            "page_title", "AI/ML Engineer Portfolio"
        ),
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    inject_global_styles()

    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Go to",
        ["Home", "Projects", "Skills", "Blog", "Contact"],
        index=0,
    )

    if page == "Home":
        render_home(cfg)
    elif page == "Projects":
        render_projects(cfg)
    elif page == "Skills":
        render_skills(cfg)
    elif page == "Blog":
        render_blog(cfg)
    elif page == "Contact":
        render_contact(cfg)


if __name__ == "__main__":
    main()

