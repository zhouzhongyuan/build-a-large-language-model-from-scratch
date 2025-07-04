# Chapter 2 Working with text data



1. Preparing text for large language model training
2. Splitting text into word and subword tokens
3. Byte pair encoding as a more advanced way of tokenizing text
4. Sampling training examples with ad sliding window approach
5. Converting tokens into vectors that feed into a large language model



During the **pre-training stage**, LLMs **process** text **one word at a time**.  

Training LLMs with millions to billions of parameters using a next-word prediction task **yields** models with impressive capabilities.

![image-20250701122446996](/Users/y/project/ai/build-a-large-language-model-from-scratch/chapter-2-working-with-text-data/assets/image-20250701122446996.png)

**Why we need word embeddings?**

Large Language Model, as a type of deep neural network, **cannot** process raw text **directly**.

Since text is **categorical**, it isn't compatible  with the mathematical operations used to implement and train neural networks.

Therefore, we need a way to represent words as **continuous-valued vectors**.

**What is embedding?**

Convert data into  a vector format. The data types can be video, audio and text.

**What is the main idea of Word2Vec?**

Words that appear in **similar contexts** tend to have **similar meanings**.

Consequently, when projected into **two-dimensional** word embeddings for **visualization** purposes, similar terms are clustered together.

Word embeddings can have varying **dimensions**, **from one to thousands**.

**What are the dimensions of GPT-2?**

The smallest GPT-2 models (117M and 125M parameters) use an embedding size of **768** dimensions to provide concrete examples. 

The largest GPT-3 model (175B parameters) uses an embedding size of **12,288** dimensions.

## 2.3 Converting tokens into token IDs



To map previously generated **tokens** into **token IDs**, we have to build a **vocabulary** first.

This vocabulary defines **how** we map each **unique word** and special character to a **unique integer**.

![image-20250701215534138](/Users/y/project/ai/build-a-large-language-model-from-scratch/chapter-2-working-with-text-data/assets/image-20250701215534138.png)

## 2.6 Data sampling with a Sliding window

Generate the **input**–**target** pairs

![image-20250703225815630](/Users/y/project/ai/build-a-large-language-model-from-scratch/chapter-2-working-with-text-data/assets/image-20250703225815630.png)

**inputs** and **targets** as PyTorch tensors,  which can be thought of as multidimensional arrays.

## 2.7 Creating token embedding

 Convert the **token ID**s into **embedding vector**s

![image-20250703230409287](/Users/y/project/ai/build-a-large-language-model-from-scratch/chapter-2-working-with-text-data/assets/image-20250703230409287.png)

We must **initialize** these **embedding weight**s with **random values.**

**A continuous vector representation**, aka **embedding**

**Just Generate random matrix.** Don't know why.

## 2.8 Encoding word positions

However, a minor **shortcoming** of LLMs is that their self-attention mechanism (see chapter 3) **doesn’t** have a **notion of position or order** for the tokens within a sequence. The way the previously introduced embedding layer works is that the same token ID always gets mapped to the same vector representation, regardless of where the token ID is positioned in the input sequence

![image-20250703232431143](/Users/y/project/ai/build-a-large-language-model-from-scratch/chapter-2-working-with-text-data/assets/image-20250703232431143.png)