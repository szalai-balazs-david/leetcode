import heapq


class Solution:
    # Cheated. Checked solution, then re-implemented
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        upcoming_servers = [] # id
        earlier_servers = list(range(k)) # id
        busy_servers = [] # (finish time, id)
        jobs_done = [0] * k

        for i in range(len(arrival)):
            # Decide default server ID
            server_id = i % k
            if server_id == 0:
                upcoming_servers = earlier_servers
                earlier_servers = []

            # Hande finished jobs
            while len(busy_servers) and busy_servers[0][0] <= arrival[i]:
                id = heapq.heappop(busy_servers)[1]
                if id < server_id:
                    heapq.heappush(earlier_servers, id)
                else:
                    heapq.heappush(upcoming_servers, id)

            # Handle incoming job
            q = upcoming_servers if len(upcoming_servers) > 0 else earlier_servers
            if len(q) == 0:
                continue
            id = heapq.heappop(q)
            heapq.heappush(busy_servers, (arrival[i] + load[i], id))
            jobs_done[id] += 1

        # Evaluate result
        max_job_count = max(jobs_done)
        result = []
        for i in range(len(jobs_done)):
            if jobs_done[i] == max_job_count:
                result.append(i)

        return result
