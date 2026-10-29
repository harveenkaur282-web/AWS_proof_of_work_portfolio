# AWS Proof-of-Work Portfolio

A curated, evidence-led portfolio of hands-on work with **AWS infrastructure, serverless systems, and agentic AI**, built alongside my core AI/ML and software engineering projects as I prepare for **AWS Cloud and Cloud-AI internships**.

> Completed implementations, work in progress, and training/workshop material are labelled separately. Follow each repository for code, architecture, setup notes, screenshots, and evaluation evidence.

## Cloud & AWS Projects

### 1. Customer Support AI Agent — Amazon Bedrock AgentCore
**Repository:** [ai-support-agent](https://github.com/harveenkaur282-web/ai-support-agent) · **Status: Deployed; six end-to-end tests documented**

A deployed support agent built with the Strands Agents SDK and Bedrock AgentCore. It handles order tracking, refund processing, policy/product Q&A with RAG, cross-session customer memory, loyalty calculations in a code sandbox, and live-page reading through a browser tool. The repository includes architecture, screenshots, six test outcomes, and troubleshooting notes.

**AWS stack:** Bedrock AgentCore Runtime, Gateway, Memory, Code Interpreter and Browser; Bedrock Knowledge Bases; Amazon Nova; OpenSearch Serverless; Lambda; API Gateway; S3; IAM; CloudWatch.

*Built as part of the Udacity Future AWS Agent Engineer Nanodegree.*

### 2. Static Website Hosting with Amazon S3 and CloudFront
**Repository:** [Website-Hosting-with-Amazon-S3-and-CloudFront](https://github.com/harveenkaur282-web/Website-Hosting-with-Amazon-S3-and-CloudFront)

Hosts static assets in a private S3 bucket and delivers them through CloudFront over HTTPS, using Origin Access Control (OAC) and a bucket policy to restrict direct bucket access.

**AWS concepts:** S3, CloudFront, OAC, bucket policies, IAM and CDN fundamentals.

### 3. Serverless Text-to-Speech with Amazon Polly
**Repository:** [aws-polly-text-to-speech](https://github.com/harveenkaur282-web/aws-polly-text-to-speech)

A Python serverless workflow that processes text with Amazon Polly through Lambda, with CloudWatch logs for troubleshooting.

**AWS services:** Lambda, Amazon Polly, CloudWatch and IAM.

### 4. EC2 Web Application Setup
**Documentation index:** [AWS portfolio repository](https://github.com/harveenkaur282-web/AWS_proof_of_work_portfolio)

A hands-on web-app setup documented in the Projects section of this portfolio repository, covering practical EC2 deployment and configuration. See the repository's step-by-step guide for implementation details.



### 5. Multi-Turn AI Chatbot with Amazon Bedrock, Nova 2 Lite & Guardrails
**Documentation & Code:** [Bedrock Multi-Turn Chatbot](PROJECTS/Bedrock_MultiTurn_Chatbot_Guardrails) · [Project Report (PDF)](PROJECTS/Bedrock_MultiTurn_Chatbot_Guardrails/Build_an_AI_Chatbot_with_Amazon_Bedrock.pdf)

A terminal-based conversational AI chatbot built with Python, Boto3, and the Bedrock Converse API in AWS CloudShell. Features multi-turn conversational context, customizable tutor personality via system prompts, inference parameter tuning (`temperature`, `top_p`, `max_tokens`), and Responsible AI content safety enforcement using Bedrock Guardrails.

**AWS concepts:** Amazon Bedrock Runtime, Amazon Nova 2 Lite, Converse API, Bedrock Guardrails, CloudShell, Boto3 SDK, prompt engineering.

## In Progress 

### Multi-Agent E-commerce RAG on AWS
**Repository:** [Multi-Agent-Ecommerce-RAG](https://github.com/harveenkaur282-web/Multi-Agent-Ecommerce-RAG) · **Status: In progress**

A multi-agent customer-support workflow with an orchestrator and specialist agents for inventory, policy retrieval, refund eligibility, and customer-facing responses. The developing architecture includes RAG across three Bedrock Knowledge Bases, DynamoDB, AgentCore Runtime, Guardrails, session memory, and CloudWatch/X-Ray observability. This project is still in progress; see its repository for current implementation status.

**AWS stack:** Bedrock AgentCore, Strands Agents SDK, Bedrock Knowledge Bases, DynamoDB, S3, Guardrails, CloudWatch and AWS X-Ray.

## AWS Training & Learning

- [Getting Started with Amazon Bedrock — AWS Skill Builder](https://skillbuilder.aws/learn/63KTRM86DQ/amazon-bedrock-getting-started/SC2Y3HMAUE)
- [Fundamentals of Generative AI — AWS Skill Builder](https://skillbuilder.aws/learn/FKXM21R555/fundamentals-of-generative-ai/ZFX96NREH4)
- **Udacity Future AWS Agent Engineer Nanodegree:** hands-on agent engineering work, including the deployed support agent above.
- [Strands Agents + Bedrock AgentCore workshop](https://github.com/harveenkaur282-web/sample-strands-agents-hands-on-workshop) — listed as workshop/learning material rather than an original end-to-end project.

## Related Cloud-Native Engineering

### CloudCart — Cloud-Native Microservices Platform
**Repository:** [cloud-native-microservices-app](https://github.com/harveenkaur282-web/cloud-native-microservices-app)

An e-commerce platform with a Next.js dashboard, FastAPI gateway, domain microservices, PostgreSQL database-per-service, Docker Compose, and Kubernetes/NGINX Ingress manifests. This demonstrates containerization and orchestration; it is **not presented as an AWS deployment** unless separately deployed there.

## Skills Practiced

- **AWS infrastructure:** EC2, S3, CloudFront, IAM, CloudWatch
- **Serverless and APIs:** Lambda, API Gateway, DynamoDB
- **AWS AI/agents:** Bedrock, AgentCore Runtime/Gateway/Memory, Knowledge Bases, Guardrails
- **RAG and observability:** OpenSearch Serverless, retrieval workflows, CloudWatch, X-Ray
- **Cloud-native development:** Python, Docker, Kubernetes, microservices, API integration
- **Engineering practices:** architecture documentation, end-to-end testing, logs and troubleshooting

## Contact

- [GitHub profile](https://github.com/harveenkaur282-web)
- [LinkedIn](https://www.linkedin.com/in/harveen-k-ab8347355)
