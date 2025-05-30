````markdown
# 🎵 convert-audio-m4a-to-mp3

A simple Python script to recursively convert `.m4a` audio files to `.mp3`, replacing the originals and preserving
folder structure. Useful for preparing audio for devices that do not support `.m4a`.

---

## ✅ Features

- Recursively scans folders and subfolders
- Converts `.m4a` files to `.mp3` using `pydub` and `ffmpeg`
- Replaces original files (deletes `.m4a` after conversion)
- Prompts user to select target folder on launch
- Customizable MP3 bitrate (default: 192k)

---

## 🚀 Requirements

- Python 3.7+
- [ffmpeg](https://ffmpeg.org/) (must be in system PATH)
- `pydub` Python library

---

## 🛠 Installation

1. **Install Python packages**:

```bash
pip install pydub
````

2. **Install ffmpeg** (on Windows via [Chocolatey](https://chocolatey.org/install)):

```bash
choco install ffmpeg -y
```

Check installation:

```bash
ffmpeg -version
```

---

## ▶️ Usage

Run the script via terminal:

```bash
python convert.py
```

You will be prompted:

```
Enter the path to the folder with .m4a files:
```

Provide the path, and the script will start converting files.

---

## 🧪 Example

If your folder contains:

```
C:\Music
├── song1.m4a
├── Album\
│   ├── track2.m4a
```

After running the script, it will contain:

```
C:\Music
├── song1.mp3
├── Album\
│   ├── track2.mp3
```

And `.m4a` files will be deleted.

---

## 💡 Notes

* Bitrate can be adjusted by modifying the script (`bitrate="192k"`)
* Script skips non-`.m4a` files silently
* Compatible with `.m4a` files encoded with AAC or ALAC

---

## 📄 License

MIT License

---

## 📬 Author

Made with ❤️ by Yevhen Kulyk
---