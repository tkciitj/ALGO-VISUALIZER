import streamlit as st
import subprocess
import os
import shutil
import google.generativeai as genai

# ----------------------------
# Streamlit Page Config
# ----------------------------
st.set_page_config(layout="wide", page_title="Algo Visualizer")

st.title("🎥 Algo Visualizer")

# ----------------------------
# Gemini API Setup
# ----------------------------
API_KEY = "AIzaSyAc3jwtgdU9LasAIf6Wl4uc99lf4-HEZIU"
genai.configure(api_key=API_KEY)

# ----------------------------
# User Inputs
# ----------------------------
array_input = st.text_input("Enter array:", "8,3,1,7,0,10,2")
pseudo_input = st.text_area("Paste pseudo-code:", height=250)
refine_loops = st.slider("Gemini refinement loops:", 1, 3, 1)
run_btn = st.button("Generate Animation")

output_area = st.empty()

# ----------------------------
# Main Execution
# ----------------------------
if run_btn:

    # ----------------------------
    # Parse Array
    # ----------------------------
    try:
        arr = [int(x.strip()) for x in array_input.split(",")]
    except:
        st.error("Invalid array! Please enter numbers separated by commas.")
        st.stop()

    if pseudo_input.strip() == "":
        st.error("Pseudo-code required!")
        st.stop()

    model = genai.GenerativeModel("gemini-2.5-pro")

    # ----------------------------
    # Base Prompt
    # ----------------------------
    base_prompt = f"""
Generate a complete **Manim Community v0.19.0** Python script that visualizes
the algorithm described in the pseudo-code and uses the input array.

STRICT RULES:
- Output ONLY Python code (no backticks).
- Must contain exactly ONE scene class named: AlgorithmVisualization
- Do NOT use Code() block under any circumstances.
- Use only simple objects: Text, Rectangle, Square, Circle, VGroup, arrows.
- Must follow pseudo-code EXACTLY in logic.
- No custom fonts.
- No extra classes.
- Must be fully compatible with Manim Community v0.19.0.
- No syntax that exists only in newer Manim versions.

Pseudo-code:
{pseudo_input}

Array:
{arr}

Return **only** the Python Manim script.
"""

    # ----------------------------
    # Initial Generation
    # ----------------------------
    with st.spinner("Generating initial Manim script using Gemini…"):
        r = model.generate_content(base_prompt)
        manim_code = r.text.strip().replace("```python", "").replace("```", "").strip()

    # ----------------------------
    # Refinement Loops
    # ----------------------------
    for i in range(refine_loops):
        refine_prompt = f"""
Refine and correct the following Manim code:

{manim_code}

Rules:
- Return ONLY Python code.
- Keep animation minimal.
- No Code() block.
- No extra classes.
- Strictly compatible with Manim 0.19.0.
- Keep the algorithm logic EXACTLY matching pseudo-code.
"""
        with st.spinner(f"Refinement Loop {i+1}…"):
            rr = model.generate_content(refine_prompt)
            manim_code = rr.text.strip().replace("```python", "").replace("```", "").strip()

    # ----------------------------
    # Save the Script
    # ----------------------------
    with open("generated_manim.py", "w", encoding="utf-8") as f:
        f.write(manim_code)

    st.success("Initial Manim script saved.")

    # ----------------------------
    # DELETE OLD MEDIA DIRECTORY (Key Fix)
    # ----------------------------
    MEDIA_DIR = "./media"
    if os.path.exists(MEDIA_DIR):
        shutil.rmtree(MEDIA_DIR)

    # ----------------------------
    # Render Function
    # ----------------------------
    def render():
        cmd = ["manim", "-ql", "generated_manim.py", "AlgorithmVisualization"]
        return subprocess.run(cmd, capture_output=True, text=True)

    # ----------------------------
    # AUTO ERROR FIX LOOP
    # ----------------------------
    MAX_FIXES = 3
    attempt = 0
    success = False

    while attempt < MAX_FIXES:
        with st.spinner(f"Rendering (Attempt {attempt+1})…"):
            result = render()

        video_path = "media/videos/generated_manim/480p15/AlgorithmVisualization.mp4"

        # success
        if os.path.exists(video_path):
            success = True
            break

        # failed → refine using error logs
        error_text = result.stdout + "\n" + result.stderr

        st.warning(f"Render failed on attempt {attempt+1}. Sending error to Gemini to fix…")

        fix_prompt = f"""
Fix the following Manim code. The rendering failed.

Manim Code:
{manim_code}

Error Log:
{error_text}

Rules:
- Return ONLY corrected Python Manim code.
- Must keep class name: AlgorithmVisualization
- Must follow pseudo-code logic.
- Must be compatible with Manim 0.19.0.
- No Code() block.
"""
        fix_response = model.generate_content(fix_prompt)
        manim_code = fix_response.text.strip().replace("```python", "").replace("```", "").strip()

        # rewrite updated file
        with open("generated_manim.py", "w", encoding="utf-8") as f:
            f.write(manim_code)

        # delete output directory to avoid stale videos
        if os.path.exists(MEDIA_DIR):
            shutil.rmtree(MEDIA_DIR)

        attempt += 1

    # ----------------------------
    # Final Outputs
    # ----------------------------
    if success:
        st.success("🎉 Rendering successful!")
        st.video(video_path)
    else:
        st.error("Rendering failed even after all refinement attempts.")
        st.code(result.stdout + "\n" + result.stderr)
