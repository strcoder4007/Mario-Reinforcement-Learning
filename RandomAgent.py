import retro
import gym

env = retro.make(game="SuperMarioBros-Nes")
obs = env.reset()

print(obs.shape)

done = False

while not done:
    obs, rew, done, info = env.step(env.action_space.sample())
    env.render()


env.close()