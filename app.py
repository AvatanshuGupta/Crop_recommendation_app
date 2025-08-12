import gradio as gr
import random

# Fake AI model logic
def mood_predictor(text, mood_type, intensity):
    moods = {
        "Happy": ["😊", "😄", "😁", "🌞"],
        "Sad": ["😢", "💧", "😔", "🌧️"],
        "Excited": ["🤩", "🎉", "🔥", "✨"],
        "Chill": ["😌", "🌊", "🍵", "🌙"]
    }
    emoji = random.choice(moods[mood_type])
    response = f"**Mood:** {mood_type}\n**Intensity:** {intensity}/10\n**Message:** {text} {emoji * intensity}"
    return response, f"https://source.unsplash.com/800x600/?{mood_type.lower()}"

# Custom CSS for background & animation
custom_css = """
body {
    background-image: url('https://images.unsplash.com/photo-1506744038136-46273834b3fb');
    background-size: cover;
    font-family: 'Poppins', sans-serif;
}

h1 {
    text-align: center;
    animation: fadeIn 2s ease-in-out;
    color: white;
}

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

.gradio-container {
    background-color: rgba(0, 0, 0, 0.6);
    border-radius: 15px;
    padding: 20px;
}
"""

with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as demo:
    gr.Markdown("<h1>🎭 AI Mood Generator</h1>")
    
    with gr.Tab("Text to Mood"):
        with gr.Row():
            text_input = gr.Textbox(label="Enter your message", placeholder="How do you feel today?")
            mood_type = gr.Dropdown(["Happy", "Sad", "Excited", "Chill"], label="Select Mood")
            intensity = gr.Slider(1, 10, value=5, step=1, label="Mood Intensity")
        
        output_text = gr.Markdown()
        output_image = gr.Image(label="Mood Image", type="filepath")
        
        submit_btn = gr.Button("✨ Generate Mood")
        submit_btn.click(mood_predictor, [text_input, mood_type, intensity], [output_text, output_image])
    
    with gr.Tab("Live Mood Updates"):
        gr.Markdown("🎯 Coming soon: Real-time mood tracking!")

demo.launch()
