class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        def get_max_profit(start: int, end: int) -> (int, int, int):
            buy_index = start
            best_buy = prices[buy_index]
            buys = [best_buy]
            buy_indexes = [buy_index]
            for i in range(start + 1, end+1):
                if prices[i] < best_buy:
                    buy_index = i
                    best_buy = prices[buy_index]
                buys.append(best_buy)
                buy_indexes.append(buy_index)

            sell_index = end
            best_sell = prices[sell_index]
            sells = [best_sell]
            sell_indexes = [sell_index]
            for i in range(end - 1, start - 1, -1):
                if prices[i] >= best_sell:
                    sell_index = i
                    best_sell = prices[sell_index]
                sells.append(best_sell)
                sell_indexes.append(sell_index)
            sells.reverse()
            sell_indexes.reverse()

            best_deal = 0
            deal_index = -1
            for i in range(len(buys)):
                if sells[i] - buys[i] > best_deal:
                    deal_index = i
                    best_deal = sells[i] - buys[i]
            return best_deal, buy_indexes[deal_index], sell_indexes[deal_index]

        length = len(prices)
        #Deal with limited elements
        match length:
            case 1:
                return 0
            case 2:
                return max(0, prices[1]-prices[0])
            case 3:
                return get_max_profit(0, 2)[0]
            case 4:
                if prices[1] > prices[2]:
                    return get_max_profit(0,1)[0] + get_max_profit(2,3)[0]
                else:
                    return get_max_profit(0,3)[0]

        #More than 4 elements in the list
        best_single_deal = get_max_profit(0, length-1)
        max_profit = best_single_deal[0]

        # Continuous price drop
        if max_profit == 0:
            return 0

        divide = max(1, best_single_deal[1] - 1)
        max_sell_value = max(prices)
        while divide < length - 2:
            first_deal = get_max_profit(0,divide)
            second_deal = get_max_profit(divide+1, length-1)
            max_profit = max(max_profit, first_deal[0] + second_deal[0])
            divide = max(divide + 1, second_deal[1]-1)

            # If second deal does not produce profit, not need to move the goalpost further
            if second_deal[0] == 0:
                break
            # If first deal ends with the max sell price, there's no need to move the goalpost further
            # Need to check if first deal actually produces profit. If not, the end time is invalid
            if max_sell_value == prices[first_deal[2]] and first_deal[0] != 0:
                break
            if first_deal[2] + 1 == second_deal[1] and first_deal[0] != 0 and second_deal[0] != 0:
                off_deal = get_max_profit(second_deal[1], second_deal[2] - 1)
                divide = off_deal[2]

        return max_profit
