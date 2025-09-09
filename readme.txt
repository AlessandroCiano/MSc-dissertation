Project Title: Suicide risk prediction in social media using
Machine Learning and Large Language Models

This repository contains the code and experiments conducted.

Project Structure
The repository is organized as follows:

.
├── preprocessing.ipynb
└── code
    ├── func.py
    ├── K-fold
    │   └── {loss_function}--{learning_rate}
    │       ├── ...
    │       └── large-cross-entropy--5e-5
    │           ├── ... (files for 5-fold cross-validation runs)
    │           └── ...-alldata.py (final model finetuning on all data)
    └── NO-fold
        ├── ... (scripts for LLM prompting)
        └── ... (scripts for pseudo-labelling)

Key Components
1. Data Preprocessing
preprocessing.ipynb: A Jupyter Notebook located in the root directory. This notebook contains all the steps used to preprocess the raw data for the models. Note: The dataset itself is not included in this repository.

2. Core Code
code/func.py: This is a crucial script containing shared utility functions and prompts that are imported and used across various models and experiments, particularly for the LLM prompting phase. Other .py files in the code directory are preliminary tests and can be disregarded.

3. Model Fine-Tuning (K-Fold Cross-Validation)
code/K-fold/: This directory houses all experiments related to the fine-tuning of the RoBERTa model using k-fold cross-validation.

Subdirectories: The subdirectories are named using the convention {loss_function}--{learning_rate} to clearly identify the hyperparameters used for each experiment (e.g., large-cross-entropy--5e-5).

Final Model Training: Within these subdirectories, files with the suffix all or alldata signify the final stage of fine-tuning. In this stage, the best-performing model architecture was trained on the entire training dataset without a separate validation set.

Iterative Fine-Tuning: Some folders may contain a nested shell structure, indicating further fine-tuning experiments that were performed based on a previous model's checkpoint.

4. LLM Prompting and Pseudo-Labelling
code/NO-fold/: This directory contains the scripts that do not use a cross-validation structure. Its primary purpose includes:

Scripts for prompting various Large Language Models (LLMs).

Code that combines the outputs from the LLMs to generate pseudo-labels for subsequent experiments.

Getting Started
To replicate the results or run the experiments, follow these general steps:

Prerequisites: Ensure you have Python and the necessary libraries installed. It is recommended to create a requirements.txt file with all dependencies.

pip install -r requirements.txt

Data: The necessary raw data can be obtained contacting "hialex.li@connect.polyu.hk" directly, placing "xinhong.chen@my.cityu.edu.hk" in CC. It will be required to sign a DUA that they will provide.

Preprocessing: Run the preprocessing.ipynb notebook to process the data and prepare it for the models.

Run Experiments: Navigate to the relevant experiment directory (code/K-fold or code/NO-fold) and execute the desired Python scripts.
