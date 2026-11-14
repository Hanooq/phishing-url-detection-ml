# Phishing Website and URL Detection Using Machine Learning

## Project overview
A small educational binary-classification project. It demonstrates how a machine-learning model can learn from URL-related features and classify an example as **potentially phishing** or **likely legitimate**.

## Important data limitation
The included `simulated_phishing_url_dataset.csv` is generated programmatically for demonstration. It does **not** contain verified real URLs or labels, and the reported test metrics only describe performance on this simulated dataset. They must not be presented as real-world phishing-detection accuracy. Do not use this prototype to decide whether a real website is safe.

## Files
- `simulated_phishing_url_dataset.csv` — 1,200 simulated rows.
- `train_model.py` — trains and evaluates a Random Forest classifier; saves `phishing_url_model.joblib`.
- `predict_example.py` — runs one example prediction after training.
- `Phishing_URL_Detection_Internship_Report.docx` — concise project report.
- `Phishing_URL_Detection_Internship_Presentation.pptx` — short presentation.
- `Phishing_URL_Detection.ipynb` — notebook version of the workflow.
- `Phishing_URL_Detection_EXECUTED.ipynb` — executed notebook with saved cell outputs for review.

## Run locally
1. Install Python 3.10 or later.
2. Open a terminal in this folder.
3. Install packages: `pip install -r requirements.txt`
4. Train and evaluate: `python train_model.py`
5. Run the example: `python predict_example.py`

## Run in Google Colab
Upload the CSV and notebook to Colab, then run the notebook cells from top to bottom. Alternatively upload the ZIP, extract it in Colab, and run `train_model.py`.

## Features used
- URL length
- Number of dots
- Number of hyphens
- Presence of `@`
- Whether an IP address is used as the host
- HTTPS indicator
- Number of digits
- Count of suspicious words (simulated feature)
- URL-shortener indicator

These are simplified demonstration features, not a complete inspection of a website.

## Model
Random Forest Classifier. Data is split into training and testing subsets using a fixed random seed and stratification. The evaluation includes accuracy, precision, recall, F1-score and a confusion matrix.

## Limitations and future work
Use a properly sourced, current, labelled public dataset; extract features from actual URLs; avoid data leakage; test on a time-separated dataset; tune thresholds; and assess false negatives. The model does not visit websites, inspect page content, verify certificates, or guarantee safety.
