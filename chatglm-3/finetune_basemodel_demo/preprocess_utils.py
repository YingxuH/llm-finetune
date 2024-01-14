from transformers import PreTrainedTokenizer
from torch.utils.data import Dataset
from typing import Dict, List

LLAMA_CHINESE_PROMPT_TEMPLATE = (
    "[INST] <<SYS>>\n"
    "You are a helpful assistant, 你是一个有能力的助手。\n"
    "<</SYS>>\n\n{instruction} [/INST]"
)

SPN_PROMPT_TEMPLATE = (
    "你是一个电信领域大模型，指责是帮助用户解决问题"
    "### Input:\n"
    "{instruction}\n"
    "### Response:\n"
)


class InputOutputDataset(Dataset):
    def __init__(self, data: List[dict], tokenizer: PreTrainedTokenizer, max_source_length: int,
                 max_target_length: int):
        super(InputOutputDataset, self).__init__()
        self.tokenizer = tokenizer
        self.max_source_length = max_source_length
        self.max_target_length = max_target_length
        self.max_seq_length = max_source_length + max_target_length + 1
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, i) -> dict:
        data_item = self.data[i]

        context = f"Instruction: {data_item['instruction']}\n"
        if data_item.get('input'):
            context += f"Input: {data_item['input']}\n"
        context += "Answer: "
        target = data_item["answer"]

        a_ids = self.tokenizer.encode(text=context, add_special_tokens=True, truncation=True,
                                      max_length=self.max_source_length)
        b_ids = self.tokenizer.encode(text=target, add_special_tokens=False, truncation=True,
                                      max_length=self.max_target_length)

        context_length = len(a_ids)
        input_ids = a_ids + b_ids + [self.tokenizer.eos_token_id]
        labels = [self.tokenizer.pad_token_id] * context_length + b_ids + [self.tokenizer.eos_token_id]

        # pad_len = self.max_seq_length - len(input_ids)
        # input_ids = input_ids + [self.tokenizer.pad_token_id] * pad_len
        # labels = labels + [self.tokenizer.pad_token_id] * pad_len
        labels = [(l if l != self.tokenizer.pad_token_id else -100) for l in labels]

        assert len(input_ids) == len(labels), f"length mismatch: {len(input_ids)} vs {len(labels)}"

        return {
            "input_ids": input_ids,
            "labels": labels
        }
