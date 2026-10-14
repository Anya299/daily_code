from abc import ABC, abstractmethod


# --------------------------------------------------
# 1. Model abstraction
# --------------------------------------------------

class AIModel(ABC):

    @abstractmethod
    def generate(self, prompt):
        pass


# --------------------------------------------------
# 2. Concrete implementations
# --------------------------------------------------

class OpenAIModel(AIModel):

    def generate(self, prompt):
        return f"OpenAI response for: {prompt}"


class OllamaModel(AIModel):

    def generate(self, prompt):
        return f"Ollama response for: {prompt}"


# --------------------------------------------------
# 3. Dependency Injection
# --------------------------------------------------

class AIService:

    def __init__(self, model):
        self.model = model

    def ask(self, prompt):
        return self.model.generate(prompt)


# --------------------------------------------------
# 4. Application
# --------------------------------------------------

openai_model = OpenAIModel()

service = AIService(openai_model)

print(service.ask("Explain Python OOP."))


ollama_model = OllamaModel()

service = AIService(ollama_model)

print(service.ask("Explain machine learning."))
