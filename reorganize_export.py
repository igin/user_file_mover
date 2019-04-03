import os
import shutil
import sys

def move_user_files_to_combined_directory(input_directory, output_dir, file_prefix=None):
    if file_prefix is None:
        file_prefix = os.path.basename(input_directory)

    for user_id in os.listdir(input_directory):
        if user_id[0] == '.':
            continue
        output_user_dir = os.path.join(output_dir, user_id)
        try:
            os.makedirs(output_user_dir)
        except Exception as e:
            pass

        input_user_dir = os.path.join(input_directory, user_id)
        for filename in os.listdir(input_user_dir):
            if filename[0] == '.':
                continue
            new_filename = user_id + '_' + file_prefix + '_' + filename
            shutil.copyfile(
                os.path.join(input_user_dir, filename),
                os.path.join(output_user_dir, new_filename)
            )


if __name__ == '__main__':
    input_dirs = sys.argv[1:]

    for input_dir in input_dirs:
        move_user_files_to_combined_directory(input_dir, './user_daten')

    print("done")
