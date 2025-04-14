from transformers import AutoTokenizer

def detect_max_context_length(model_name_or_path):
    """
    Attempts to detect the maximum context length of a transformer model.

    Args:
        model_name_or_path: The name or path of the pre-trained model.

    Returns:
        The maximum context length (int) if detected, or None if it cannot be determined.
        Also returns a boolean indicating if the detection was successful.
    """
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

        # Common attributes where context length is stored
        possible_attributes = [
            "model_max_length",
            "context_length",
            "n_positions",  # For some older models
            "max_position_embeddings"
        ]

        for attr in possible_attributes:
            if hasattr(tokenizer, attr):
                max_length = getattr(tokenizer, attr)
                if isinstance(max_length, int) and max_length > 0: # Check if it's a positive int
                    return max_length, True

        #Special case for some models
        if hasattr(tokenizer.config, 'max_position_embeddings'):
            max_length = tokenizer.config.max_position_embeddings
            if isinstance(max_length, int) and max_length > 0:
                return max_length, True

        return None, False  # Could not determine context length
    except Exception as e:
        print(f"Error loading tokenizer or detecting context length: {e}")
        return None, False


# Example usage:
models_to_test = [
    "bert-base-uncased",
    "gpt2",
    "google/flan-t5-xl",
    "google/flan-ul2",
    "facebook/opt-125m",
    "meta-llama/Llama-2-7b-chat-hf",
    "google/gemma-7b",
    "mistralai/Mistral-7B-v0.1"
]

for model_name in models_to_test:
    max_length, success = detect_max_context_length(model_name)
    if success:
        print(f"Model: {model_name}, Max Context Length: {max_length}")
    else:
        print(f"Model: {model_name}, Could not detect max context length.")

# Example of a model on Vertex AI (you'd need to adapt this if it's not a standard HF model):
vertex_model = "google/flan-t5-xxl" # Example, replace if needed
max_length_vertex, success_vertex = detect_max_context_length(vertex_model)
if success_vertex:
    print(f"Vertex AI Model: {vertex_model}, Max Context Length: {max_length_vertex}")
else:
    print(f"Vertex AI Model: {vertex_model}, Could not detect max context length. Consult Vertex AI documentation.")