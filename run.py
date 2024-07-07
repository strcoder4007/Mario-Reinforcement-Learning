import retro
from stable_baselines3 import PPO
from stable_baselines3.common.atari_wrappers import MaxAndSkipEnv

model = PPO.load("tmp/best_model.zip")

def main():
    env = retro.make(game="SuperMarioBros-Nes")
    env = MaxAndSkipEnv(env, 4)

    obs = env.reset()
    done = False

    last5Rewards = []

    yesprint = 0

    while not done: 
        action, state = model.predict(obs)
        obs, reward, done, info = env.step(action)
        if len(last5Rewards) == 10:
            last5Rewards = []
        last5Rewards.append(reward)
        if yesprint%10 == 0:
            print(f"min reward: {min(last5Rewards)} |||| max reward: {max(last5Rewards)}")
        yesprint += 1
        env.render()


if __name__ == "__main__":
    main()