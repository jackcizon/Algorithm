'''page replacement Algorithm
Clock algorithm'''


class ClockAlgorithm:
    def __init__(self, frame_count):
        self.frame_count = frame_count
        self.frames = [None] * frame_count  # Memory frames
        self.ref_bits = [0] * frame_count  # Reference bits
        self.hand = 0  # Clock hand position

    def reference_page(self, page):
        # Check if page is already in memory
        if page in self.frames:
            index = self.frames.index(page)
            self.ref_bits[index] = 1
            return

        # Page fault: page is not in memory
        while True:
            # Search for a page with reference bit 0
            if self.ref_bits[self.hand] == 0:
                # Replace the page
                self.frames[self.hand] = page
                self.ref_bits[self.hand] = 1
                # Move hand to the next frame
                self.hand = (self.hand + 1) % self.frame_count
                return
            else:
                # Clear reference bit and move hand
                self.ref_bits[self.hand] = 0
                self.hand = (self.hand + 1) % self.frame_count

    def print_memory(self):
        print("Memory frames:", self.frames)
        print("Reference bits:", self.ref_bits)


# Example usage:
sequence = [1, 2, 3, 4, 1, 5, 1, 6, 2, 7, 8, 7, 8, 3, 7, 3, 2, 7, 3, 2]
frame_count = 3
clock_algo = ClockAlgorithm(frame_count)

for page in sequence:
    clock_algo.reference_page(page)

clock_algo.print_memory()
