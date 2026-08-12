# Risk matrix
risk_matrix = {
1: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10},
3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15},
4: {1: 4, 2: 8, 3: 12, 4: 16, 5: 20},
5: {1: 5, 2: 10, 3: 15, 4: 20, 5:25}
}


# Welcome message
print("=====================================")
print("        QA DETECTIVE")
print("=====================================")

print("Hello! Let's assess your quality issue.")


# Information gathering
issue = input("\nWhat is your quality issue? ")

print("\nIssue recorded:")
print(issue)

severity = int(input("\nSeverity (1-5): "))
print("Severity recorded:", severity)

likelihood = int(input("\nLikelihood (1-5): "))
print("Likelihood recorded:", likelihood)

repeated_issue = input("\nHas this happened before? (yes/no): ").lower()

number_of_affected_cases = int(input("How many cases are affected?" ))



# Calculate risk
risk_score = risk_matrix[likelihood][severity]



# Decision tree
if risk_score <= 8:
    risk_level = "LOW"
elif risk_score <= 12:
    risk_level = "MEDIUM"
else:
    risk_level = "HIGH"

if repeated_issue == "yes" and risk_score <= 12:
    risk_level = "HIGH"

if number_of_affected_cases >= 100:
    risk_level = "HIGH"
    


# Display result
print("\n====================================")
print("       RISK ASSESSMENT COMPLETE")
print("======================================")

print("Issue:", issue)
print("Likelihood:", likelihood)
print("Severity:", severity)
print("Risk Score:", risk_score)
print("Risk Level:", risk_level)

if risk_level == "HIGH":
    print("\nRecommended action:")
    print("Investigate immediately and place affected products and all products from last good check on hold.")
elif risk_level == "MEDIUM":
    print("\Recommended action:")
    print("Investigate the issue and monitor, raise ncs.")
else:
    print("\nRecommended action:")
    print("Record the issue and monitor for recurrence.")