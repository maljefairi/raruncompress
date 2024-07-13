# RAR Decompressor for Mac

This Python script allows Mac users to easily decompress RAR files using the `patool` library.

## Requirements

- Python 3.x
- `patool` Python library

## Setup and Installation

### Setting Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies cleanly and avoid conflicts with other Python projects. Here's how to set it up:

1. Navigate to the project directory:
   ```bash
   cd path/to/RAR-Decompressor-for-Mac
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

### Installing Dependencies

Install the required packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

Once the setup is complete, you can use the script to decompress RAR files. Replace `path_to_your_rar_file.rar` with the path to your RAR file and `path_to_extract_to` with the path where you want the files extracted:

```bash
python decompress_rar.py path_to_your_rar_file.rar path_to_extract_to
```

## Deactivating the Virtual Environment

After you're done using the script, you can deactivate the virtual environment:

```bash
deactivate
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.