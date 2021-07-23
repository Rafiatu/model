import numpy as np
import json

def __process_input(request_data: str) -> np.array:
    parsed_body = np.asarray(json.loads(request_data)["inputs"])
    # assert len(parsed_body) == 1 and len(parsed_body[0] == 13), "'inputs' must be a 1-d array with 13 parameters"
    return parsed_body
