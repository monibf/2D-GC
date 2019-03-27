
import numpy as np

class Chromatogram:
    
    def __init__(self, grid):
        self._grid = grid
        # todo: store offset etc. Maybe even store grid as 1-dimensional data
    
    def as_grid(self):
        # returns a 2-dimensional numpy grid of the data (so we don't have to expose the internal representation)
        return self._grid
    
    @classmethod
    def from_file(cls, filename):
        data = []
        with open(filename) as sourcefile:
            for line in sourcefile:
                row = [float(val.strip()) for val in line.split(",") if val.strip()]
                data.append(row)
        arr = np.array(data, dtype=np.float64)
        return cls(arr.transpose())
