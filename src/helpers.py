import os
import shutil


def create_or_recreate_dir(dir_path):
    if os.path.isdir(dir_path):
        shutil.rmtree(dir_path)
    os.makedirs(dir_path)


def create_if_none(dir_path):
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)


def validate_exists_and_dir(dir_path, arg_name):
    if not os.path.exists(dir_path):
        raise ValueError("{0} {1} does not exist".format(arg_name, dir_path))

    if not os.path.isdir(dir_path):
        raise ValueError("{0} {1} is not a dir".format(arg_name, dir_path))


def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)


def seed():
    from random import seed
    seed(1)
    import numpy.random
    numpy.random.seed(2)
    from tensorflow import set_random_seed
    set_random_seed(3)
