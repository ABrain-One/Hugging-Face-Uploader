# Hugging Face Uploader

To use this Hugging Face uploader, you’ll need a user access token with write permissions. If you don’t have one, you can easily generate it by following the instructions at https://huggingface.co/docs/hub/en/security-tokens

## Running on Linux without Python and a Virtual Environment

Replace the text inside the angle brackets, including the brackets, with the appropriate strings

```bash
   cd uploader
   ./uploader </path/to/my_model> <HF_username/HF_repo> --token <HF_token>
   ```

## Running Python Script in a Virtual Environment

Create and activate a virtual environment.

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

Upload your model to Hugging Face (replace the text inside the angle brackets, including the brackets, with the appropriate strings):
```
python -m ab.hf.uploader </path/to/my_model> <HF_username/HF_repo> --token <HF_token>
```
