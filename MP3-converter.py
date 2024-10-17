from moviepy.editor import AudioFileClip
import os
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# CHANGE THE FOLDERS PATH # 
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ # 
INPUT_FOLDER = r"C:\Users\PATH\Desktop\f"  # Path to the folder with .m4a files
OUTPUT_FOLDER = r"C:\Users\PATH\Desktop\c"  # Path to the folder where converted .mp3 files will be saved
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ #

def create_output_folder(folder):
    """Create the output folder if it doesn't exist."""
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"{Fore.CYAN}[INFO] Created output folder: {folder}")

def convert_m4a_to_mp3(input_folder, output_folder):
    """Convert .m4a files to .mp3 format."""
    files_converted = 0
    m4a_files = [f for f in os.listdir(input_folder) if f.endswith(".m4a")]
    total_files = len(m4a_files)

    # Loop through each file in the input folder
    for filename in m4a_files:
        m4a_path = os.path.join(input_folder, filename)
        mp3_path = os.path.join(output_folder, filename.replace(".m4a", ".mp3"))

        try:
            # Load and convert the m4a file to mp3
            audio = AudioFileClip(m4a_path)
            audio.write_audiofile(mp3_path)
            files_converted += 1
            print(f"{Fore.GREEN}[SUCCESS] Converted: {filename} to mp3")
        except Exception as e:
            print(f"{Fore.RED}[ERROR] Error converting {filename}: {e}")

    return files_converted, total_files

def list_remaining_files(folder):
    """List remaining .m4a files in the input folder."""
    remaining_files = [f for f in os.listdir(folder) if f.endswith(".m4a")]
    return remaining_files

def main():
    """Main function to run the conversion process."""
    print(f"{Fore.MAGENTA}=== M4A to MP3 Converter ===\n")
    create_output_folder(OUTPUT_FOLDER)

    # Perform conversion
    files_converted, total_files = convert_m4a_to_mp3(INPUT_FOLDER, OUTPUT_FOLDER)

    # Re-check remaining .m4a files after conversion attempt
    remaining_files = list_remaining_files(INPUT_FOLDER)

    # Display summary
    print(f"\n{Fore.BLUE}=== Conversion Summary ===")
    print(f"Total files to convert: {Fore.YELLOW}{total_files}")
    print(f"Files converted successfully: {Fore.GREEN}{files_converted}")
    print(f"Files remaining: {Fore.RED}{len(remaining_files)}")

    if remaining_files:
        print("\nRemaining .m4a files:")
        for file in remaining_files:
            print(f"{Fore.YELLOW}- {file}")
    else:
        print("\nNo .m4a files remaining.")

    print(f"\n{Fore.MAGENTA}=== Conversion Complete! ===")
    print(f"\n{Fore.RED}== Made By ITzAD20")

    # Wait for user input before closing
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
