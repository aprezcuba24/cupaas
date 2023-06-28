from pathlib import Path
from app.config import INPUT_PIPE, OUTPUT_PIPE


def run_command(command):
    input_fifo_path = Path(INPUT_PIPE)
    input_fifo_path.write_text(command)
    with open(OUTPUT_PIPE) as fifo:
        for line in fifo:
            yield line
