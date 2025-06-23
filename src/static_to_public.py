import os
import shutil


def static_to_public(path_from_copy, path_to_paste):

    if not os.path.exists(path_to_paste):
        os.mkdir(path_to_paste)

    for item in os.listdir(path = path_from_copy):
        if os.path.isfile(os.path.join(path_from_copy, item)):
            shutil.copy(os.path.join(path_from_copy, item), path_to_paste)
        else:
            static_to_public(os.path.join(path_from_copy, item), f"{path_to_paste}/{item}")
