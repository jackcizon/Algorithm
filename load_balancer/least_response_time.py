class LeastResponseTimeBalancer:
    def __init__(self, response_times):
        # response_times = {"A":120, "B":30, "C":50}
        self.response_times = response_times

    def next_server(self):
        best_server = None
        best_time = float("inf")

        for server, t in self.response_times.items():
            if t < best_time:
                best_server = server
                best_time = t

        return best_server

    def update_response_time(self, server, new_time):
        self.response_times[server] = new_time


if __name__ == '__main__':
    lrt = LeastResponseTimeBalancer({
        "A": 120,
        "B": 30,
        "C": 50
    })

    for _ in range(3):
        print(lrt.next_server())

    lrt.update_response_time("B", 200)
    print("After update:", lrt.next_server())