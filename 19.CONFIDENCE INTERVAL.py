import numpy as np
from scipy.stats import t

# Sample data (replace with your actual data)
drug_group = [2.3, 1.8, 2.5, 2.0, 2.2]  # Replace with actual blood pressure reductions for the drug group
placebo_group = [1.5, 1.0, 1.8, 1.2, 1.6]  # Replace with actual blood pressure reductions for the placebo group

# Calculate sample statistics for each group
mean_drug = np.mean(drug_group)
std_dev_drug = np.std(drug_group, ddof=1)  # Using Bessel's correction for sample standard deviation
n_drug = len(drug_group)

mean_placebo = np.mean(placebo_group)
std_dev_placebo = np.std(placebo_group, ddof=1)
n_placebo = len(placebo_group)

# Degrees of freedom for t-distribution
df_drug = n_drug - 1
df_placebo = n_placebo - 1

# Calculate t-score for a 95% confidence interval
confidence_level = 0.95
t_score = t.ppf((1 + confidence_level) / 2, df_drug)  # Using drug group's degrees of freedom

# Calculate standard errors
std_error_drug = std_dev_drug / np.sqrt(n_drug)
std_error_placebo = std_dev_placebo / np.sqrt(n_placebo)

# Calculate margin of error
margin_of_error_drug = t_score * std_error_drug
margin_of_error_placebo = t_score * std_error_placebo

# Calculate confidence intervals
ci_lower_drug = mean_drug - margin_of_error_drug
ci_upper_drug = mean_drug + margin_of_error_drug

ci_lower_placebo = mean_placebo - margin_of_error_placebo
ci_upper_placebo = mean_placebo + margin_of_error_placebo

# Print the results
print("95% Confidence Interval for Mean Reduction in Blood Pressure (Drug Group):")
print(f"Lower Bound: {ci_lower_drug:.2f}")
print(f"Upper Bound: {ci_upper_drug:.2f}")

print("\n95% Confidence Interval for Mean Reduction in Blood Pressure (Placebo Group):")
print(f"Lower Bound: {ci_lower_placebo:.2f}")
print(f"Upper Bound: {ci_upper_placebo:.2f}")
