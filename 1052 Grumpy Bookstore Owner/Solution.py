class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        satisfied_customers = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfied_customers += customers[i]

        customer = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                customer += customers[i]
        max_extra_customers = customer
        for i in range(minutes, len(customers)):
            customer += grumpy[i] * customers[i]
            customer -= grumpy[i-minutes] * customers[i-minutes]
            max_extra_customers = max(max_extra_customers, customer)

        return satisfied_customers + max_extra_customers
