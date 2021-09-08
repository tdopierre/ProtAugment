from transformers import AutoTokenizer, AutoModelForMaskedLM

for url, model_dir in [
    ("tdopierre/ProtAugment-LM-BANKING77", "transformer_models/BANKING77/fine-tuned"),
    ("tdopierre/ProtAugment-LM-HWU64", "transformer_models/HWU64/fine-tuned"),
    ("tdopierre/ProtAugment-LM-Clinic150", "transformer_models/OOS/fine-tuned"),
    ("tdopierre/ProtAugment-LM-Liu", "transformer_models/Liu/fine-tuned")
]:
    tokenizer = AutoTokenizer.from_pretrained(url)
    model = AutoModelForMaskedLM.from_pretrained(url)
    tokenizer.save_pretrained(model_dir)
    model.save_pretrained(model_dir)

