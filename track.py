import numpy as np
import pandas as pd

class Track:
    def __init__(self, segments_data):
        """
        Initialize track from segment data
        segments_data: list of (distance, curvature) tuples or DataFrame
        """
        if isinstance(segments_data, pd.DataFrame):
            self.distances = segments_data['s'].values
            self.curvatures = segments_data['curvature'].values
        else:
            self.distances = np.array([s[0] for s in segments_data])
            self.curvatures = np.array([s[1] for s in segments_data])
        
        self.segment_lengths = np.diff(np.append(self.distances, self.distances[0]))
        self.total_length = self.distances[-1]
    
    @classmethod
    def from_csv(cls, filename):
        """Load track from CSV file"""
        data = pd.read_csv(filename)
        return cls(data)
    
    def get_radius(self, segment_idx):
        """Get radius of curvature for segment (handles zero curvature)"""
        curvature = self.curvatures[segment_idx]
        return float('inf') if curvature == 0 else 1.0 / abs(curvature)
    
    def get_segment_length(self, segment_idx):
        """Get length of segment"""
        return self.segment_lengths[segment_idx]