from cycle_detector import detect_cycles
from velocity_detector import detect_velocity_fraud


def calculate_risk():

    risk_scores = {}

    # Detect cycle fraud
    cycles = detect_cycles()

    for path in cycles:

        for node in path.nodes:

            account = node["id"]

            if account not in risk_scores:
                risk_scores[account] = 0

            risk_scores[account] += 50


    # Detect velocity fraud
    velocity_accounts = detect_velocity_fraud()

    for acc in velocity_accounts:

        account = acc["account"]

        if account not in risk_scores:
            risk_scores[account] = 0

        risk_scores[account] += 25


    return risk_scores


if __name__ == "__main__":

    scores = calculate_risk()

    print("Risk Scores")

    for account, score in scores.items():

        if score > 70:
            print(account, "HIGH RISK", score)
        else:
            print(account, "MEDIUM RISK", score)