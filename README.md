# 🎬 ALGO-Visualizer

An intelligent, self-healing system that transforms static pseudocode into dynamic **Manim** animations using **Google Gemini AI**.

---

## 📖 Overview

**ALGO-Visualizer** bridges the gap between abstract computer science theory and visual understanding. Students often struggle to mentally map static pseudocode to dynamic processes such as sorting and searching algorithms.

This tool allows users to input any pseudocode (via **text or image**) along with a **custom dataset**. It uses a **Large Language Model (Google Gemini)** to intelligently generate a Python script using the **Manim animation engine**, producing animated algorithm visualizations automatically.

---

## 🌟 Core Innovation: *Self-Healing Architecture*

Unlike standard AI code generators that frequently output buggy or unrenderable code, **ALGO-Visualizer** introduces an **Iterative Refinement Loop**:

1. **Generate** – The AI writes an initial Manim animation script using a DSPy-inspired master prompt.  
2. **Validate** – The system attempts to render the animation.  
3. **Self-Correction** – If rendering fails (syntax error, logic bug, runtime crash, infinite loop), the error logs are captured.  
4. **Refine** – The error details are fed back to the AI with instructions to correct its own code.  
5. **Result** – The loop continues until a fully valid, successfully rendered animation is produced.

This ensures every final output video is **flawless and executable** without user debugging.

---

## 🎥 Demo

https://github.com/user-attachments/assets/8cee3b84-a503-43be-b3b4-437ce634b4ec

Example: A user inputs **Quick Sort pseudocode** along with a custom array and instantly receives a verified animated visualization.

---

## 📂 Project Resources & Presentation

https://drive.google.com/drive/folders/1Z1KVi4dY7zL56lCByMXNEaUyIYbO8gFb?usp=sharing

---

## ✨ Key Features

- **🤖 AI-Powered Generation**  
  Converts natural language pseudocode into detailed Python + Manim animation scripts.

- **🔄 Automated Refinement Loop**  
  Detects rendering errors and automatically fixes the code without any user intervention.

- **📷 Multi-Modal Input**  
  Accepts **text pseudocode** or **uploaded images** (handled using OCR and vision input).

- **🔢 Custom Data Arrays**  
  Visualize algorithms using your own numbers instead of random or preset datasets.

- **🆚 Comparison Mode**  
  Run two algorithms side-by-side to compare behavior and performance  
  *(e.g., Bubble Sort vs. Quick Sort).*

- **🎨 Polished UI**  
  Built using **Streamlit** for a clean, responsive web interface with instant video playback.

---

## 🛠️ Technology Stack

| Component | Technology | Description |
|----------|-------------|---------------|
| **Frontend** | Streamlit | Interactive web interface for user input and animations |
| **Animation Engine** | Manim Community | Programmatic animation engine |
| **Intelligence** | Google Gemini API | LLM for script generation and self-correction |
| **Backend** | Python | Orchestrates validation and refinement loops |
| **Architecture** | DSPy-Inspired | Structured prompting with iterative feedback |

---

## 🚀 Installation & Setup

Follow the steps below to run the project locally.

---

### ✅ Prerequisites

- **Python 3.9+**
- **FFmpeg** (required for Manim rendering)

**Install FFmpeg**

- **Windows:** Download FFmpeg and add it to your system PATH  
- **macOS:**
  ```bash
  brew install ffmpeg
Linux: 
  sudo apt install ffmpeg
Google AI Studio API Key

git clone https://github.com/YOUR_USERNAME/algo-visualizer.git
cd algo-visualizer

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt

GOOGLE_API_KEY = "YOUR_ACTUAL_API_KEY_HERE"

streamlit run app_streamlit.py

# Project Structure
  algo-visualizer/
  
  ├── app_streamlit.py        # Main Streamlit web interface
  
  ├── dspy_master_prompt.py  # Master prompt and Gemini interaction
  
  ├── manim_runner.py        # Script execution, rendering, and error capture
  
  ├── json_response_fixer.py # Utility to repair malformed AI JSON output
  
  ├── requirements.txt       # Python dependencies
  
  └── README.md              # Documentation
  
# Contributors
  Tushar Kant – Developer
  
  Akshay Bachu – Developer

# Acknowledgement
  Special thanks to Anshul Thakur and Prof. Pallavi Jain for their mentorship and guidance in evolving this system from a simple prompt pipeline into a powerful self-healing iteration architecture.
