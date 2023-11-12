import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

sns.set()

df = pd.DataFrame(
    [
        {"type": "No Cache", "service": "GitHub Actions", "value": 510},  # minute
        {"type": "With Cache", "service": "GitHub Actions", "value": 442.5},  # minute
        {"type": "No Cache", "service": "ECR", "value": 66},  # GB
        {"type": "With Cache", "service": "ECR", "value": 22},  # GB
        {"type": "No Cache", "service": "ECR Cost", "value": 6.6},  # USD
        {"type": "With Cache", "service": "ECR Cost", "value": 2.2},  # USD
    ]
)

print(df)


fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(15, 5))

sns.barplot(
    data=df[df.service == "GitHub Actions"], x="type", y="value", hue="type", ax=ax[0]
)
ax[0].set_xlabel("")
ax[0].set_ylabel("Duration (Minutes)")
ax[0].set_title("GitHub Actions Runtime")

sns.barplot(data=df[df.service == "ECR"], x="type", y="value", hue="type", ax=ax[1])
ax[1].set_xlabel("")
ax[1].set_ylabel("Size (GB)")
ax[1].set_title("ECR Storage")

sns.barplot(
    data=df[df.service == "ECR Cost"], x="type", y="value", hue="type", ax=ax[2]
)
ax[2].set_xlabel("")
ax[2].set_ylabel("Cost (USD)")
ax[2].set_title("ECR Cost")

fig.suptitle("Cost Breakdown for 150 deployments / month")

fig.savefig("../images/chart.png")
