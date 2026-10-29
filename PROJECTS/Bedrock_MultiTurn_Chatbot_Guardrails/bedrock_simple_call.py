import boto3

# Initialize Bedrock Runtime client in us-east-1
client = boto3.client("bedrock-runtime", region_name="us-east-1")
model_id = "amazon.nova-lite-v1:0"

# Single message format expected by Converse API
messages = [
    {
        "role": "user",
        "content": [{"text": "What is cloud computing? Explain in 3 sentences."}]
    }
]

# Send request to Bedrock Converse API
response = client.converse(
    modelId=model_id,
    messages=messages
)

# Extract and display the model's text response
response_text = response["output"]["message"]["content"][0]["text"]
print(response_text)

