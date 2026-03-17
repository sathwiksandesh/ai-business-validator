import pandas as pd

def find_competitors():

    data = {
        "Startup":[
            "Uber",
            "Airbnb",
            "DoorDash",
            "Stripe"
        ],
        "Industry":[
            "Transport",
            "Travel",
            "Food Delivery",
            "Payments"
        ]
    }

    df = pd.DataFrame(data)

    return df