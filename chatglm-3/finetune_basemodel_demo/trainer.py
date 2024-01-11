# coding=utf-8
# Copyright 2020-present the HuggingFace Inc. team.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
The Trainer class, to easily train a 🤗 Transformers from scratch or finetune it on a new task.
"""
# coding=utf-8
import os
import torch
from transformers import Trainer
from transformers.modeling_utils import unwrap_model, PreTrainedModel
from transformers.utils import logging

logger = logging.get_logger(__name__)

class LoRATrainer(Trainer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
