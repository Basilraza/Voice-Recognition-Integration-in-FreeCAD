# Voice Command Interface for FreeCAD

This Python script allows basic voice control for reading and writing numerical values using speech recognition and text-to-speech (TTS). It demonstrates how to interpret spoken commands and execute FreeCAD GUI commands accordingly.

## 🧠 Features

- Speech recognition using Google's API via `speech_recognition`
- Text-to-speech feedback using `pyttsx3`
- Ability to extract numerical values from spoken commands
- Sample integration with FreeCAD's GUI command (`Gui.runCommand`)
- Support for Indian English (`en-IN`) recognition

---

## 🛠️ Requirements

Make sure the following Python packages are installed:

```bash
pip install SpeechRecognition
pip install pyttsx3
```

You also need:

- A working **microphone**
- `pyaudio` for microphone access (install via `pip install pyaudio`, or use `pipwin install pyaudio` on Windows)
- **FreeCAD** environment if you're using `Gui.runCommand`

---

## ▶️ How to Use

1. Make sure your microphone is connected and working.
2. Run the script:

```bash
python voice_control.py
```

3. You will be prompted:
```
Please give a command:
```

4. Say something like:

```
view 3
```

5. The script extracts the number (`3`) and runs:

```python
Gui.runCommand('Std_ViewGroup', 3)
```

6. It also provides spoken feedback such as:

> "Please give a command"  
> "The value of view is 3"

---

## 🔧 Functions Explained

### `Speech.recognise()`

- Listens to the microphone
- Recognizes voice using Google Speech Recognition
- Converts the result to lowercase text

### `getValue(text)`

- Parses the first numeric value from a string

### `handleRead(text)` / `handleWrite(text)`

- Provide TTS feedback for reading or writing a value

---

## 📌 Notes

- The microphone uses device index 0. Change `device_index=0` in `sr.Microphone()` if needed.
- Make sure your internet is connected, as Google Speech API requires online access.
- `Gui.runCommand()` will only work if this is executed inside a FreeCAD Python console or environment.

---