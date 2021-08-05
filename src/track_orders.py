class TrackOrders:
    def __init__(self):
        self.track = {}
        self.days = {}
        self.orders = set()

    def __len__(self):
        return len(self.track)

    def add_new_order(self, costumer, order, day):
        if costumer not in self.track:
            self.track[costumer] = {"orders": {order: 1}, "days": set()}
        if order not in self.track[costumer]["orders"].keys():
            self.track[costumer]["orders"][order] = 1
        else:
            self.track[costumer]["orders"][order] += 1
        if day not in self.days:
            self.days[day] = 1
        else:
            self.days[day] += 1
        self.track[costumer]["days"].add(day)
        self.orders.add(order)

    def get_most_ordered_dish_per_costumer(self, costumer):
        return [
            order
            for order in self.track[costumer]["orders"].keys()
            if self.track[costumer]["orders"][order]
            == max(self.track[costumer]["orders"].values())
        ][0]

    def get_never_ordered_per_costumer(self, costumer):
        return self.orders.difference(self.track[costumer]["orders"].keys())

    def get_days_never_visited_per_costumer(self, costumer):
        return set(self.days.keys()).difference(self.track[costumer]["days"])

    def get_busiest_day(self):
        return [
            day
            for day in self.days.keys()
            if self.days[day] == max(self.days.values())
        ][0]

    def get_least_busy_day(self):
        return [
            day
            for day in self.days.keys()
            if self.days[day] == min(self.days.values())
        ][0]
