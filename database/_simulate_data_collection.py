"""
Simulates data collection process. Our results are that we have npz files in our top-level `data` folder.

This file isn't meant to be "used" or even "run" except for on initialization of the project.
"""

import torchvision.datasets as tfds
import torchvision.transforms as transforms
import numpy as np
import psycopg2


def investigate_data(base):
    train_set = tfds.FashionMNIST("../data/", download=True,
                                  transform=transforms.Compose([transforms.ToTensor()]),

                                  )
    test_set = tfds.FashionMNIST("../data/", download=True, train=False,
                                 transform=transforms.Compose([transforms.ToTensor()])
                                 )
    def generate_ds(iterable_ds, prefix="train"):
        accum_x = []
        accum_y = []
        counter = 0
        for x, y in iterable_ds:
            x = x.detach().numpy()
            accum_x.append(x)
            accum_y.append(y)

            if len(accum_y) >= 10_000:
                f_name = f"{base}{prefix}_fmnist_{counter}_{(counter + 1) * 10_000}.npz"
                np.savez(f_name, x=accum_x, y=accum_y)

                accum_y = []
                accum_x = []
                counter += 1
    generate_ds(train_set)
    generate_ds(test_set, "test")

if __name__ == "__main__":
    base = "../data/sourced_data/"
    investigate_data(base)
