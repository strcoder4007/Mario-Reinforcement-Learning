import retro
import imageio
import numpy as np
import cv2
from stable_baselines3 import PPO
from stable_baselines3.common.atari_wrappers import MaxAndSkipEnv

model = PPO.load("tmp/best_model.zip")

def main():
    env = retro.make(game="SuperMarioBros-Nes")
    env = MaxAndSkipEnv(env, 4)

    obs = env.reset()
    done = False

    images = []
    img = env.render(mode="rgb_array")

    last5Rewards = []

    while not done:
        images.append(img)
        action, state = model.predict(obs)
        obs, reward, done, info = env.step(action)

        # env.render()
        img = env.render(mode="rgb_array")


    
    imageio.mimsave("mario_ppo.gif", [np.array(img) for i, img in enumerate(images) if i%2 == 0], fps=29)


if __name__ == "__main__":
    main()