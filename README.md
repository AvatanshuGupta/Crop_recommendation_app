# Crop Recommendation App

This is a simple interactive web app built with **Gradio** that recommends the best crop to plant based on soil and weather parameters. The app takes inputs like Nitrogen, Phosphorous, Potassium levels, temperature, humidity, pH, and rainfall, then sends this data to a prediction API and displays the recommended crop.

---

## Features

- User-friendly UI with input fields for soil nutrients and weather conditions
- Input validation with min/max ranges and placeholders
- Background image and styled headers for better UX
- Integration with a REST API for real-time crop recommendation
- Error handling for API request failures

---

## Tech Stack

- Python 3.x
- [Gradio](https://gradio.app/) for the frontend UI
- REST API endpoint hosted at `https://crop-recommendation-api-latest.onrender.com/predict` 

