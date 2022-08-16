class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        class thingy:
            def __init__(self, start: int, end: list[int], profit: list[int]):
                self.start = start
                self.end = end
                self.profit = profit

        def get_options() -> list[thingy]:
            options = []
            for i in range(len(prices) - 1):
                if prices[i] == prices[i+1]:
                    continue
                current = thingy(i, [], [])
                for j in range(i + 1, len(prices)):
                    for k in range(len(current.end)):
                        if prices[j] > prices[current.end[k]]:
                            if current.end[k] == j-1:
                                current.end[k] = j
                                current.profit[k] = prices[j] - prices[current.start]
                            else:
                                current.end.append(j)
                                current.profit.append(prices[j] - prices[i])

                    if len(current.end) == 0:
                        if prices[i] < prices[j]:
                            current.end.append(j)
                            current.profit.append(prices[j] - prices[i])
                    else:
                        if prices[i] + current.profit[-1] < prices[j]:
                            current.end.append(j)
                            current.profit.append(prices[j] - prices[i])
                if len(current.end) > 0:
                    options.append(current)
            return options

        def filter_options(options: list[thingy]):
            for i in range(len(options) - 1, 0, -1):
                if options[i].start == options[i-1].start + 1 and options[i].profit[-1] < options[i-1].profit[-1]:
                    options.remove(options[i])
            #Remove same end & earlier start & lower profit
            for i in range(len(options) - 1):
                for ii in range(len(options[i].end) - 1, -1, -1):
                    for j in range(i + 1, len(options)):
                        done = False
                        for jj in range(len(options[j].end)):
                            start_is_earlier = options[i].start < options[j].start
                            end_is_same = options[i].end[ii] == options[j].end[jj]
                            profit_is_less = options[i].profit[ii] <= options[j].profit[jj]
                            if start_is_earlier and end_is_same and profit_is_less:
                                del options[i].end[ii]
                                del options[i].profit[ii]
                                done = True
                                break
                        if done:
                            break
            #remove options with no element
            for i in range(len(options) - 1, -1, -1):
                if len(options[i].profit) == 0:
                    del options[i]

        def calculate_profit(options: list[thingy]) -> int:
            max_profit = 0
            for i in range(len(options) - 1):
                for ii in range(len(options[i].profit)):
                    first_profit = options[i].profit[ii]
                    for j in range(i + 1, len(options)):
                        if options[j].start <= options[i].end[ii]:
                            max_profit = max(max_profit, first_profit)
                        else:
                            profit = first_profit + options[j].profit[-1]
                            max_profit = max(max_profit, profit)
            return max_profit

        options = get_options()
        filter_options(options)
        if len(options) == 0:
            return 0
        if len(options) == 1:
            return options[0].profit[-1]
        return calculate_profit(options)
