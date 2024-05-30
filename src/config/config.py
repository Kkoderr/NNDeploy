import os
import pathlib

NUM_INPUTS = 2
NUM_LAYERS = 3
P = [NUM_INPUTS,2,1]

f = [None, "Linear", "Sigmoid"]

LOSS_FUNCTION = "Mean Squared Error"
MINI_BATCH_SIZE = 1

PACKAGE_ROOT = pathlib.Path(src.__file__).resolve().parent
