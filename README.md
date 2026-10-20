# AWS Proof-of-Work Portfolio

A curated index of my hands-on work with **AWS cloud infrastructure, serverless applications, and AI services**. I’m building this portfolio alongside my AI/ML projects as I prepare for **cloud, cloud engineering, and cloud-AI internships**.

> **Portfolio status:** This repository is an index of projects and learning work. Follow the linked repositories for each project's code, architecture, setup instructions, and available evidence. I distinguish completed implementations from work in progress and workshop exercises.

## Projects

### 1. Static Website Hosting with Amazon S3 and CloudFront
**Repository:** [Website-Hosting-with-Amazon-S3-and-CloudFront](https://github.com/harveenkaur282-web/Website-Hosting-with-Amazon-S3-and-CloudFront)

Demonstrates hosting static website assets in a private S3 bucket and delivering them through CloudFront using Origin Access Control (OAC), with attention to HTTPS delivery and limiting direct access to the bucket.

**AWS concepts:** Amazon S3, Amazon CloudFront, Origin Access Control, bucket policies, IAM/security fundamentals.

### 2. Serverless Text-to-Speech with Amazon Polly
**Repository:** [aws-polly-text-to-speech](https://github.com/harveenkaur282-web/aws-polly-text-to-speech)

A Python-based serverless workflow that accepts text, invokes Amazon Polly for speech synthesis, and uses AWS Lambda for processing. CloudWatch supports logs and troubleshooting.

**AWS services:** AWS Lambda, Amazon Polly, Amazon CloudWatch, IAM.

### 3. Customer Support Chatbot with Amazon Bedrock AgentCore
**Repository:** [Customer-Support-Chatbot-with-Amazon-Bedrock-AgentCore](https://github.com/harveenkaur282-web/Customer-Support-Chatbot-with-Amazon-Bedrock-AgentCore)

A multi-turn support assistant using prompt-based routing and Amazon Nova Pro. It gathers bug-report details across turns, calls a Lambda-backed tool through AgentCore Gateway, and persists submitted tickets in DynamoDB. The README documents baseline and extended edge-case evaluation results.

**AWS services/concepts:** Amazon Bedrock, Bedrock AgentCore, AgentCore Gateway, AWS Lambda, Amazon DynamoDB, AWS CloudFormation, IAM, model evaluation.

### 4. Production-Style AI Support Agent
**Repository:** [ai-support-agent](https://github.com/harveenkaur282-web/ai-support-agent)

**Status: Work in progress / learning project.** This project explores a richer support-agent architecture using the Strands SDK and Bedrock AgentCore, with planned capabilities for tool use, knowledge-base retrieval, cross-session memory, calculations, and web browsing. Check the repository for current implementation status; planned capabilities should not be treated as deployed features unless verified there.

**AWS services/concepts:** Amazon Bedrock AgentCore, Bedrock Knowledge Bases, AgentCore Gateway, Lambda, AgentCore Memory, Code Interpreter, Browser Tool.

### 5. Strands Agents + Bedrock AgentCore Workshop
**Repository:** [sample-strands-agents-hands-on-workshop](https://github.com/harveenkaur282-web/sample-strands-agents-hands-on-workshop)

Hands-on workshop material for learning agent tools, hooks, memory, deployment, multi-agent delegation, and evaluations with Strands Agents and Amazon Bedrock AgentCore. This is listed as **workshop/learning material**, not as an entirely original project.

## Related Cloud-Native Project

### CloudCart — Cloud-Native Microservices Platform
**Repository:** [cloud-native-microservices-app](https://github.com/harveenkaur282-web/cloud-native-microservices-app)

A cloud-native e-commerce platform with a Next.js dashboard, FastAPI gateway, domain microservices, PostgreSQL database-per-service, Docker Compose, and Kubernetes/NGINX Ingress manifests. It complements the AWS projects with containerization and orchestration practice; it is not presented as an AWS deployment unless deployed to AWS.

## Skills and Concepts Practiced

- **AWS foundations:** S3, CloudFront, Lambda, IAM, CloudWatch
- **AWS AI services:** Amazon Polly, Amazon Bedrock, Bedrock AgentCore
- **Serverless and managed services:** DynamoDB, CloudFormation, AgentCore Gateway
- **Cloud-native engineering:** Docker, Kubernetes, microservices, API integration
- **Engineering practices:** architecture documentation, reproducible setup steps, evaluation, logging, and security-aware configuration

## Next Improvements

- Add deployment evidence and architecture diagrams where available.
- Document least-privilege IAM policies and safe teardown steps.
- Add repeatable deployment using Infrastructure as Code.
- Record cost assumptions and cleanup guidance for resources that can incur charges.
- Add automated tests and operational monitoring to the serverless projects.

## Contact

- [GitHub profile](https://github.com/harveenkaur282-web)
- [LinkedIn](https://www.linkedin.com/in/harveen-kaur-ab8347355)
