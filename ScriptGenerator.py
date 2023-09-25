from transformers import pipeline

class ScriptGenerator:
    def __init__(self, model_name: str, device: int = -1):
        self.generator = pipeline("text-generation", model=model_name, device=device )

    def generate_script(self, prompt: str, max_length: int = 50, num_return_sequences: int = 1) -> str:
        p = f"""
        Generate a script based on the given prompt.

        Parameters:
        - prompt (str): The initial text to start the script generation.
        - max_length (int): The maximum length of the generated text.
        - num_return_sequences (int): The number of different scripts to generate.

        Returns:
        - str: The generated script.

        Prompt
        - {prompt}
        """
        outputs = self.generator(p, max_length=max_length, num_return_sequences=num_return_sequences, return_full_text=False)
        if num_return_sequences == 1:
            return outputs[0]['generated_text']
        else:
            return [output['generated_text'] for output in outputs]
