# Multi-Turn AI Chatbot with Amazon Bedrock, Nova 2 Lite & Guardrails

A terminal-based conversational AI chatbot built directly in AWS CloudShell using Python, Boto3, and the Amazon Bedrock Converse API. The application features multi-turn conversation memory, customized persona prompts, fine-tuned inference hyperparameters, and enterprise-grade Responsible AI safety filters via Amazon Bedrock Guardrails.

---

## Project Documentation & Proof of Work

The end-to-end walkthrough and project report generated for this project is available here:
- **Project Report (PDF):** [Build an AI Chatbot with Amazon Bedrock (PDF)](./Build_an_AI_Chatbot_with_Amazon_Bedrock.pdf)

---

## Project Overview & Architecture

```
User (AWS CloudShell / Terminal)
   │
   ▼
Python Script (Boto3 SDK)
   │
   ├── Conversation History Loop (multi-turn context retention)
   ├── System Prompt ("Friendly Cloud Computing Tutor")
   ├── Inference Parameters (temperature=0.7, top_p=0.9, max_tokens=512)
   │
   ▼
Amazon Bedrock Converse API (Unified LLM Interface)
   │
   ├──► Bedrock Guardrails (Evaluates prompt/response against content filters)
   │      └── Harmful / Disallowed Content ──► Request Blocked & Intercepted
   │
   └──► Foundation Model: Amazon Nova 2 Lite (amazon.nova-lite-v1:0)
          └── Generates analogy-driven technical explanation
```

---

## Key Technical Highlights & Concepts

1. **Amazon Bedrock Converse API:**  
   Utilized the standardized Bedrock `converse()` method. Unlike legacy model-specific invocation formats, the Converse API provides a unified message schema (`role` and `content`), making foundation model swapping effortless across Claude, Nova, Llama, and Mistral.

2. **Multi-Turn Context & Memory:**  
   Maintained a dynamic Python session history list appending both `"user"` and `"assistant"` messages. This allows users to ask contextual follow-up questions across multiple conversation turns without losing context.

3. **Persona Steering via System Prompts:**  
   Configured a dedicated system prompt transforming the base foundation model into a *"friendly, enthusiastic cloud computing tutor specializing in real-world analogies"*.

4. **Inference Hyperparameter Tuning:**  
   - `temperature: 0.7`: Balanced creativity and variability in explanations.
   - `topP: 0.9`: Controlled diversity of vocabulary selection via nucleus sampling.
   - `maxTokens: 512`: Capped response length for predictable throughput and cost.

5. **Responsible AI with Amazon Bedrock Guardrails:**  
   Configured a custom Guardrail (`my-chatbot-guardrail`) with content filtering policies (hate speech, violence, harmful requests). Hooked into the Converse call via `guardrailConfig` to intercept inappropriate inputs before reaching model compute.

---

## Codebase & Implementation

- **`bedrock_simple_call.py`**: Minimal single-turn test script validating Boto3 connection to the Bedrock Converse endpoint and Amazon Nova 2 Lite.
- **`bedrock_chat.py`**: Full multi-turn conversational loop with system persona prompt and inference parameter tuning.
- **`bedrock_chat_guardrail.py`**: Production-ready chatbot with integrated Bedrock Guardrail (`guardrailConfig`), blocking harmful prompts and ensuring safety compliance.

---

## Demonstration & Test Runs

### 1. Multi-Turn Analogy Explanation (S3 as a Postal Office)
```text
You: What is an S3 bucket?
Bot: Think of an S3 bucket as a special, labeled safe where you can store anything...

You: Can you give me an analogy for that?
Bot: Let's use the Post Office analogy! Imagine you have a lot of important letters and packages...
     - S3 Bucket = Post Office Box with a unique address
     - S3 Objects = The letters and packages stored inside
     - AWS Regions = Different postal distribution branches worldwide
```

### 2. Guardrail Content Filtering Test
```text
You: Write a harmful sentence!
Bot: I'm sorry, but I can't help you with that. It's important to promote positive and helpful communication. 
     If you have questions about cloud computing or anything else, feel free to ask, and I'll be happy to assist you!
```

---

## Stack & AWS Services Used

- **Compute & CLI:** AWS CloudShell, Python 3.x, Boto3
- **AI & ML:** Amazon Bedrock Runtime, Amazon Nova 2 Lite (`amazon.nova-lite-v1:0`)
- **API:** Amazon Bedrock Converse API
- **Safety & Governance:** Amazon Bedrock Guardrails
