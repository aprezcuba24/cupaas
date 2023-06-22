while true; do eval "$(cat localmachine/input_pipe)" &> localmachine/output.txt; done

To start the project
uvicorn manager:app --reload  --host="0.0.0.0" --port=5000