import json
import os

def load_schemes():
    # Load local JSON file
    with open("data/sample_schemes.json", "r") as file:
        return json.load(file)


def lambda_handler(event, context=None):
    try:
        # If testing locally, event may already be dict
        if isinstance(event, str):
            body = json.loads(event)
        else:
            body = event.get("body", event)

            if isinstance(body, str):
                body = json.loads(body)

        age = int(body.get("age"))
        income = int(body.get("income"))
        category = body.get("category")
        occupation = body.get("occupation")

        schemes = load_schemes()

        eligible_schemes = []

        for scheme in schemes:
            min_age = scheme.get("min_age", 0)
            max_income = scheme.get("max_income", 999999999)
            allowed_category = scheme.get("category", "Any")
            allowed_occupation = scheme.get("occupation", "Any")

            reasons = []

            # Eligibility checks
            if age < min_age:
                continue
            else:
                reasons.append("Age criteria satisfied")

            if income > max_income:
                continue
            else:
                reasons.append("Income criteria satisfied")

            if allowed_category != "Any" and allowed_category != category:
                continue
            else:
                reasons.append("Category criteria satisfied")

            if allowed_occupation != "Any" and allowed_occupation.lower() != occupation.lower():
                continue
            else:
                reasons.append("Occupation criteria satisfied")

            explanation = f"You are eligible for {scheme['name']} because: " + ", ".join(reasons)

            eligible_schemes.append({
                "scheme_name": scheme["name"],
                "reason": explanation
            })

        return {
            "statusCode": 200,
            "body": json.dumps(eligible_schemes, indent=2)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
