import requests

url = "http://localhost:9696/predict"
client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}
conv_res = requests.post(url, json=client).json()

print("Probability of being converted: ", conv_res)
