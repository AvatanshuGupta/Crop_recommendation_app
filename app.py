import gradio as gd
import requests
import os
def fetch_prediction(n, p, k, temp, humidity, ph, rainfall):
    API_URL="https://crop-recommendation-api-latest.onrender.com/predict"
    payload = {
        "n": int(n),
        "p": int(p),
        "k": int(k),
        "temp": float(temp),
        "humidity": float(humidity),
        "ph": float(ph),
        "rainfall": float(rainfall)
    }
    try:
        result=requests.post(url=API_URL,json=payload)
        result.raise_for_status()
        if result.status_code == 200:
            return result.json()["prediction"]
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"



with gd.Blocks() as demo:
    gd.HTML("<h1 style='font-size:60px; text-align:center; color:red;'>Crop Recommendation App</h1>")
    gd.Markdown("<h2 style='color:blue; font-size:45px' >Please fill in the soil and weather details below.<h2>") 
    gd.HTML("""
    <style>
    body, .gradio-container {
        background-image: url('https://images6.alphacoders.com/341/341895.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    """)


    with gd.Row():
        n = gd.Number(label="Nitrogen Content", precision=0, minimum=0, maximum=100,value=None,placeholder="Enter Nitrogen Content")
        p = gd.Number(label="Phosphorous Content", precision=0, minimum=0, maximum=100,value=None,placeholder="Enter Phosphorous Content")
        k = gd.Number(label="Potassium Content", precision=0, minimum=0, maximum=100,value=None,placeholder="Enter Potassium Content")
    
    with gd.Row():
        temp = gd.Number(label="Temperature (°C)", minimum=0, maximum=65,value=None,placeholder="Enter Temperature")
        humidity = gd.Number(label="Humidity (%)", minimum=0, maximum=100,value=None,placeholder="Enter Humidity percent")
    
    with gd.Row():
        ph = gd.Number(label="pH of Soil", minimum=0, maximum=14,value=None,placeholder="Enter Ph of soil")
        rainfall = gd.Number(label="Rainfall (cm)", minimum=0,value=None,placeholder="Enter rainfall in cm")
    submit_button=gd.Button("Get recommended crop")
    output=gd.Textbox(label="Recommended Crop")
    
    submit_button.click(
        fetch_prediction,
        inputs=[n,p,k,temp,humidity,ph,rainfall],
        outputs=output
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 7860))
    demo.launch(server_name="0.0.0.0" if port != 7860 else "127.0.0.1", server_port=port)

