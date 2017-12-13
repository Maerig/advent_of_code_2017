import re


SCANNER_REGEX = re.compile("(\d+): (\d+)")


class Scanner(object):
    def __init__(self, size):
        self.size = size
        self.loop_size = 2 * (size - 1)

    @staticmethod
    def read_scanners(raw_lines):
        return {
            int(n): Scanner(int(size))
            for n, size in [
                SCANNER_REGEX.match(raw_line).groups()
                for raw_line in raw_lines
            ]
        }

    def get_position(self, t):
        loop_step = t % self.loop_size

        if loop_step < self.loop_size // 2:
            # Ascending
            return loop_step
        # Else descending
        return self.loop_size - t
