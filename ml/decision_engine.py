def make_decision(machine_id,failure_probability):

    machine_id = "M003"

    maintenance_cost = 12000
    production_loss_if_stopped = 20000
    potential_failure_loss = 80000
    shift_production_cost = 5000

    # Calculate expected failure cost
    expected_failure_cost = (
        failure_probability / 100
    ) * potential_failure_loss

    option1_cost = expected_failure_cost
    option2_cost = maintenance_cost + production_loss_if_stopped
    option3_cost = maintenance_cost + shift_production_cost

    print("\n===== CogniFact AI Decision Engine =====")
    print(f"Machine: {machine_id}")

    print(
        f"\nAI Failure Probability: "
        f"{failure_probability:.2f}%"
    )

    if failure_probability >= 70:
        risk = "HIGH"

    elif failure_probability >= 30:
        risk = "MEDIUM"

    else:
        risk = "LOW"

    print(f"Risk Level: {risk}")

    print("\n===== COST ANALYSIS =====")

    print(
        f"Expected Failure Cost: "
        f"Rs.{expected_failure_cost:,.2f}"
    )

    print("\nOption 1: Continue Operating")

    print(
        f"Expected Impact: "
        f"Rs.{option1_cost:,.2f}"
    )

    print("\nOption 2: Stop + Maintenance")

    print(
        f"Maintenance Cost: "
        f"Rs.{maintenance_cost:,}"
    )

    print(
        f"Production Loss: "
        f"Rs.{production_loss_if_stopped:,}"
    )

    print(
        f"Total Impact: "
        f"Rs.{option2_cost:,}"
    )

    print("\nOption 3: Maintenance + Shift Production")

    print(
        f"Maintenance Cost: "
        f"Rs.{maintenance_cost:,}"
    )

    print(
        f"Shift Production Cost: "
        f"Rs.{shift_production_cost:,}"
    )

    print(
        f"Total Impact: "
        f"Rs.{option3_cost:,}"
    )

    options = {
        "Continue Operating": option1_cost,
        "Stop + Maintenance": option2_cost,
        "Maintenance + Shift Production": option3_cost
    }

    # Choose the lowest-cost option
    recommended_action = min(
        options,
        key=options.get
    )

    recommended_cost = options[recommended_action]

    print("\n===== FINAL RECOMMENDATION =====")

    print(
        f"Action: {recommended_action}"
    )

    print(
        f"Estimated Impact: "
        f"Rs.{recommended_cost:,.2f}"
    )

    print(
        f"Decision based on AI risk "
        f"({failure_probability:.2f}%) + cost analysis"
    )

    return recommended_action

