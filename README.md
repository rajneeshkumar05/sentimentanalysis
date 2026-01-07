## 🧠 How Sentiment is Determined

The sentiment of the input text is predicted using a pre-trained transformer
model. The model does not rely on simple word counting; instead, it analyzes
the contextual meaning of the sentence.

Internally, the model calculates probability scores for each sentiment class
(Positive and Negative). The sentiment label with the highest probability is
selected as the final output.

The confidence score shown in the result represents how confident the model
is about the predicted label.



## 📊 Confidence Score & Threshold Logic

Although 0.50 is commonly used as a reference threshold in binary classification,
this application selects sentiment based on the highest probability score.

Example:
- Positive: 0.78
- Negative: 0.22

In this case, the sentiment is classified as Positive because it has a higher
probability score.

Optionally, custom thresholds can be applied:
- Score ≥ 0.60 → Positive
- Score ≤ 0.40 → Negative
- Score between 0.40 and 0.60 → Neutral (can be extended in future)
