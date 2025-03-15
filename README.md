# Hugging Face Uploader

## Running on Linux without Python and a virtual environment installation

Replace the text inside the angle brackets, including the brackets, with the appropriate strings

```bash
   cd uploader
   ./uploader </path/to/my_model> <HF_username/HF_repo> --token <HF_token>
   ```

## Create and Activate a Virtual Environment
For Linux/Mac:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
For Windows:
   ```bash
   python3 -m venv .venv
   .venv\Scripts\activate
   ```

All subsequent commands are provided for Linux/Mac OS. For Windows, please replace ```source .venv/bin/activate``` with ```.venv\Scripts\activate```.

Run the following command to install the project dependencies:
```bash
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

User access token generation with write permission: https://huggingface.co/docs/hub/en/security-tokens

Use case:
```
python -m ab.hf.uploader </path/to/my_model> <HF_username/HF_repo> --token <HF_token>
```
