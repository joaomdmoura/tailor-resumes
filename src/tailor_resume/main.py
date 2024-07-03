#!/usr/bin/env python
import sys
from tailor_resume.crew import TailorResumeCrew


def run():
    with open('resume.md', 'r') as f:
        resume = f.read()

    inputs = {
        "job_posting": "https://www.amazon.jobs/en/jobs/2668304/sr-software-engineer-ai-ml-aws-neuron-distributed-training?utm_source=WCT-FCT+job+board&utm_medium=getro.com&gh_src=WCT-FCT+job+board",
        "fit_score": "9.0",
        "fit_score_explanation": "The candidate's experience with Python, distributed training libraries like FSDP and Deepspeed, and knowledge of large-scale ML models such as GPT and Vision Transformers align well with this role. The role's focus on AWS Neuron and Trainium instances matches the candidate's expertise in cloud-scale ML accelerators, making it a strong fit.",
        "resume": resume
    }
    TailorResumeCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    with open('resume.md', 'r') as f:
        resume = f.read()

    inputs = {
        "job_posting": "https://www.amazon.jobs/en/jobs/2668304/sr-software-engineer-ai-ml-aws-neuron-distributed-training?utm_source=WCT-FCT+job+board&utm_medium=getro.com&gh_src=WCT-FCT+job+board",
        "fit_score": "9.0",
        "fit_score_explanation": "The candidate's experience with Python, distributed training libraries like FSDP and Deepspeed, and knowledge of large-scale ML models such as GPT and Vision Transformers align well with this role. The role's focus on AWS Neuron and Trainium instances matches the candidate's expertise in cloud-scale ML accelerators, making it a strong fit.",
        "resume": resume
    }
    try:
        TailorResumeCrew().crew().train(n_iterations=int(sys.argv[1]), inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")
