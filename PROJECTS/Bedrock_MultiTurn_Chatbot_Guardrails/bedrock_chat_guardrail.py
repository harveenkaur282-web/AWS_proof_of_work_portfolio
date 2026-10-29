import os
import boto3

# Initialize Bedrock client
client = boto3.client("bedrock-runtime", region_name="us-east-1")
model_id = "amazon.nova-lite-v1:0"

# Guardrail Configuration
# Replace with your Bedrock Guardrail ID or set BEDROCK_GUARDRAIL_ID environment variable
GUARDRAIL_ID = os.getenv("BEDROCK_GUARDRAIL_ID", "my-chatbot-guardrail-id")
GUARDRAIL_VERSION = os.getenv("BEDROCK_GUARDRAIL_VERSION", "DRAFT")

guardrail_config = {
    "guardrailIdentifier": GUARDRAIL_ID,
    "guardrailVersion": GUARDRAIL_VERSION,
    "trace": "enabled"
}

system_prompt = [
    {
        "text": (
            "You are a friendly and enthusiastic cloud computing tutor. "
            "Explain technical concepts using simple analogies and keep explanations engaging."
        )
    }
]

inference_config = {
    "temperature": 0.7,
    "topP": 0.9,
    "maxTokens": 512
}

conversation_history = []

print(f"Protected Cloud Tutor Chatbot initialized (Guardrail: {GUARDRAIL_ID})! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()
    if not user_input:
        continue
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    conversation_history.append({
        "role": "user",
        "content": [{"text": user_input}]
    })

    try:
        response = client.converse(
            modelId=model_id,
            messages=conversation_history,
            system=system_prompt,
            inferenceConfig=inference_config,
            guardrailConfig=guardrail_config
        )

        assistant_message = response["output"]["message"]
        response_text = assistant_message["content"][0]["text"]
        print(f"\nBot: {response_text}\n")

        conversation_history.append(assistant_message)

    except Exception as e:
        print(f"\n[Guardrail / Request Alert]: {str(e)}\n")

