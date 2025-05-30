import os
from pydub import AudioSegment


def convert_m4a_to_mp3(root_folder: str, bitrate: str = "192k") -> None:
    """
    Recursively convert all .m4a files in the given folder and subfolders to .mp3,
    replacing the original files.

    Args:
        root_folder (str): Path to the root directory to search for .m4a files.
        bitrate (str): Bitrate for the output .mp3 files (default is "192k").
    """
    if not os.path.isdir(root_folder):
        print(f"❌ The folder does not exist: {root_folder}")
        return

    # Walk through all subdirectories and files
    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.lower().endswith(".m4a"):
                m4a_path = os.path.join(dirpath, filename)
                mp3_path = os.path.splitext(m4a_path)[0] + ".mp3"

                try:
                    print(f"🎧 Converting: {m4a_path} → {mp3_path}")
                    audio = AudioSegment.from_file(m4a_path, format="m4a")
                    audio.export(mp3_path, format="mp3", bitrate=bitrate)
                    os.remove(m4a_path)
                    print(f"✅ Done. Deleted original file: {m4a_path}")
                except Exception as e:
                    print(f"❌ Error processing {m4a_path}: {e}")


def main():
    """
    Entry point of the script. Prompts the user to input a folder path.
    """
    folder = input("Enter the path to the folder with .m4a files: ").strip()
    convert_m4a_to_mp3(folder)


if __name__ == "__main__":
    main()
