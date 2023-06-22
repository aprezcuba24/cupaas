from pathlib import Path
from app.config import INPUT_PIPE, OUTPUT_PIPE


def run_command(command):
    input_fifo_path = Path(INPUT_PIPE)
    assert input_fifo_path.is_fifo()
    input_fifo_path.write_text(command)
    output_fifo_path = Path(OUTPUT_PIPE)
    assert output_fifo_path.is_fifo()
    print("===>", output_fifo_path.read_text())
