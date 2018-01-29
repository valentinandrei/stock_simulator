import random as rng
import math

# Global parameters to modify the average "personality" of brokers

n_min_start_cash = 10000
n_max_start_cash = 10000000
n_min_logins_per_day = 1
n_max_logins_per_day = 48
f_pc_avg_drop_sell = 5
f_pc_avg_growth_short_sell = 10
f_pc_avg_buy_margin = 0.1
f_pc_avg_sell_margin = 0.05
f_pc_avg_prob_cash_out = 1
f_pc_avg_prob_cash_in = 1
n_avg_window_study = 90


class Broker:

    # The identifier of the broker
    n_id = 0

    # Cash balance in the account
    n_cash = 100000

    # Share balance in the account
    n_shares = 0

    # Account value
    n_value = 0

    # Number of daily logins
    n_logins_per_day = 1

    # Last value of the stock, known to the broker
    f_last_known_value = 0

    # Drop percent to trigger selling of stock
    f_pc_drop_sell = f_pc_avg_drop_sell

    # Growth percent to trigger short selling of stock
    f_pc_growth_short_sell = f_pc_avg_growth_short_sell

    # Bid percentage
    f_pc_buy_margin = f_pc_avg_buy_margin

    # Ask percentage
    f_pc_sell_margin = f_pc_avg_sell_margin

    # Probability of a full cash out without analyzing stock price
    f_pc_prob_cash_out = f_pc_avg_prob_cash_out

    # Probability of a share acquisition with the full account amount
    f_pc_prob_cash_in = f_pc_avg_prob_cash_in

    # Number of days analyzed in order to make a decision
    n_days_to_analyze = n_avg_window_study

    # Constructor
    def __init__(self, broker_id, start_price):
        self.n_id = broker_id
        self.n_cash = rng.randint(n_min_start_cash, n_max_start_cash)
        self.n_value = self.n_cash
        self.n_logins_per_day = rng.randint(n_min_logins_per_day, n_max_logins_per_day)
        self.f_last_known_value = start_price

    # Returns the maximum amount to spend on shares; If negative, that number of shares are sold
    def get_decision(self, share_price):

        # Check if random cash out
        if self.n_shares > 0:
            f_sell = rng.randint(1, 1e+5) / 1e+5
            if f_sell < f_pc_avg_prob_cash_out:
                return -1 * self.n_shares

        # Check if random cash in
        if self.n_cash > share_price:
            f_buy = rng.randint(1, 1e+5) / 1e+5
            if f_buy < f_pc_avg_prob_cash_in:
                return math.floor(self.n_cash / share_price) * (1 + self.f_pc_buy_margin)

        return 0

    # Posts a transaction and converts cash to shares and vice-versa
    def post_transaction(self, num_shares, share_price):
        self.n_shares += num_shares
        self.n_cash -= (num_shares * share_price)

    # Updates the account value based on share price
    def update_value(self, share_price):
        self.n_value = self.n_shares * share_price

    # Prints the records of the broker
    def print_details(self):
        print("ID = %d, Shares = %d, Cash = %d, Value = %d" % (self.n_id, self.n_shares, self.n_cash, self.n_value))


b = Broker(1, 10)
b.print_details()
