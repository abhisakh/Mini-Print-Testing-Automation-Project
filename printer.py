import shutil
import os

def send_print_job(input_file, output_dir="printed_output"):
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, "output.pdf")

    # simulate printing by copying file
    shutil.copy(input_file, output_file)

    return output_file
