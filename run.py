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
        resized_image = cv2.resize(img, (480, 480))
        resized_image = cv2.cvtColor(resized_image, cv2.COLOR_RGB2BGR)
        cv2.imshow("Frame", resized_image)
        img = env.render(mode="rgb_array")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        

    imageio.mimsave("mario_ppo.gif", [np.array(img) for i, img in enumerate(images) if i%2 == 0], fps=29)
    env.close()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()