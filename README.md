# Mario Reinforcement Learning

This project aims to train an artificial intelligence (AI) agent to achieve proficiency in playing Super Mario Bros. through the application of reinforcement learning techniques. Specifically, it utilizes the Proximal Policy Optimization (PPO) algorithm from Stable Baselines 3. 

![Playing GIF 1](/images/mario_ppo.gif)

The AI agent learns to navigate the iconic game environment, surmount obstacles, and strategically collect rewards such as coins and power-ups. This project not only demonstrates the capabilities of modern reinforcement learning algorithms but also explores their application in mastering complex, real-time video game scenarios.

## Training

It total it took around 10 hours of training on a local Nvidia RTX 4070 Ti Super (16GB) for 2.5 million timesteps. 

![Training Photo 1](/images/mario_ppo_training_1.png)
![Training Photo 2](/images/mario_ppo_training_2.png)


## Installation

To install the required dependencies, you can use `pip` with the provided `requirements.txt` file.

1. Clone the repository:

   ```bash
   git clone https://github.com/strcoder4007/Mario-Reinforcement-Learning.git
   cd Mario-Reinforcement-Learning
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   This command will install all necessary packages including `gym`, `gym-retro`, and `stable-baselines3`.

3. Import the ROM: The ROM for Super Mario Bros. can be found in the repo itself, use the following command to import it into gym-retro:

   ```bash
   python -m retro.import
   ```

## Pre-trained Model

Checkpoint for a trained Mario: https://drive.google.com/file/d/1RRwhSMUrpBBRyAsfHLPGt1rlYFoiuus2/view?usp=sharing


## Usage

1. After installing the dependencies, you can train the agent by running:

   ```bash
   python train.py
   ```

   This command will start the training process using the PPO algorithm.
   After/during training the best model will be saved in `/tmp/` directory.

2. Monitor training progress and visualize results using Tensorboard visualizations. Logs are stored in the `board` folder. Use it by running:

    ```bash
    tensorboard --logdir "board"
    ```

3. You can watch the agent playing the game using the `best_model.zip` in `/tmp/` directory by running:

    ```bash
    python run.py
    ```

## Credits

- [Stable Baselines 3](https://github.com/DLR-RM/stable-baselines3): For providing efficient implementations of reinforcement learning algorithms.
- [OpenAI Gym](https://github.com/openai/gym) and [gym-retro](https://github.com/openai/retro): For providing the environments to train and test the AI agent.
- Nintendo: For creating the classic game Super Mario Bros.

---
