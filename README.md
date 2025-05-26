---
license: other
datasets:
- MERaLiON/Multitask-National-Speech-Corpus-v1
language:
- en
- ms
- ta
- id
- th
- vi
metrics:
- wer
- bleu
base_model:
- openai/whisper-large-v3
- google/gemma-2-9b-it
library_name: transformers
tags:
- meralion
- meralion-2
---
# 🎉 MERaLiON-2: [MERaLiON-2-10B](https://huggingface.co/MERaLiON/MERaLiON-2-10B) | [MERaLiON-2-10B-ASR](https://huggingface.co/MERaLiON/MERaLiON-2-10B-ASR) | [MERaLiON-2-3B](https://huggingface.co/MERaLiON/MERaLiON-2-3B)


## 🆙 What's New in V2

- **Extended Audio Length**: Improved support for audio inputs up to 300 seconds (5 minutes), compared to the 30-second limit in V1.

- **Expanded Language Coverage**: In addition to English, Chinese, and Singlish, V2 introduces support for Malay, Tamil, and other regional languages including Indonesian, Thai, and Vietnamese.

- **Improved Performance**: Achieves higher performance across a wide range of tasks. See the Evaluation section for detailed benchmarks.

- **Higher Quality Training Data**: Trained on 120,000 hours of curated speech and audio data, filtered for quality and diversity, with an emphasis on local and multilingual audio sources.

---

## 📝 Model Description: 

MERaLiON-2 is a family of Speech-Text Large Language Models tailored for **Singapore’s multilingual and multicultural landscape**, as well as the wider **Southeast Asian region**. 
The 10B model integrates a localized [Whisper-Large-V3](https://huggingface.co/openai/whisper-large-v3) speech encoder with the [Gemma2-9b-IT](https://huggingface.co/google/gemma-2-9b-it) text decoder.
The 3B model integrates a localized [Whisper-Large-V3](https://huggingface.co/openai/whisper-large-v3) speech encoder with the [Gemma2-2b-IT](https://huggingface.co/google/gemma-2-2b-it) text decoder.
The model is finetuned on **120,000 hours of speech and audio data** across **6 diverse tasks**. 
The model supports long-form audio inputs of up to 300 seconds (5 minutes) and is specifically adapted to handle the linguistic nuances, accents, and dialects commonly found across Singapore and neighboring countries.

MERaLiON stands for **M**ultimodal **E**mpathetic **R**easoning **a**nd **L**earning **i**n **O**ne **N**etwork.

- **Developed by:** I<sup>2</sup>R, A\*STAR, Singapore
- **Model type:** Multimodal LLM
- **Language(s):** Primarily English (Global and Singapore), with support for audio of regional languages including Malay, Tamil, Indonesian, Thai, and Vietnamese.
- **Audio:** **Mono** channel audio, **16000** hz, up to **300** seconds.
- **License:** [MERaLiON Public License](https://huggingface.co/MERaLiON/MERaLiON-AudioLLM-Whisper-SEA-LION/blob/main/MERaLiON-Public-Licence-v1.pdf)
- **Demo:** [MERaLiON-AudioLLM Web Demo](https://meralion.org/demo/)

<!-- We support model inference using the [**Huggingface**](#inference) and [**vLLM**](vllm_plugin_meralion/README.md) frameworks, enabling [**lightning inference speed**](https://huggingface.co/MERaLiON/MERaLiON-AudioLLM-Whisper-SEA-LION/blob/main/vllm_plugin_meralion/README.md#inference-performance-benchmark). -->

**MERaLiON-2** is an upgraded version of [MERaLiON-AudioLLM](https://huggingface.co/MERaLiON/MERaLiON-AudioLLM-Whisper-SEA-LION).

---



## 📈 Evaluations: 
We benchmark MERaLiON-2 series models with extended [AudioBench benchmark](https://github.com/AudioLLMs/AudioBench) | [LeaderBoard](https://huggingface.co/spaces/MERaLiON/AudioBench-Leaderboard) against several recently released opensource multimodal models — SALMONN-7B, Qwen2.5-Omni series and Phi-4-Multimodal — as well as two cascade model. The MERaLiON-2 series models shows stronger performance on a wide range of audio/speech understanding tasks.


**Automatic Speech Recognition (ASR) results**
<div class="table*">
  <table>
    <thead>
      <tr>
        <th style="text-align: center;"><strong>type</strong></th>
        <th style="text-align: center;"><strong>dataset</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-1</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-2-3B</strong></th>
        <th style="text-align: center; background-color: #06a2a2;"><strong>MERaLiON-2-10B</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-2-10B-ASR</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-2-Whisper </strong></th>
        <th style="text-align: center;"><strong>whisper_large_v3</strong></th>
        <th style="text-align: center;"><strong>Phi-4-multimodal-instruct</strong></th>
        <th style="text-align: center;"><strong>Qwen2.5-Omni-3B</strong></th>
        <th style="text-align: center;"><strong>Qwen2.5-Omni-7B</strong></th>
        <th style="text-align: center;"><strong>SALMONN-7B</strong></th>
        <th style="text-align: center;"><strong>cascade-whisper_v2+sealion</strong></th>
        <th style="text-align: center;"><strong>cascade-whisper_v3+llama</strong></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="column style5 s style7" rowspan="10">English</td>
        <td style="text-align: center;"><strong>common_voice_15_en</strong></td>
        <td style="text-align: center;">0.078</td>
        <td style="text-align: center;">0.093</td>
        <td style="text-align: center; background-color: #06a2a2;">0.087</td>
        <td style="text-align: center;"><strong><u>0.076</u></strong></td>
        <td style="text-align: center;">0.102</td>
        <td style="text-align: center;">0.100</td>
        <td style="text-align: center;">0.081</td>
        <td style="text-align: center;">0.094</td>
        <td style="text-align: center;">0.080</td>
        <td style="text-align: center;">0.316</td>
        <td style="text-align: center;">0.106</td>
        <td style="text-align: center;">0.099</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>earnings21</strong></td>
        <td style="text-align: center;">0.138</td>
        <td style="text-align: center;">0.219</td>
        <td style="text-align: center; background-color: #06a2a2;">0.108</td>
        <td style="text-align: center;"><strong><u>0.092</u></strong></td>
        <td style="text-align: center;">0.130</td>
        <td style="text-align: center;">0.132</td>
        <td style="text-align: center;">0.131</td>
        <td style="text-align: center;">0.147</td>
        <td style="text-align: center;">0.189</td>
        <td style="text-align: center;">0.277</td>
        <td style="text-align: center;">0.141</td>
        <td style="text-align: center;">0.109</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>earnings22</strong></td>
        <td style="text-align: center;">0.166</td>
        <td style="text-align: center;">0.239</td>
        <td style="text-align: center; background-color: #06a2a2;">0.151</td>
        <td style="text-align: center;"><strong><u>0.128</u></strong></td>
        <td style="text-align: center;">0.168</td>
        <td style="text-align: center;">0.165</td>
        <td style="text-align: center;">0.226</td>
        <td style="text-align: center;">0.197</td>
        <td style="text-align: center;">0.241</td>
        <td style="text-align: center;">0.380</td>
        <td style="text-align: center;">0.172</td>
        <td style="text-align: center;">0.146</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>gigaspeech</strong></td>
        <td style="text-align: center;">0.145</td>
        <td style="text-align: center;">0.092</td>
        <td style="text-align: center; background-color: #06a2a2;">0.090</td>
        <td style="text-align: center;"><strong><u>0.088</u></strong></td>
        <td style="text-align: center;">0.089</td>
        <td style="text-align: center;">0.098</td>
        <td style="text-align: center;">0.099</td>
        <td style="text-align: center;">0.114</td>
        <td style="text-align: center;">0.140</td>
        <td style="text-align: center;">0.110</td>
        <td style="text-align: center;">0.100</td>
        <td style="text-align: center;">0.095</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>librispeech_clean</strong></td>
        <td style="text-align: center;">0.024</td>
        <td style="text-align: center;">0.027</td>
        <td style="text-align: center; background-color: #06a2a2;">0.025</td>
        <td style="text-align: center;">0.021</td>
        <td style="text-align: center;">0.020</td>
        <td style="text-align: center;">0.022</td>
        <td style="text-align: center;"><strong><u>0.017</u></strong></td>
        <td style="text-align: center;">0.021</td>
        <td style="text-align: center;">0.044</td>
        <td style="text-align: center;">0.096</td>
        <td style="text-align: center;">0.033</td>
        <td style="text-align: center;">0.018</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>librispeech_other</strong></td>
        <td style="text-align: center;">0.042</td>
        <td style="text-align: center;">0.051</td>
        <td style="text-align: center; background-color: #06a2a2;">0.047</td>
        <td style="text-align: center;">0.040</td>
        <td style="text-align: center;">0.044</td>
        <td style="text-align: center;">0.039</td>
        <td style="text-align: center;">0.039</td>
        <td style="text-align: center;">0.045</td>
        <td style="text-align: center;">0.069</td>
        <td style="text-align: center;">0.118</td>
        <td style="text-align: center;">0.054</td>
        <td style="text-align: center;"><strong><u>0.036</u></strong></td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>peoples_speech</strong></td>
        <td style="text-align: center;">0.216</td>
        <td style="text-align: center;">0.206</td>
        <td style="text-align: center; background-color: #06a2a2;">0.205</td>
        <td style="text-align: center;">0.196</td>
        <td style="text-align: center;">0.197</td>
        <td style="text-align: center;">0.150</td>
        <td style="text-align: center;">0.215</td>
        <td style="text-align: center;">0.262</td>
        <td style="text-align: center;">0.312</td>
        <td style="text-align: center;">0.242</td>
        <td style="text-align: center;">0.203</td>
        <td style="text-align: center;"><strong><u>0.145</u></strong></td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>tedlium3</strong></td>
        <td style="text-align: center;">0.082</td>
        <td style="text-align: center;">0.035</td>
        <td style="text-align: center; background-color: #06a2a2;">0.035</td>
        <td style="text-align: center;">0.031</td>
        <td style="text-align: center;">0.036</td>
        <td style="text-align: center;">0.041</td>
        <td style="text-align: center;"><strong><u>0.029</u></strong></td>
        <td style="text-align: center;">0.048</td>
        <td style="text-align: center;">0.049</td>
        <td style="text-align: center;">0.039</td>
        <td style="text-align: center;">0.049</td>
        <td style="text-align: center;">0.038</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>tedlium3_long_form</strong></td>
        <td style="text-align: center;">0.105</td>
        <td style="text-align: center;">0.138</td>
        <td style="text-align: center; background-color: #06a2a2;">0.044</td>
        <td style="text-align: center;"><strong><u>0.035</u></strong></td>
        <td style="text-align: center;">0.048</td>
        <td style="text-align: center;">0.045</td>
        <td style="text-align: center;">0.051</td>
        <td style="text-align: center;">0.071</td>
        <td style="text-align: center;">0.084</td>
        <td style="text-align: center;">0.141</td>
        <td style="text-align: center;">0.086</td>
        <td style="text-align: center;">0.049</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>average</strong></td>
        <td style="text-align: center;">0.111</td>
        <td style="text-align: center;">0.122</td>
        <td style="text-align: center; background-color: #06a2a2;">0.088</td>
        <td style="text-align: center;"><strong><u>0.079</u></strong></td>
        <td style="text-align: center;">0.093</td>
        <td style="text-align: center;">0.088</td>
        <td style="text-align: center;">0.098</td>
        <td style="text-align: center;">0.111</td>
        <td style="text-align: center;">0.134</td>
        <td style="text-align: center;">0.191</td>
        <td style="text-align: center;">0.105</td>
        <td style="text-align: center;">0.082</td>
      </tr>
      <tr>
        <td class="column style5 s style7" rowspan="14">Inhouse</td>
        <td style="text-align: center;"><strong>cna</strong></td>
        <td style="text-align: center;">0.145</td>
        <td style="text-align: center;">0.135</td>
        <td style="text-align: center; background-color: #06a2a2;">0.133</td>
        <td style="text-align: center;"><strong><u>0.127</u></strong></td>
        <td style="text-align: center;">0.128</td>
        <td style="text-align: center;">0.138</td>
        <td style="text-align: center;">0.191</td>
        <td style="text-align: center;">0.174</td>
        <td style="text-align: center;">0.183</td>
        <td style="text-align: center;">0.149</td>
        <td style="text-align: center;">0.152</td>
        <td style="text-align: center;">0.138</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>idpc</strong></td>
        <td style="text-align: center;">0.204</td>
        <td style="text-align: center;">0.177</td>
        <td style="text-align: center; background-color: #06a2a2;"><strong><u>0.160</u></strong></td>
        <td style="text-align: center;">0.166</td>
        <td style="text-align: center;">0.169</td>
        <td style="text-align: center;">0.179</td>
        <td style="text-align: center;">0.261</td>
        <td style="text-align: center;">0.199</td>
        <td style="text-align: center;">0.220</td>
        <td style="text-align: center;">0.541</td>
        <td style="text-align: center;">0.170</td>
        <td style="text-align: center;">0.162</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>idpc_short</strong></td>
        <td style="text-align: center;">0.165</td>
        <td style="text-align: center;">0.151</td>
        <td style="text-align: center; background-color: #06a2a2;">0.157</td>
        <td style="text-align: center;"><strong><u>0.140</u></strong></td>
        <td style="text-align: center;">0.152</td>
        <td style="text-align: center;">0.220</td>
        <td style="text-align: center;">0.539</td>
        <td style="text-align: center;">0.211</td>
        <td style="text-align: center;">0.414</td>
        <td style="text-align: center;">0.240</td>
        <td style="text-align: center;">0.197</td>
        <td style="text-align: center;">0.153</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>mediacorp</strong></td>
        <td style="text-align: center;">0.123</td>
        <td style="text-align: center;">0.123</td>
        <td style="text-align: center; background-color: #06a2a2;">0.105</td>
        <td style="text-align: center;"><strong><u>0.104</u></strong></td>
        <td style="text-align: center;">0.116</td>
        <td style="text-align: center;">0.129</td>
        <td style="text-align: center;">0.198</td>
        <td style="text-align: center;">0.152</td>
        <td style="text-align: center;">0.235</td>
        <td style="text-align: center;">0.364</td>
        <td style="text-align: center;">0.158</td>
        <td style="text-align: center;">0.151</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>mediacorp_short</strong></td>
        <td style="text-align: center;">0.128</td>
        <td style="text-align: center;">0.121</td>
        <td style="text-align: center; background-color: #06a2a2;">0.117</td>
        <td style="text-align: center;">0.118</td>
        <td style="text-align: center;">0.122</td>
        <td style="text-align: center;">0.127</td>
        <td style="text-align: center;">0.122</td>
        <td style="text-align: center;">0.148</td>
        <td style="text-align: center;">0.141</td>
        <td style="text-align: center;">0.199</td>
        <td style="text-align: center;">0.154</td>
        <td style="text-align: center;"><strong><u>0.114</u></strong></td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>parliament</strong></td>
        <td style="text-align: center;">0.059</td>
        <td style="text-align: center;">0.185</td>
        <td style="text-align: center; background-color: #06a2a2;">0.060</td>
        <td style="text-align: center;"><strong><u>0.053</u></strong></td>
        <td style="text-align: center;">0.078</td>
        <td style="text-align: center;">0.090</td>
        <td style="text-align: center;">0.278</td>
        <td style="text-align: center;">0.100</td>
        <td style="text-align: center;">0.110</td>
        <td style="text-align: center;">0.204</td>
        <td style="text-align: center;">0.090</td>
        <td style="text-align: center;">0.065</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>ste</strong></td>
        <td style="text-align: center;">0.159</td>
        <td style="text-align: center;">0.263</td>
        <td style="text-align: center; background-color: #06a2a2;">0.147</td>
        <td style="text-align: center;"><strong><u>0.125</u></strong></td>
        <td style="text-align: center;">0.151</td>
        <td style="text-align: center;">0.298</td>
        <td style="text-align: center;">0.297</td>
        <td style="text-align: center;">0.287</td>
        <td style="text-align: center;">0.288</td>
        <td style="text-align: center;">0.422</td>
        <td style="text-align: center;">0.132</td>
        <td style="text-align: center;">0.144</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>ukusnews</strong></td>
        <td style="text-align: center;">0.113</td>
        <td style="text-align: center;">0.174</td>
        <td style="text-align: center; background-color: #06a2a2;">0.070</td>
        <td style="text-align: center;"><strong><u>0.056</u></strong></td>
        <td style="text-align: center;">0.083</td>
        <td style="text-align: center;">0.123</td>
        <td style="text-align: center;">0.075</td>
        <td style="text-align: center;">0.091</td>
        <td style="text-align: center;">0.176</td>
        <td style="text-align: center;">0.192</td>
        <td style="text-align: center;">0.123</td>
        <td style="text-align: center;">0.089</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>ytb_asr_batch1</strong></td>
        <td style="text-align: center;">0.107</td>
        <td style="text-align: center;">0.099</td>
        <td style="text-align: center; background-color: #06a2a2;">0.098</td>
        <td style="text-align: center;"><strong><u>0.092</u></strong></td>
        <td style="text-align: center;">0.112</td>
        <td style="text-align: center;">0.133</td>
        <td style="text-align: center;">0.169</td>
        <td style="text-align: center;">0.162</td>
        <td style="text-align: center;">0.174</td>
        <td style="text-align: center;">0.221</td>
        <td style="text-align: center;">0.125</td>
        <td style="text-align: center;">0.108</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>ytb_asr_batch2</strong></td>
        <td style="text-align: center;">0.133</td>
        <td style="text-align: center;">0.160</td>
        <td style="text-align: center; background-color: #06a2a2;">0.111</td>
        <td style="text-align: center;">0.099</td>
        <td style="text-align: center;">0.118</td>
        <td style="text-align: center;">0.129</td>
        <td style="text-align: center;">0.232</td>
        <td style="text-align: center;">0.245</td>
        <td style="text-align: center;">0.351</td>
        <td style="text-align: center;">0.350</td>
        <td style="text-align: center;">0.126</td>
        <td style="text-align: center;"><strong><u>0.084</u></strong></td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>ytb_asr_batch3_chinese</strong></td>
        <td style="text-align: center;">0.418</td>
        <td style="text-align: center;">0.256</td>
        <td style="text-align: center; background-color: #06a2a2;">0.191</td>
        <td style="text-align: center;"><strong><u>0.149</u></strong></td>
        <td style="text-align: center;">0.177</td>
        <td style="text-align: center;">0.266</td>
        <td style="text-align: center;">0.440</td>
        <td style="text-align: center;">0.250</td>
        <td style="text-align: center;">0.206</td>
        <td style="text-align: center;">0.886</td>
        <td style="text-align: center;">0.347</td>
        <td style="text-align: center;">0.270</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>ytb_asr_batch3_malay</strong></td>
        <td style="text-align: center;">0.290</td>
        <td style="text-align: center;">0.280</td>
        <td style="text-align: center; background-color: #06a2a2;">0.209</td>
        <td style="text-align: center;"><strong><u>0.195</u></strong></td>
        <td style="text-align: center;">0.290</td>
        <td style="text-align: center;">0.260</td>
        <td style="text-align: center;">3.763</td>
        <td style="text-align: center;">2.944</td>
        <td style="text-align: center;">1.461</td>
        <td style="text-align: center;">1.086</td>
        <td style="text-align: center;">0.314</td>
        <td style="text-align: center;">0.312</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>ytb_asr_batch3_tamil</strong></td>
        <td style="text-align: center;">0.693</td>
        <td style="text-align: center;">0.750</td>
        <td style="text-align: center; background-color: #06a2a2;">0.664</td>
        <td style="text-align: center;"><strong><u>0.547</u></strong></td>
        <td style="text-align: center;">0.927</td>
        <td style="text-align: center;">0.841</td>
        <td style="text-align: center;">2.750</td>
        <td style="text-align: center;">1.461</td>
        <td style="text-align: center;">1.362</td>
        <td style="text-align: center;">0.985</td>
        <td style="text-align: center;">0.967</td>
        <td style="text-align: center;">0.898</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>average</strong></td>
        <td style="text-align: center;">0.210</td>
        <td style="text-align: center;">0.221</td>
        <td style="text-align: center; background-color: #06a2a2;">0.171</td>
        <td style="text-align: center;"><strong><u>0.152</u></strong></td>
        <td style="text-align: center;">0.202</td>
        <td style="text-align: center;">0.226</td>
        <td style="text-align: center;">0.717</td>
        <td style="text-align: center;">0.494</td>
        <td style="text-align: center;">0.409</td>
        <td style="text-align: center;">0.449</td>
        <td style="text-align: center;">0.235</td>
        <td style="text-align: center;">0.207</td>
      </tr>
      <tr>
        <td class="column style5 s style7" rowspan="3">Mandarin</td>
        <td style="text-align: center;"><strong>aishell_asr_zh</strong></td>
        <td style="text-align: center;">0.128</td>
        <td style="text-align: center;">0.050</td>
        <td style="text-align: center; background-color: #06a2a2;">0.058</td>
        <td style="text-align: center;">0.043</td>
        <td style="text-align: center;">0.056</td>
        <td style="text-align: center;">0.123</td>
        <td style="text-align: center;">0.122</td>
        <td style="text-align: center;">0.028</td>
        <td style="text-align: center;"><strong><u>0.024</u></strong></td>
        <td style="text-align: center;">0.931</td>
        <td style="text-align: center;">0.209</td>
        <td style="text-align: center;">0.125</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>commonvoice_zh</strong></td>
        <td style="text-align: center;">0.327</td>
        <td style="text-align: center;">0.131</td>
        <td style="text-align: center; background-color: #06a2a2;">0.147</td>
        <td style="text-align: center;">0.118</td>
        <td style="text-align: center;">0.141</td>
        <td style="text-align: center;">0.198</td>
        <td style="text-align: center;">0.154</td>
        <td style="text-align: center;">0.113</td>
        <td style="text-align: center;"><strong><u>0.076</u></strong></td>
        <td style="text-align: center;">1.001</td>
        <td style="text-align: center;">0.319</td>
        <td style="text-align: center;">0.196</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>average</strong></td>
        <td style="text-align: center;">0.228</td>
        <td style="text-align: center;">0.091</td>
        <td style="text-align: center; background-color: #06a2a2;">0.102</td>
        <td style="text-align: center;">0.081</td>
        <td style="text-align: center;">0.098</td>
        <td style="text-align: center;">0.161</td>
        <td style="text-align: center;">0.138</td>
        <td style="text-align: center;">0.071</td>
        <td style="text-align: center;"><strong><u>0.050</u></strong></td>
        <td style="text-align: center;">0.966</td>
        <td style="text-align: center;">0.264</td>
        <td style="text-align: center;">0.160</td>
      </tr>
      <tr>
        <td class="column style5 s style7" rowspan="10">SEA languages</td>
        <td style="text-align: center;"><strong>commonvoice_id</strong></td>
        <td style="text-align: center;">0.260</td>
        <td style="text-align: center;">0.085</td>
        <td style="text-align: center; background-color: #06a2a2;">0.113</td>
        <td style="text-align: center;">0.079</td>
        <td style="text-align: center;"><strong><u>0.069</u></strong></td>
        <td style="text-align: center;">0.075</td>
        <td style="text-align: center;">1.327</td>
        <td style="text-align: center;">0.136</td>
        <td style="text-align: center;">0.110</td>
        <td style="text-align: center;">1.189</td>
        <td style="text-align: center;">0.100</td>
        <td style="text-align: center;">0.078</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>commonvoice_ta</strong></td>
        <td style="text-align: center;">0.528</td>
        <td style="text-align: center;">0.139</td>
        <td style="text-align: center; background-color: #06a2a2;">0.156</td>
        <td style="text-align: center;"><strong><u>0.129</u></strong></td>
        <td style="text-align: center;">0.195</td>
        <td style="text-align: center;">0.271</td>
        <td style="text-align: center;">1.178</td>
        <td style="text-align: center;">0.831</td>
        <td style="text-align: center;">0.847</td>
        <td style="text-align: center;">1.427</td>
        <td style="text-align: center;">0.238</td>
        <td style="text-align: center;">0.244</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>commonvoice_th</strong></td>
        <td style="text-align: center;">0.847</td>
        <td style="text-align: center;">0.307</td>
        <td style="text-align: center; background-color: #06a2a2;">0.466</td>
        <td style="text-align: center;">0.635</td>
        <td style="text-align: center;"><strong><u>0.051</u></strong></td>
        <td style="text-align: center;">0.069</td>
        <td style="text-align: center;">1.054</td>
        <td style="text-align: center;">0.113</td>
        <td style="text-align: center;">0.104</td>
        <td style="text-align: center;">1.044</td>
        <td style="text-align: center;">0.093</td>
        <td style="text-align: center;">0.064</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>commonvoice_vi</strong></td>
        <td style="text-align: center;">0.922</td>
        <td style="text-align: center;">0.142</td>
        <td style="text-align: center; background-color: #06a2a2;">0.156</td>
        <td style="text-align: center;">0.142</td>
        <td style="text-align: center;">0.118</td>
        <td style="text-align: center;">0.129</td>
        <td style="text-align: center;">1.107</td>
        <td style="text-align: center;">0.196</td>
        <td style="text-align: center;">0.184</td>
        <td style="text-align: center;">1.496</td>
        <td style="text-align: center;">0.157</td>
        <td style="text-align: center;"><strong><u>0.117</u></strong></td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>fleurs_tamil_ta</strong></td>
        <td style="text-align: center;">0.462</td>
        <td style="text-align: center;">0.143</td>
        <td style="text-align: center; background-color: #06a2a2;">0.161</td>
        <td style="text-align: center;"><strong><u>0.138</u></strong></td>
        <td style="text-align: center;">0.224</td>
        <td style="text-align: center;">0.276</td>
        <td style="text-align: center;">1.702</td>
        <td style="text-align: center;">1.654</td>
        <td style="text-align: center;">0.867</td>
        <td style="text-align: center;">1.508</td>
        <td style="text-align: center;">0.272</td>
        <td style="text-align: center;">0.284</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>gigaspeech2_id</strong></td>
        <td style="text-align: center;">0.337</td>
        <td style="text-align: center;">0.178</td>
        <td style="text-align: center; background-color: #06a2a2;">0.172</td>
        <td style="text-align: center;"><strong><u>0.163</u></strong></td>
        <td style="text-align: center;">0.185</td>
        <td style="text-align: center;">0.196</td>
        <td style="text-align: center;">5.804</td>
        <td style="text-align: center;">0.275</td>
        <td style="text-align: center;">0.227</td>
        <td style="text-align: center;">2.118</td>
        <td style="text-align: center;">0.219</td>
        <td style="text-align: center;">0.193</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>gigaspeech2_th</strong></td>
        <td style="text-align: center;">0.987</td>
        <td style="text-align: center;">0.200</td>
        <td style="text-align: center; background-color: #06a2a2;">0.200</td>
        <td style="text-align: center;">0.182</td>
        <td style="text-align: center;"><strong><u>0.171</u></strong></td>
        <td style="text-align: center;">0.222</td>
        <td style="text-align: center;">1.734</td>
        <td style="text-align: center;">0.300</td>
        <td style="text-align: center;">0.232</td>
        <td style="text-align: center;">1.247</td>
        <td style="text-align: center;">0.276</td>
        <td style="text-align: center;">0.209</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>gigaspeech2_vi</strong></td>
        <td style="text-align: center;">0.982</td>
        <td style="text-align: center;">0.168</td>
        <td style="text-align: center; background-color: #06a2a2;">0.113</td>
        <td style="text-align: center;"><strong><u>0.095</u></strong></td>
        <td style="text-align: center;">0.127</td>
        <td style="text-align: center;">0.177</td>
        <td style="text-align: center;">2.504</td>
        <td style="text-align: center;">0.177</td>
        <td style="text-align: center;">0.227</td>
        <td style="text-align: center;">1.546</td>
        <td style="text-align: center;">0.171</td>
        <td style="text-align: center;">0.155</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>lotus_thai_th</strong></td>
        <td style="text-align: center;">0.852</td>
        <td style="text-align: center;">0.015</td>
        <td style="text-align: center; background-color: #06a2a2;">0.019</td>
        <td style="text-align: center;"><strong><u>0.011</u></strong></td>
        <td style="text-align: center;">0.026</td>
        <td style="text-align: center;">0.039</td>
        <td style="text-align: center;">1.286</td>
        <td style="text-align: center;">0.026</td>
        <td style="text-align: center;">0.021</td>
        <td style="text-align: center;">1.135</td>
        <td style="text-align: center;">0.068</td>
        <td style="text-align: center;">0.032</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>average</strong></td>
        <td style="text-align: center;">0.686</td>
        <td style="text-align: center;">0.153</td>
        <td style="text-align: center; background-color: #06a2a2;">0.173</td>
        <td style="text-align: center;">0.175</td>
        <td style="text-align: center;"><strong><u>0.129</u></strong></td>
        <td style="text-align: center;">0.162</td>
        <td style="text-align: center;">1.966</td>
        <td style="text-align: center;">0.412</td>
        <td style="text-align: center;">0.313</td>
        <td style="text-align: center;">1.412</td>
        <td style="text-align: center;">0.177</td>
        <td style="text-align: center;">0.153</td>
      </tr>
      <tr>
        <td class="column style5 s style7" rowspan="7">Singlish</td>
        <td style="text-align: center;"><strong>imda_part1_asr</strong></td>
        <td style="text-align: center;"><strong><u>0.043</u></strong></td>
        <td style="text-align: center;">0.049</td>
        <td style="text-align: center; background-color: #06a2a2;">0.052</td>
        <td style="text-align: center;">0.044</td>
        <td style="text-align: center;">0.052</td>
        <td style="text-align: center;">0.069</td>
        <td style="text-align: center;">0.058</td>
        <td style="text-align: center;">0.053</td>
        <td style="text-align: center;">0.053</td>
        <td style="text-align: center;">0.093</td>
        <td style="text-align: center;">0.071</td>
        <td style="text-align: center;">0.069</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>imda_part2_asr</strong></td>
        <td style="text-align: center;"><strong><u>0.047</u></strong></td>
        <td style="text-align: center;">0.058</td>
        <td style="text-align: center; background-color: #06a2a2;">0.145</td>
        <td style="text-align: center;">0.054</td>
        <td style="text-align: center;">0.080</td>
        <td style="text-align: center;">0.318</td>
        <td style="text-align: center;">0.345</td>
        <td style="text-align: center;">0.095</td>
        <td style="text-align: center;">0.094</td>
        <td style="text-align: center;">0.458</td>
        <td style="text-align: center;">0.330</td>
        <td style="text-align: center;">0.319</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>imda_part3_30s_asr</strong></td>
        <td style="text-align: center;">0.213</td>
        <td style="text-align: center;">0.264</td>
        <td style="text-align: center; background-color: #06a2a2;">0.227</td>
        <td style="text-align: center;"><strong><u>0.196</u></strong></td>
        <td style="text-align: center;">0.211</td>
        <td style="text-align: center;">0.320</td>
        <td style="text-align: center;">0.438</td>
        <td style="text-align: center;">0.475</td>
        <td style="text-align: center;">0.535</td>
        <td style="text-align: center;">0.681</td>
        <td style="text-align: center;">0.281</td>
        <td style="text-align: center;">0.277</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>imda_part4_30s_asr</strong></td>
        <td style="text-align: center;">0.297</td>
        <td style="text-align: center;">0.360</td>
        <td style="text-align: center; background-color: #06a2a2;">0.295</td>
        <td style="text-align: center;"><strong><u>0.246</u></strong></td>
        <td style="text-align: center;">0.271</td>
        <td style="text-align: center;">0.503</td>
        <td style="text-align: center;">1.470</td>
        <td style="text-align: center;">1.250</td>
        <td style="text-align: center;">1.303</td>
        <td style="text-align: center;">0.787</td>
        <td style="text-align: center;">0.459</td>
        <td style="text-align: center;">0.458</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>imda_part5_30s_asr</strong></td>
        <td style="text-align: center;">0.154</td>
        <td style="text-align: center;">0.202</td>
        <td style="text-align: center; background-color: #06a2a2;">0.168</td>
        <td style="text-align: center;"><strong><u>0.140</u></strong></td>
        <td style="text-align: center;">0.149</td>
        <td style="text-align: center;">0.237</td>
        <td style="text-align: center;">0.239</td>
        <td style="text-align: center;">0.280</td>
        <td style="text-align: center;">0.374</td>
        <td style="text-align: center;">0.375</td>
        <td style="text-align: center;">0.218</td>
        <td style="text-align: center;">0.214</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>imda_part6_30s_asr</strong></td>
        <td style="text-align: center;">0.109</td>
        <td style="text-align: center;">0.149</td>
        <td style="text-align: center; background-color: #06a2a2;">0.127</td>
        <td style="text-align: center;"><strong><u>0.099</u></strong></td>
        <td style="text-align: center;">0.110</td>
        <td style="text-align: center;">0.198</td>
        <td style="text-align: center;">0.144</td>
        <td style="text-align: center;">0.183</td>
        <td style="text-align: center;">0.275</td>
        <td style="text-align: center;">0.255</td>
        <td style="text-align: center;">0.175</td>
        <td style="text-align: center;">0.172</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>average</strong></td>
        <td style="text-align: center;">0.144</td>
        <td style="text-align: center;">0.180</td>
        <td style="text-align: center; background-color: #06a2a2;">0.169</td>
        <td style="text-align: center;"><strong><u>0.130</u></strong></td>
        <td style="text-align: center;">0.145</td>
        <td style="text-align: center;">0.274</td>
        <td style="text-align: center;">0.449</td>
        <td style="text-align: center;">0.389</td>
        <td style="text-align: center;">0.439</td>
        <td style="text-align: center;">0.441</td>
        <td style="text-align: center;">0.256</td>
        <td style="text-align: center;">0.252</td>
      </tr>
    </tbody>
  </table>
</div>

**Spoken Question Answering (SQA) results**
<div class="table*">
  <table>
    <thead>
      <tr>
        <th style="text-align: center;"><strong>dataset</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-1</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-2-3B</strong></th>
        <th style="text-align: center; background-color: #06a2a2;"><strong>MERaLiON-2-10B</strong></th>
        <th style="text-align: center;"><strong>Phi-4-multimodal-instruct</strong></th>
        <th style="text-align: center;"><strong>Qwen2.5-Omni-3B</strong></th>
        <th style="text-align: center;"><strong>Qwen2.5-Omni-7B</strong></th>
        <th style="text-align: center;"><strong>SALMONN-7B</strong></th>
        <th style="text-align: center;"><strong>cascade-whisper_v2+sealion</strong></th>
        <th style="text-align: center;"><strong>cascade-whisper_v3+llama</strong></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="text-align: center;"><strong>cn_college_listen_mcq</strong></td>
        <td style="text-align: center;">57.111</td>
        <td style="text-align: center;">66.006</td>
        <td style="text-align: center; background-color: #06a2a2;">84.588</td>
        <td style="text-align: center;">75.649</td>
        <td style="text-align: center;">81.418</td>
        <td style="text-align: center;">81.726</td>
        <td style="text-align: center;">50.815</td>
        <td style="text-align: center;"><strong><u>89.520</u></strong></td>
        <td style="text-align: center;">84.985</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>dream_tts_mcq</strong></td>
        <td style="text-align: center;">51.542</td>
        <td style="text-align: center;">61.160</td>
        <td style="text-align: center; background-color: #06a2a2;">83.325</td>
        <td style="text-align: center;">77.522</td>
        <td style="text-align: center;">69.995</td>
        <td style="text-align: center;">70.779</td>
        <td style="text-align: center;">56.560</td>
        <td style="text-align: center;">85.154</td>
        <td style="text-align: center;"><strong><u>86.200</u></strong></td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>imda_part3_30s_sqa</strong></td>
        <td style="text-align: center;">55.200</td>
        <td style="text-align: center;">52.600</td>
        <td style="text-align: center; background-color: #06a2a2;"><strong><u>59.400</u></strong></td>
        <td style="text-align: center;">55.000</td>
        <td style="text-align: center;">52.400</td>
        <td style="text-align: center;">54.200</td>
        <td style="text-align: center;">42.000</td>
        <td style="text-align: center;">51.400</td>
        <td style="text-align: center;">51.600</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>imda_part4_30s_sqa</strong></td>
        <td style="text-align: center;">50.000</td>
        <td style="text-align: center;">54.600</td>
        <td style="text-align: center; background-color: #06a2a2;"><strong><u>63.000</u></strong></td>
        <td style="text-align: center;">56.400</td>
        <td style="text-align: center;">54.400</td>
        <td style="text-align: center;">52.000</td>
        <td style="text-align: center;">35.400</td>
        <td style="text-align: center;">46.400</td>
        <td style="text-align: center;">55.600</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>imda_part5_30s_sqa</strong></td>
        <td style="text-align: center;">63.000</td>
        <td style="text-align: center;">61.400</td>
        <td style="text-align: center; background-color: #06a2a2;"><strong><u>72.000</u></strong></td>
        <td style="text-align: center;">64.600</td>
        <td style="text-align: center;">66.000</td>
        <td style="text-align: center;">62.800</td>
        <td style="text-align: center;">45.800</td>
        <td style="text-align: center;">54.600</td>
        <td style="text-align: center;">62.000</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>imda_part6_30s_sqa</strong></td>
        <td style="text-align: center;">67.400</td>
        <td style="text-align: center;">70.200</td>
        <td style="text-align: center; background-color: #06a2a2;"><strong><u>71.800</u></strong></td>
        <td style="text-align: center;"><strong><u>71.800</u></strong></td>
        <td style="text-align: center;">69.200</td>
        <td style="text-align: center;">64.600</td>
        <td style="text-align: center;">49.600</td>
        <td style="text-align: center;">62.600</td>
        <td style="text-align: center;">68.200</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>mmau_mini</strong></td>
        <td style="text-align: center;">53.100</td>
        <td style="text-align: center;">51.000</td>
        <td style="text-align: center; background-color: #06a2a2;">56.700</td>
        <td style="text-align: center;">58.800</td>
        <td style="text-align: center;"><strong><u>60.700</u></strong></td>
        <td style="text-align: center;">56.100</td>
        <td style="text-align: center;">50.600</td>
        <td style="text-align: center;">52.600</td>
        <td style="text-align: center;">55.900</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>muchomusic</strong></td>
        <td style="text-align: center;">51.348</td>
        <td style="text-align: center;">55.602</td>
        <td style="text-align: center; background-color: #06a2a2;"><strong><u>63.943</u></strong></td>
        <td style="text-align: center;">55.265</td>
        <td style="text-align: center;">59.309</td>
        <td style="text-align: center;">47.599</td>
        <td style="text-align: center;">49.705</td>
        <td style="text-align: center;">50.463</td>
        <td style="text-align: center;">56.698</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>public_sg_speech_qa</strong></td>
        <td style="text-align: center;">59.593</td>
        <td style="text-align: center;">69.477</td>
        <td style="text-align: center; background-color: #06a2a2;"><strong><u>75.029</u></strong></td>
        <td style="text-align: center;">74.186</td>
        <td style="text-align: center;">61.076</td>
        <td style="text-align: center;">61.715</td>
        <td style="text-align: center;">59.390</td>
        <td style="text-align: center;">70.930</td>
        <td style="text-align: center;">69.680</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>slue_p2_sqa5</strong></td>
        <td style="text-align: center;">86.716</td>
        <td style="text-align: center;">83.186</td>
        <td style="text-align: center; background-color: #06a2a2;"><strong><u>89.559</u></strong></td>
        <td style="text-align: center;">83.725</td>
        <td style="text-align: center;">73.873</td>
        <td style="text-align: center;">77.304</td>
        <td style="text-align: center;">80.882</td>
        <td style="text-align: center;">51.520</td>
        <td style="text-align: center;">86.961</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>spoken_squad</strong></td>
        <td style="text-align: center;">74.207</td>
        <td style="text-align: center;">81.461</td>
        <td style="text-align: center; background-color: #06a2a2;"><strong><u>89.209</u></strong></td>
        <td style="text-align: center;">83.196</td>
        <td style="text-align: center;">59.850</td>
        <td style="text-align: center;">62.867</td>
        <td style="text-align: center;">65.648</td>
        <td style="text-align: center;">57.163</td>
        <td style="text-align: center;">87.434</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>average</strong></td>
        <td style="text-align: center;">60.838</td>
        <td style="text-align: center;">64.245</td>
        <td style="text-align: center; background-color: #06a2a2;"><strong><u>73.505</u></strong></td>
        <td style="text-align: center;">68.740</td>
        <td style="text-align: center;">64.384</td>
        <td style="text-align: center;">62.881</td>
        <td style="text-align: center;">53.309</td>
        <td style="text-align: center;">61.123</td>
        <td style="text-align: center;">69.569</td>
      </tr>
    </tbody>
  </table>
</div>

**Speech Translation (ST) results**
<div class="table*">
  <table>
    <thead>
      <tr>
        <th style="text-align: center;"><strong>dataset</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-1</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-2-2B</strong></th>
        <th style="text-align: center; background-color: #06a2a2;"><strong>MERaLiON-2-9B</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-2-Whisper </strong></th>
        <th style="text-align: center;"><strong>whisper_large_v3</strong></th>
        <th style="text-align: center;"><strong>Phi-4-multimodal-instruct</strong></th>
        <th style="text-align: center;"><strong>Qwen2.5-Omni-3B</strong></th>
        <th style="text-align: center;"><strong>Qwen2.5-Omni-7B</strong></th>
        <th style="text-align: center;"><strong>SALMONN-7B</strong></th>
        <th style="text-align: center;"><strong>cascade-whisper_v2+sealion</strong></th>
        <th style="text-align: center;"><strong>cascade-whisper_v3+llama</strong></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="text-align: center;"><strong>covost2_en_id</strong></td>
        <td style="text-align: center;"><strong><u>37.058</u></strong></td>
        <td style="text-align: center;">30.658</td>
        <td style="text-align: center; background-color: #06a2a2;">36.242</td>
        <td style="text-align: center;">-</td>
        <td style="text-align: center;">-</td>
        <td style="text-align: center;">14.554</td>
        <td style="text-align: center;">22.677</td>
        <td style="text-align: center;">22.381</td>
        <td style="text-align: center;">14.193</td>
        <td style="text-align: center;">27.592</td>
        <td style="text-align: center;">10.753</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>covost2_en_ta</strong></td>
        <td style="text-align: center;"><strong><u>13.809</u></strong></td>
        <td style="text-align: center;">5.602</td>
        <td style="text-align: center; background-color: #06a2a2;">10.886</td>
        <td style="text-align: center;">-</td>
        <td style="text-align: center;">-</td>
        <td style="text-align: center;">0.148</td>
        <td style="text-align: center;">0.114</td>
        <td style="text-align: center;">0.724</td>
        <td style="text-align: center;">0.001</td>
        <td style="text-align: center;">7.475</td>
        <td style="text-align: center;">1.003</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>covost2_en_zh</strong></td>
        <td style="text-align: center;">43.963</td>
        <td style="text-align: center;">40.028</td>
        <td style="text-align: center; background-color: #06a2a2;">43.747</td>
        <td style="text-align: center;">-</td>
        <td style="text-align: center;">-</td>
        <td style="text-align: center;"><strong><u>45.480</u></strong></td>
        <td style="text-align: center;">41.390</td>
        <td style="text-align: center;">40.436</td>
        <td style="text-align: center;">33.256</td>
        <td style="text-align: center;">28.714</td>
        <td style="text-align: center;">6.090</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>covost2_id_en</strong></td>
        <td style="text-align: center;">43.374</td>
        <td style="text-align: center;">37.773</td>
        <td style="text-align: center; background-color: #06a2a2;"><strong><u>47.859</u></strong></td>
        <td style="text-align: center;">21.269</td>
        <td style="text-align: center;">44.667</td>
        <td style="text-align: center;">0.377</td>
        <td style="text-align: center;">44.702</td>
        <td style="text-align: center;">43.845</td>
        <td style="text-align: center;">27.885</td>
        <td style="text-align: center;">46.805</td>
        <td style="text-align: center;">46.797</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>covost2_ta_en</strong></td>
        <td style="text-align: center;"><strong><u>4.758</u></strong></td>
        <td style="text-align: center;">1.942</td>
        <td style="text-align: center; background-color: #06a2a2;">3.479</td>
        <td style="text-align: center;">0.022</td>
        <td style="text-align: center;">2.494</td>
        <td style="text-align: center;">0.073</td>
        <td style="text-align: center;">0.212</td>
        <td style="text-align: center;">0.057</td>
        <td style="text-align: center;">0.406</td>
        <td style="text-align: center;">2.833</td>
        <td style="text-align: center;">2.418</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>covost2_zh_en</strong></td>
        <td style="text-align: center;">19.556</td>
        <td style="text-align: center;">16.778</td>
        <td style="text-align: center; background-color: #06a2a2;">22.134</td>
        <td style="text-align: center;">12.225</td>
        <td style="text-align: center;">14.865</td>
        <td style="text-align: center;"><strong><u>22.330</u></strong></td>
        <td style="text-align: center;">21.564</td>
        <td style="text-align: center;">16.686</td>
        <td style="text-align: center;">5.176</td>
        <td style="text-align: center;">15.210</td>
        <td style="text-align: center;">14.156</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>average</strong></td>
        <td style="text-align: center;">27.086</td>
        <td style="text-align: center;">22.130</td>
        <td style="text-align: center; background-color: #06a2a2;"><strong><u>27.391</u></strong></td>
        <td style="text-align: center;">11.172</td>
        <td style="text-align: center;">20.675</td>
        <td style="text-align: center;">13.827</td>
        <td style="text-align: center;">21.777</td>
        <td style="text-align: center;">20.688</td>
        <td style="text-align: center;">13.486</td>
        <td style="text-align: center;">21.438</td>
        <td style="text-align: center;">13.536</td>
      </tr>
    </tbody>
  </table>
</div>

**Spoken Dialogue Summarization (SDS) results**
<div class="table*">
  <table>
    <thead>
      <tr>
        <th style="text-align: center;"><strong>dataset</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-1</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-2-3B</strong></th>
        <th style="text-align: center; background-color: #06a2a2;"><strong>MERaLiON-2-10B</strong></th>
        <th style="text-align: center;"><strong>Phi-4-multimodal-instruct</strong></th>
        <th style="text-align: center;"><strong>Qwen2.5-Omni-3B</strong></th>
        <th style="text-align: center;"><strong>Qwen2.5-Omni-7B</strong></th>
        <th style="text-align: center;"><strong>SALMONN-7B</strong></th>
        <th style="text-align: center;"><strong>cascade-whisper_v2+sealion</strong></th>
        <th style="text-align: center;"><strong>cascade-whisper_v3+llama</strong></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="text-align: center;"><strong>imda_part3_30s_ds</strong></td>
        <td style="text-align: center;">47.800</td>
        <td style="text-align: center;">42.200</td>
        <td style="text-align: center; background-color: #06a2a2;"><strong><u>49.800</u></strong></td>
        <td style="text-align: center;">43.600</td>
        <td style="text-align: center;">42.800</td>
        <td style="text-align: center;">39.800</td>
        <td style="text-align: center;">9.000</td>
        <td style="text-align: center;">48.400</td>
        <td style="text-align: center;">38.000</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>imda_part4_30s_ds</strong></td>
        <td style="text-align: center;">46.400</td>
        <td style="text-align: center;">40.200</td>
        <td style="text-align: center; background-color: #06a2a2;"><strong><u>46.600</u></strong></td>
        <td style="text-align: center;">42.800</td>
        <td style="text-align: center;">33.200</td>
        <td style="text-align: center;">31.600</td>
        <td style="text-align: center;">7.400</td>
        <td style="text-align: center;">45.600</td>
        <td style="text-align: center;">38.200</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>imda_part5_30s_ds</strong></td>
        <td style="text-align: center;">54.600</td>
        <td style="text-align: center;">51.800</td>
        <td style="text-align: center; background-color: #06a2a2;">55.400</td>
        <td style="text-align: center;"><strong><u>55.600</u></strong></td>
        <td style="text-align: center;">52.200</td>
        <td style="text-align: center;">42.800</td>
        <td style="text-align: center;">16.000</td>
        <td style="text-align: center;">53.400</td>
        <td style="text-align: center;">46.200</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>imda_part6_30s_ds</strong></td>
        <td style="text-align: center;"><strong><u>65.600</u></strong></td>
        <td style="text-align: center;">60.000</td>
        <td style="text-align: center; background-color: #06a2a2;">60.600</td>
        <td style="text-align: center;">61.000</td>
        <td style="text-align: center;">58.800</td>
        <td style="text-align: center;">58.400</td>
        <td style="text-align: center;">25.200</td>
        <td style="text-align: center;">56.600</td>
        <td style="text-align: center;">61.000</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>average</strong></td>
        <td style="text-align: center;"><strong><u>53.600</u></strong></td>
        <td style="text-align: center;">48.550</td>
        <td style="text-align: center; background-color: #06a2a2;">53.100</td>
        <td style="text-align: center;">50.750</td>
        <td style="text-align: center;">46.750</td>
        <td style="text-align: center;">43.150</td>
        <td style="text-align: center;">14.400</td>
        <td style="text-align: center;">51.000</td>
        <td style="text-align: center;">45.850</td>
      </tr>
    </tbody>
  </table>
</div>

**Speech instruction (SI) results**
<div class="table*">
  <table>
    <thead>
      <tr>
        <th style="text-align: center;"><strong>dataset</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-1</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-2-3B</strong></th>
        <th style="text-align: center; background-color: #06a2a2;"><strong>MERaLiON-2-10B</strong></th>
        <th style="text-align: center;"><strong>Phi-4-multimodal-instruct</strong></th>
        <th style="text-align: center;"><strong>Qwen2.5-Omni-3B</strong></th>
        <th style="text-align: center;"><strong>Qwen2.5-Omni-7B</strong></th>
        <th style="text-align: center;"><strong>SALMONN-7B</strong></th>
        <th style="text-align: center;"><strong>cascade-whisper_v2+sealion</strong></th>
        <th style="text-align: center;"><strong>cascade-whisper_v3+llama</strong></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="text-align: center;"><strong>alpaca_audio</strong></td>
        <td style="text-align: center;"><strong><u>75.200</u></strong></td>
        <td style="text-align: center;">25.600</td>
        <td style="text-align: center; background-color: #06a2a2;">74.200</td>
        <td style="text-align: center;">33.400</td>
        <td style="text-align: center;">64.000</td>
        <td style="text-align: center;">59.200</td>
        <td style="text-align: center;">10.400</td>
        <td style="text-align: center;">67.000</td>
        <td style="text-align: center;">69.400</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>openhermes_audio</strong></td>
        <td style="text-align: center;">66.400</td>
        <td style="text-align: center;">12.600</td>
        <td style="text-align: center; background-color: #06a2a2;">66.200</td>
        <td style="text-align: center;">39.000</td>
        <td style="text-align: center;">66.000</td>
        <td style="text-align: center;">57.400</td>
        <td style="text-align: center;">15.400</td>
        <td style="text-align: center;"><strong><u>78.800</u></strong></td>
        <td style="text-align: center;">62.800</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>average</strong></td>
        <td style="text-align: center;">70.800</td>
        <td style="text-align: center;">19.100</td>
        <td style="text-align: center; background-color: #06a2a2;">70.200</td>
        <td style="text-align: center;">36.200</td>
        <td style="text-align: center;">65.000</td>
        <td style="text-align: center;">58.300</td>
        <td style="text-align: center;">12.900</td>
        <td style="text-align: center;"><strong><u>72.900</u></strong></td>
        <td style="text-align: center;">66.100</td>
      </tr>
    </tbody>
  </table>
</div>

**Audio Captioning (AC) results**
<div class="table*">
  <table>
    <thead>
      <tr>
        <th style="text-align: center;"><strong>dataset</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-1</strong></th>
        <th style="text-align: center; "><strong>MERaLiON-2-3B</strong></th>
        <th style="text-align: center; background-color: #06a2a2;"><strong>MERaLiON-2-10B</strong></th>
        <th style="text-align: center;"><strong>Phi-4-multimodal-instruct</strong></th>
        <th style="text-align: center;"><strong>Qwen2.5-Omni-3B</strong></th>
        <th style="text-align: center;"><strong>Qwen2.5-Omni-7B</strong></th>
        <th style="text-align: center;"><strong>SALMONN-7B</strong></th>
        <th style="text-align: center;"><strong>cascade-whisper_v2+sealion</strong></th>
        <th style="text-align: center;"><strong>cascade-whisper_v3+llama</strong></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="text-align: center;"><strong>audiocaps</strong></td>
        <td style="text-align: center;">39.386</td>
        <td style="text-align: center;">35.077</td>
        <td style="text-align: center; background-color: #06a2a2;">36.041</td>
        <td style="text-align: center;">33.595</td>
        <td style="text-align: center;"><strong><u>43.695</u></strong></td>
        <td style="text-align: center;">37.700</td>
        <td style="text-align: center;">35.241</td>
        <td style="text-align: center;">2.455</td>
        <td style="text-align: center;">2.514</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>wavcaps</strong></td>
        <td style="text-align: center;">34.566</td>
        <td style="text-align: center;">31.410</td>
        <td style="text-align: center; background-color: #06a2a2;"><strong><u>35.168</u></strong></td>
        <td style="text-align: center;">28.069</td>
        <td style="text-align: center;">34.705</td>
        <td style="text-align: center;">26.092</td>
        <td style="text-align: center;">22.520</td>
        <td style="text-align: center;">3.827</td>
        <td style="text-align: center;">3.318</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>average</strong></td>
        <td style="text-align: center;">36.976</td>
        <td style="text-align: center;">33.244</td>
        <td style="text-align: center; background-color: #06a2a2;">35.604</td>
        <td style="text-align: center;">30.832</td>
        <td style="text-align: center;"><strong><u>39.200</u></strong></td>
        <td style="text-align: center;">31.896</td>
        <td style="text-align: center;">28.881</td>
        <td style="text-align: center;">3.141</td>
        <td style="text-align: center;">2.916</td>
      </tr>
    </tbody>
  </table>
</div>

**Accent Recognition (AR) results**
<div class="table*">
  <table>
    <thead>
      <tr>
        <th style="text-align: center;"><strong>dataset</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-1</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-2-3B</strong></th>
        <th style="text-align: center; background-color: #06a2a2;"><strong>MERaLiON-2-10B</strong></th>
        <th style="text-align: center;"><strong>Phi-4-multimodal-instruct</strong></th>
        <th style="text-align: center;"><strong>Qwen2.5-Omni-3B</strong></th>
        <th style="text-align: center;"><strong>Qwen2.5-Omni-7B</strong></th>
        <th style="text-align: center;"><strong>SALMONN-7B</strong></th>
        <th style="text-align: center;"><strong>cascade-whisper_v2+sealion</strong></th>
        <th style="text-align: center;"><strong>cascade-whisper_v3+llama</strong></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="text-align: center;"><strong>voxceleb_accent</strong></td>
        <td style="text-align: center;">47.066</td>
        <td style="text-align: center;"><strong><u>66.598</u></strong></td>
        <td style="text-align: center; background-color: #06a2a2;">40.788</td>
        <td style="text-align: center;">2.626</td>
        <td style="text-align: center;">0.903</td>
        <td style="text-align: center;">1.662</td>
        <td style="text-align: center;">31.699</td>
        <td style="text-align: center;">28.006</td>
        <td style="text-align: center;">40.295</td>
      </tr>
    </tbody>
  </table>
</div>

**Audio-Scene Question Answering (ASQA) results**
<div class="table*">
  <table>
    <thead>
      <tr>
        <th style="text-align: center;"><strong>dataset</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-1</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-2-3B</strong></th>
        <th style="text-align: center; background-color: #06a2a2;"><strong>MERaLiON-2-10B</strong></th>
        <th style="text-align: center;"><strong>Phi-4-multimodal-instruct</strong></th>
        <th style="text-align: center;"><strong>Qwen2.5-Omni-3B</strong></th>
        <th style="text-align: center;"><strong>Qwen2.5-Omni-7B</strong></th>
        <th style="text-align: center;"><strong>SALMONN-7B</strong></th>
        <th style="text-align: center;"><strong>cascade-whisper_v2+sealion</strong></th>
        <th style="text-align: center;"><strong>cascade-whisper_v3+llama</strong></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="text-align: center;"><strong>audiocaps_qa</strong></td>
        <td style="text-align: center;">48.818</td>
        <td style="text-align: center;">44.792</td>
        <td style="text-align: center; background-color: #06a2a2;">50.351</td>
        <td style="text-align: center;">40.319</td>
        <td style="text-align: center;">48.562</td>
        <td style="text-align: center;"><strong><u>50.415</u></strong></td>
        <td style="text-align: center;">50.351</td>
        <td style="text-align: center;">17.444</td>
        <td style="text-align: center;">17.061</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>clotho_aqa</strong></td>
        <td style="text-align: center;"><strong><u>62.674</u></strong></td>
        <td style="text-align: center;">50.540</td>
        <td style="text-align: center; background-color: #06a2a2;">58.201</td>
        <td style="text-align: center;">48.371</td>
        <td style="text-align: center;">52.649</td>
        <td style="text-align: center;">46.592</td>
        <td style="text-align: center;">58.192</td>
        <td style="text-align: center;">22.674</td>
        <td style="text-align: center;">29.820</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>wavcaps_qa</strong></td>
        <td style="text-align: center;">45.132</td>
        <td style="text-align: center;">43.092</td>
        <td style="text-align: center; background-color: #06a2a2;">44.868</td>
        <td style="text-align: center;">37.961</td>
        <td style="text-align: center;">43.158</td>
        <td style="text-align: center;">40.000</td>
        <td style="text-align: center;"><strong><u>46.908</u></strong></td>
        <td style="text-align: center;">14.013</td>
        <td style="text-align: center;">18.750</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>average</strong></td>
        <td style="text-align: center;"><strong><u>52.208</u></strong></td>
        <td style="text-align: center;">46.141</td>
        <td style="text-align: center; background-color: #06a2a2;">51.140</td>
        <td style="text-align: center;">42.217</td>
        <td style="text-align: center;">48.123</td>
        <td style="text-align: center;">45.669</td>
        <td style="text-align: center;">51.817</td>
        <td style="text-align: center;">18.044</td>
        <td style="text-align: center;">21.877</td>
      </tr>
    </tbody>
  </table>
</div>

**Emotion Recognition (ER) results**
<div class="table*">
  <table>
    <thead>
      <tr>
        <th style="text-align: center;"><strong>dataset</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-1</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-2-3B</strong></th>
        <th style="text-align: center; background-color: #06a2a2;"><strong>MERaLiON-2-10B</strong></th>
        <th style="text-align: center;"><strong>Phi-4-multimodal-instruct</strong></th>
        <th style="text-align: center;"><strong>Qwen2.5-Omni-3B</strong></th>
        <th style="text-align: center;"><strong>Qwen2.5-Omni-7B</strong></th>
        <th style="text-align: center;"><strong>SALMONN-7B</strong></th>
        <th style="text-align: center;"><strong>cascade-whisper_v2+sealion</strong></th>
        <th style="text-align: center;"><strong>cascade-whisper_v3+llama</strong></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="text-align: center;"><strong>iemocap_emotion</strong></td>
        <td style="text-align: center;">49.104</td>
        <td style="text-align: center;">51.394</td>
        <td style="text-align: center; background-color: #06a2a2;"><strong><u>62.550</u></strong></td>
        <td style="text-align: center;">32.072</td>
        <td style="text-align: center;">34.363</td>
        <td style="text-align: center;">36.554</td>
        <td style="text-align: center;">26.195</td>
        <td style="text-align: center;">41.982</td>
        <td style="text-align: center;">46.912</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>meld_emotion</strong></td>
        <td style="text-align: center;">44.176</td>
        <td style="text-align: center;">52.146</td>
        <td style="text-align: center; background-color: #06a2a2;"><strong><u>59.808</u></strong></td>
        <td style="text-align: center;">40.843</td>
        <td style="text-align: center;">34.330</td>
        <td style="text-align: center;">30.077</td>
        <td style="text-align: center;">32.299</td>
        <td style="text-align: center;">44.272</td>
        <td style="text-align: center;">49.425</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>meld_sentiment</strong></td>
        <td style="text-align: center;">52.452</td>
        <td style="text-align: center;">58.582</td>
        <td style="text-align: center; background-color: #06a2a2;"><strong><u>68.851</u></strong></td>
        <td style="text-align: center;">49.119</td>
        <td style="text-align: center;">30.421</td>
        <td style="text-align: center;">27.778</td>
        <td style="text-align: center;">42.261</td>
        <td style="text-align: center;">58.391</td>
        <td style="text-align: center;">56.475</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>average</strong></td>
        <td style="text-align: center;">48.577</td>
        <td style="text-align: center;">54.041</td>
        <td style="text-align: center; background-color: #06a2a2;"><strong><u>63.736</u></strong></td>
        <td style="text-align: center;">40.678</td>
        <td style="text-align: center;">33.038</td>
        <td style="text-align: center;">31.469</td>
        <td style="text-align: center;">33.585</td>
        <td style="text-align: center;">48.215</td>
        <td style="text-align: center;">50.938</td>
      </tr>
    </tbody>
  </table>
</div>

**Gender Recognition (GR) results**
<div class="table*">
  <table>
    <thead>
      <tr>
        <th style="text-align: center;"><strong>dataset</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-1</strong></th>
        <th style="text-align: center;"><strong>MERaLiON-2-3B</strong></th>
        <th style="text-align: center; background-color: #06a2a2;"><strong>MERaLiON-2-10B</strong></th>
        <th style="text-align: center;"><strong>Phi-4-multimodal-instruct</strong></th>
        <th style="text-align: center;"><strong>Qwen2.5-Omni-3B</strong></th>
        <th style="text-align: center;"><strong>Qwen2.5-Omni-7B</strong></th>
        <th style="text-align: center;"><strong>SALMONN-7B</strong></th>
        <th style="text-align: center;"><strong>cascade-whisper_v2+sealion</strong></th>
        <th style="text-align: center;"><strong>cascade-whisper_v3+llama</strong></th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="text-align: center;"><strong>iemocap_gender</strong></td>
        <td style="text-align: center;"><strong><u>94.622</u></strong></td>
        <td style="text-align: center;">87.928</td>
        <td style="text-align: center; background-color: #06a2a2;">92.968</td>
        <td style="text-align: center;">46.853</td>
        <td style="text-align: center;">62.948</td>
        <td style="text-align: center;">43.367</td>
        <td style="text-align: center;">80.199</td>
        <td style="text-align: center;">12.211</td>
        <td style="text-align: center;">44.382</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>voxceleb_gender</strong></td>
        <td style="text-align: center;"><strong><u>99.733</u></strong></td>
        <td style="text-align: center;">99.692</td>
        <td style="text-align: center; background-color: #06a2a2;">97.251</td>
        <td style="text-align: center;">94.584</td>
        <td style="text-align: center;">32.786</td>
        <td style="text-align: center;">54.083</td>
        <td style="text-align: center;">88.531</td>
        <td style="text-align: center;">26.631</td>
        <td style="text-align: center;">69.696</td>
      </tr>
      <tr>
        <td style="text-align: center;"><strong>average</strong></td>
        <td style="text-align: center;"><strong><u>97.177</u></strong></td>
        <td style="text-align: center;">93.810</td>
        <td style="text-align: center; background-color: #06a2a2;">95.109</td>
        <td style="text-align: center;">70.718</td>
        <td style="text-align: center;">47.867</td>
        <td style="text-align: center;">48.725</td>
        <td style="text-align: center;">84.365</td>
        <td style="text-align: center;">19.421</td>
        <td style="text-align: center;">57.039</td>
      </tr>
    </tbody>
  </table>
</div>



## 🔧 How to Use
> [!WARNING]
> **Out of Scope use**: This model is not intended for use in tool calling, math, and coding tasks.

### Requirements
We suggest to use Python version, transformers version, PyTorch version. See GitHub() for installation instructions.

### Inputs

**Audio**
- To keep the stable performance, the maximum audio length is suggested to be 300 seconds at 16,000 Hz sampling rate.
- For ASR tasks, the maximum audio length is suggested to be 30 seconds at 16,000.

**Prompt examples**  
<pre>
Answer in as many details as possible, including paralinguistic.
Instruction: &lt;TextHere&gt;
Follow the text instruction based on the following audio: &lt;SpeechHere&gt;
</pre>

<pre>
Your name is MERaLiON, a powerful speech-text multimodal model designed to analyze and understand audio content.
Your answer should include as many details as possible, including paralinguistics.
Instruction: &lt;TextHere&gt; 
Follow the text instruction based on the following audio: &lt;SpeechHere&gt;
</pre>

### Load and Use the Model

```python
import torch
import librosa
from concurrent.futures import ThreadPoolExecutor
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor

repo_id = "MERaLiON/MERaLiON-2-10B"
device = "cuda"

# Load the processor and model
processor = AutoProcessor.from_pretrained(
    repo_id, 
    trust_remote_code=True,
    )
model = AutoModelForSpeechSeq2Seq.from_pretrained(
    repo_id,
    use_safetensors=True,
    trust_remote_code=True,
    attn_implementation="flash_attention_2",
    torch_dtype=torch.bfloat16
).to(device)

# Construct prompt
prompt = "Answer in as many details as possible, including paralinguistic.\nInstruction: {query} \nFollow the text instruction based on the following audio: <SpeechHere>"
query_list = ["query_1", "query_2", "..."]

conversation = [
    [{"role": "user", "content": prompt.format(query=prompt)}]

    for prompt in query_list
]

chat_prompt = processor.tokenizer.apply_chat_template(
    conversation=conversation,
    tokenize=False,
    add_generation_prompt=True
)

# Audio Inputs ------
# Option 1: Load audio from a local file
def load_audio(path):
    audio, _ = librosa.load(path, sr=16000)
    return audio

audio_paths = ["/path/to/audio1.wav", "/path/to/audio2.wav", "..."]
with ThreadPoolExecutor() as executor:
    audio_array = list(executor.map(load_audio, audio_paths))

# Option 2: Using HuggingFace Dataset directly, make sure sr=16000
# audio_array = batch_ds['audio']['array']
# ------

# Feed to processor
inputs = processor(text=chat_prompt, audios=audio_array).to(device)

# Run inference
outputs = model.generate(**inputs, max_new_tokens=256)
generated_ids = outputs[:, inputs['input_ids'].size(1):]
response = processor.batch_decode(generated_ids, skip_special_tokens=True)
print(response)

```

### vLLM inference
To maximize throughput for long-form audio-text interactions, we support inference using vLLM. Please refer to the GitHub instructions for vLLM-specific setup and deployment scripts.


## ⚠️ Disclaimer

The current MERaLiON-2 has not been specifically aligned for safety and may generate content that is inappropriate, offensive, or harmful. Developers and users are responsible for performing their own safety fine-tuning and implementing necessary security measures. The authors shall not be held liable for any claims, damages, or other liabilities arising from the use of the released models, weights, or code.

### Compute and Infrastructure

MERaLiON-2 was trained on the [**ASPIRE 2A+**](https://help.nscc.sg/aspire2aplus/about/) Supercomputer Cluster, provided by [**National Supercomputing Centre (NSCC)**](https://www.nscc.sg/), Singapore. ASPIRE 2A+ cluster provides multiple H100 nodes, with each compute node equipped with 8 Nvidia H100 GPUs, 2 TB of RAM, and 30 TB of locally attached NVMe storage. These nodes are interconnected via a rail-optimised, full fat-tree topology, utilising 400 Gb/s NDR InfiniBand cables. Additionally, the cluster incorporates a 2.5 PB SSD-based Lustre file system, linked to the H100 nodes through high-speed InfiniBand connections. 

With a global batch size of 768, we trained the current release of MERaLiON-2 for around 200k steps, which took around 2 days to complete using 16 nodes, 128 H100 GPUs.

## 📚 Citation

If you find our work useful, please cite our papers:

```
@misc{he2024meralionaudiollmtechnicalreport,
      title={MERaLiON-AudioLLM: Bridging Audio and Language with Large Language Models}, 
      author={{MERaLiON Team}},
      year={2024},
      eprint={2412.09818},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.09818}, 
}
```

```
@article{wang2024audiobench,
    title={AudioBench: A Universal Benchmark for Audio Large Language Models},
    author={Wang, Bin and Zou, Xunlong and Lin, Geyu and Sun, Shuo and Liu, Zhuohan and Zhang, Wenyu and Liu, Zhengyuan and Aw, AiTi and Chen, Nancy F},
    journal={NAACL},
    year={2025}
    }
```

```
@article{wang2025advancing,
    title={Advancing Singlish Understanding: Bridging the Gap with Datasets and Multimodal Models},
    author={Wang, Bin and Zou, Xunlong and Sun, Shuo and Zhang, Wenyu and He, Yingxu and Liu, Zhuohan and Wei, Chengwei and Chen, Nancy F and Aw, AiTi},
    journal={arXiv preprint arXiv:2501.01034},
    year={2025}
    }
```

```
@article{zhang2024mowe,
    title={MoWE-Audio: Multitask AudioLLMs with Mixture of Weak Encoders},
    author={Zhang, Wenyu and Sun, Shuo and Wang, Bin and Zou, Xunlong and Liu, Zhuohan and He, Yingxu and Lin, Geyu and Chen, Nancy F and Aw, Ai Ti},
    journal={ICASSP},
    year={2025}
    }
```