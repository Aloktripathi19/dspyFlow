import os
import typer
from dotenv import load_dotenv

import dspy
from dspy.signatures.field import InputField, OutputField

# -------- 1. Load & verify your OpenAI key --------
load_dotenv()
assert os.getenv("OPENAI_API_KEY"), "🔑 OPENAI_API_KEY not set!"

# -------- 2. Configure DSPy with a built‑in OpenAI LM --------
# Use "openai/gpt-4" (or "openai/gpt-3.5-turbo")—avoid the "gpt-4o" name until DSPy adds full support.
dspy.configure(
    lm=dspy.LM(
        "openai/gpt-4o",
        api_key=os.environ["OPENAI_API_KEY"]
    )
)  # :contentReference[oaicite:0]{index=0}

# -------- 3. Define your Signatures --------
class PromptRefinementSignature(dspy.Signature):
    vague_prompt:    str = InputField(desc="the user’s original, vague prompt")
    improved_prompt: str = OutputField(desc="the rewritten, clarified version")

class StepwiseAnswerSignature(dspy.Signature):
    question:        str = InputField(desc="the refined question to answer")
    thought_process: str = OutputField(desc="the chain-of-thought reasoning")
    final_answer:    str = OutputField(desc="the complete answer after reasoning")

class AnswerSummarySignature(dspy.Signature):
    full_answer:     str = InputField(desc="the long answer to summarize")
    concise_summary: str = OutputField(desc="the short, bullet-point summary")

# -------- 4. Build your Modules --------
class PromptRefiner(dspy.Module):
    def __init__(self):
        super().__init__()
        self.refiner = dspy.Predict(PromptRefinementSignature)

    def forward(self, vague_prompt: str) -> str:
        return self.refiner(vague_prompt=vague_prompt).improved_prompt

class StepwiseAnswerer(dspy.Module):
    def __init__(self):
        super().__init__()
        self.thinker = dspy.ChainOfThought(StepwiseAnswerSignature)

    def forward(self, question: str):
        result = self.thinker(question=question)
        return result.thought_process, result.final_answer

class AnswerSummarizer(dspy.Module):
    def __init__(self):
        super().__init__()
        self.summarizer = dspy.Predict(AnswerSummarySignature)

    def forward(self, full_answer: str) -> str:
        return self.summarizer(full_answer=full_answer).concise_summary

# -------- 5. Wire up Typer CLI --------
app = typer.Typer()

@app.command()
def ask(prompt: str):
    """
    Accepts a user prompt, improves it, answers it step-by-step, and summarizes the final answer.
    """
    print("\n🎯 Step 1: Improving your prompt…")
    improved = PromptRefiner()(prompt)
    print("✅ Refined Prompt:\n", improved)

    print("\n🧠 Step 2: Generating a step-by-step answer…")
    thoughts, answer = StepwiseAnswerer()(improved)
    print("🧩 Thought Process:\n", thoughts)
    print("\n📘 Final Answer:\n", answer)

    print("\n✂️ Step 3: Summarizing the answer…")
    summary = AnswerSummarizer()(answer)
    print("\n📝 Answer Summary:\n", summary)

if __name__ == "__main__":
    app()
