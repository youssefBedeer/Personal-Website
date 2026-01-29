import yaml
import pathlib

# Read the config file
config_path = pathlib.Path("config.yaml")
with config_path.open("r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# Update blog_posts to use readme_path instead of content
config["blog_posts"] = [
    {
        "title": "Telco Customer Churn Prediction - End-to-End ML Project",
        "date": "2026-01-13",
        "tags": ["ML", "MLOps"],
        "readme_path": "https://raw.githubusercontent.com/youssefBedeer/End-to-End-TelcoChurn/main/README.md"
    },
    {
        "title": "End-to-End Plant Disease Detection System",
        "date": "2025-06-01",
        "tags": ["MLOps", "Computer Vision"],
        "readme_path": "https://raw.githubusercontent.com/youssefBedeer/End-to-End-PlantVillage/main/README.md"
    },
    {
        "title": "End-to-End PDF Q&A System",
        "date": "2025-06-01",
        "tags": ["LLMs", "RAG"],
        "readme_path": "https://raw.githubusercontent.com/youssefBedeer/RAG-End-to-End/main/README.md"
    }
]

# Write back to the file
with config_path.open("w", encoding="utf-8") as f:
    yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

print("Config file updated successfully!")
