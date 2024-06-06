class OptionsBatch:

    def __init__(self, corners, climbing, paths, method, steps, time_limit):
        self.cut_corners = corners
        self.allow_climbing = climbing
        self.respect_paths = paths
        self.method = method
        self.placement_steps = steps
        self.time_limit = time_limit