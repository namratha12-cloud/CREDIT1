from huggingface_hub import HfApi, create_repo, upload_folder
import os

api = HfApi()
username = "a-b-15"
repo_id = f"{username}/credit-fraud-detection"

print(f"Creating Space: {repo_id}...")
try:
    create_repo(
        repo_id=repo_id,
        repo_type="space",
        space_sdk="docker",
        private=False,
        exist_ok=True
    )
    print("Space created or already exists.")
except Exception as e:
    print(f"Error creating space: {e}")

# Files to upload: app.py, requirements.txt, Dockerfile, models/, static/, templates/
print("Uploading files...")
try:
    # We'll upload the folder contents, excluding large/unnecessary files
    # The current directory is the root
    upload_folder(
        repo_id=repo_id,
        repo_type="space",
        folder_path=".",
        ignore_patterns=[
            "creditcard.csv",
            "train_model.py",
            "deploy_hf.py",
            "*.md",
            ".git*",
            "venv",
            "__pycache__",
            "*.pyc"
        ]
    )
    print(f"Deployment successful! Link: https://huggingface.co/spaces/{repo_id}")
except Exception as e:
    print(f"Error uploading files: {e}")
