import boto3

# Initialize Bedrock client
client = boto3.client("bedrock-runtime", region_name="us-east-1")
model_id = "amazon.nova-lite-v1:0"

# Custom system prompt defining the persona
system_prompt = [
    {
        "text": (
            "You are a friendly and enthusiastic cloud computing tutor. "
            "Explain technical concepts using simple analogies and keep explanations engaging."
        )
    }
]

# Tuned inference parameters
inference_config = {
    "temperature": 0.7,   # Creativity & variety
    "topP": 0.9,          # Diversity of word choice
    "maxTokens": 512      # Maximum token limit per response
}

# Conversation history tracking
conversation_history = []

print("Cloud Tutor Chatbot initialized! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    if not user_input:
        continue
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    # Append user prompt to history
    conversation_history.append({
        "role": "user",
        "content": [{"text": user_input}]
    })

    # Invoke Bedrock Converse API with full history, system prompt, and inference configs
    response = client.converse(
        modelId=model_id,
        messages=conversation_history,
        system=system_prompt,
        inferenceConfig=inference_config
    )

    # Extract response message
    assistant_message = response["output"]["message"]
    response_text = assistant_message["content"][0]["text"]
    print(f"\nBot: {response_text}\n")

    # Append assistant's answer to conversation history to maintain context
    conversation_history.append(assistant_message)

