import csv


def maria_data(order, favorite, maria_dict):
    if not maria_dict:
        favorite = order

    if order in maria_dict:
        maria_dict[order] += 1
    else:
        maria_dict[order] = 1

    if maria_dict[order] > maria_dict[favorite]:
        favorite = order

    return maria_dict, favorite


def extract_data_csv(file):
    orders = set()
    weekdays = set()
    maria_ordered = {}
    maria_favorite = ""
    arnaldo_burguer = 0
    joao_ordered = set()
    days_joao_went = set()
    with open(file, "r") as file:
        for row in csv.DictReader(
            file, fieldnames=["name", "order", "weekday"]
        ):
            orders.add(row["order"])
            weekdays.add(row["weekday"])
            if row["name"] == "maria":
                maria_ordered, maria_favorite = maria_data(
                    row["order"], maria_favorite, maria_ordered
                )
            elif row["name"] == "arnaldo" and row["order"] == "hamburguer":
                arnaldo_burguer += 1
            elif row["name"] == "joao":
                joao_ordered.add(row["order"])
                days_joao_went.add(row["weekday"])
    return (
        orders,
        weekdays,
        maria_ordered,
        maria_favorite,
        arnaldo_burguer,
        joao_ordered,
        days_joao_went,
    )


def analyze_log(path_to_file):
    (
        orders,
        weekdays,
        maria_ordered,
        maria_favorite_order,
        arnaldo_burguer,
        joao_ordered,
        days_joao_went,
    ) = extract_data_csv(path_to_file)
    with open(
        f"{'/'.join(path_to_file.split('/')[:-1])}/mkt_campaign.txt", "w"
    ) as mkt_file:
        print(
            maria_favorite_order,
            arnaldo_burguer,
            orders.difference(joao_ordered),
            weekdays.difference(days_joao_went),
            sep="\n",
            file=mkt_file,
        )
