# Hugging-Face-Uploader


## Create and Activate a Virtual Environment (recommended)
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
python -m ab.hf.uploader </path/to/my_model> --token <HF_token>
```
