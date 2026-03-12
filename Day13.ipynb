In AI/ML QA, my job is to verify how good or bad the model predictions are.

Example:
If a model predicts Spam vs Not Spam, you must measure:

Correct predictions

Wrong predictions

How confident the model is

1️⃣ Confusion Matrix

A Confusion Matrix shows the prediction results in a table.

\begin{bmatrix}TP & FP \ FN & TN\end{bmatrix}

Meaning:

Term	Meaning
TP	True Positive (Correct Positive)
TN	True Negative
FP	False Positive
FN	False Negative

Example (Spam detector)

Actual	Predicted	Result
Spam	Spam	TP
Spam	Not Spam	FN
Not Spam	Spam	FP
Not Spam	Not Spam	TN

ML QA engineers analyze these errors.

2️⃣ ROC Curve & AUC

ROC shows model performance across thresholds.

AUC = \int_{0}^{1} TPR(FPR), d(FPR)

idea:

AUC Score	Model Quality
0.5	Random
0.7–0.8	Good
0.8–0.9	Very good
0.9+	Excellent

QA Engineers check if AUC drops after updates.



Example code:

from sklearn.metrics import confusion_matrix, roc_auc_score
import numpy as np

y_true = [0,1,1,0,1]
y_pred = [0,1,0,0,1]

cm = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:\n", cm)

auc = roc_auc_score(y_true, y_pred)
print("AUC Score:", auc)


CI/CD Basics for ML QA

Now I learn automation used in real companies.

CI/CD = Continuous Integration / Continuous Deployment

Meaning:

Every time code is pushed to GitHub, tests run automatically.

Popular CI/CD tools:

GitHub Actions

Jenkins

GitLab CI

We will use GitHub Actions

Create Workflow

Create file:

.github/workflows/test.yml

Example:

name: ML Tests

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.10

      - name: Install dependencies
        run: pip install pytest scikit-learn

      - name: Run tests
        run: pytest

Now when I push code → tests run automatically.
