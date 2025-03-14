import argparse
import getpass

from huggingface_hub import HfApi, create_repo


def upload_local_model_to_huggingface(local_model_path, repo_name, commit_message, token):
    """
    Uploads a locally saved model to Hugging Face Hub using a provided token.

    Args:
        local_model_path: The path to the directory containing the saved model files.
        repo_name: The desired repository name (e.g., "your_username/my_model").
        commit_message: The commit message for the upload.
        token: Hugging Face authentication token.
    """

    api = HfApi(token=token)

    # Check if the repo exists, if not create it.
    try:
        api.repo_info(repo_id=repo_name)
    except:
        create_repo(repo_id=repo_name, repo_type="model", exist_ok=True, token=token)

    try:
        api.upload_folder(
            repo_id=repo_name,
            folder_path=local_model_path,
            commit_message=commit_message,
        )

        print(f"Model uploaded successfully to {repo_name}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload a local model to Hugging Face Hub.")
    parser.add_argument("local_model_path", help="Path to the local model directory.")
    parser.add_argument("repo_name", help="Hugging Face repository name (e.g., your_username/my_model).")
    parser.add_argument("--commit_message", default="Upload model", help="Commit message for the upload.")
    parser.add_argument("--token", help="Hugging Face authentication token. If not provided, will prompt for password.")

    args = parser.parse_args()

    token = args.token
    if token is None:
        token = getpass.getpass("Enter your Hugging Face authentication token: ")

    upload_local_model_to_huggingface(args.local_model_path, args.repo_name, args.commit_message, token)