import os
import sys
import patoolib

def decompress_rar(file_path, output_path):
    """Decompress a RAR file to the specified output directory."""
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    patoolib.extract_archive(file_path, outdir=output_path)

if __name__ == "__main__":
    # Default file and output path, modify as needed
    rar_file_path = 'example.rar'  # Replace with your RAR file path
    output_directory = '.'  # Replace with your desired output directory

    if len(sys.argv) > 1:
        rar_file_path = sys.argv[1]
        if len(sys.argv) > 2:
            output_directory = sys.argv[2]

    decompress_rar(rar_file_path, output_directory)
