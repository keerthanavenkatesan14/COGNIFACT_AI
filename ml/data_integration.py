import pandas as pd
machine_data = pd.read_csv("data/cognifact_machine_dataset.csv")
maintenance_data = pd.read_csv("data/maintenance_data.csv")
production_data = pd.read_csv("data/production_data.csv")
inventory_data = pd.read_csv("data/inventory_data.csv")
orders_data = pd.read_csv("data/orders_data.csv")
factory_data = machine_data.merge(
    maintenance_data,
    on="Machine_ID",
    how="left"
)
factory_data = factory_data.merge(
    production_data,
    on="Machine_ID",
    how="left"
)

print("\nCogniFact Data Integration")

print("\nIntegrated Machine Data:")
print(factory_data.head())

print("\nTotal Machines:", len(factory_data))

print("\nAvailable Inventory:")
print(inventory_data)

print("\nProduction Orders:")
print(orders_data)

print("\n")