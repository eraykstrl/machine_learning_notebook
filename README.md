## Data Source & Acknowledgements

The datasets used in this project are the **[Job Salary Prediction Dataset](https://www.kaggle.com/datasets/nalisha/job-salary-prediction-dataset)** provided by **Aleesha Nadeem (Nalisha)** on Kaggle, and the classic **[Iris Dataset](https://archive.ics.uci.edu/ml/datasets/iris)**.

I would like to thank the dataset creator for making this comprehensive data publicly available for machine learning and analytical purposes.

## What is Feature Engineering

Feature engineering is a technique that improves the feature set and interpretability of data. By means of feature engineering, algorithms can process data more effectively. It includes different techniques such as feature transformation, scaling, extraction, and selection.

## Feature Transformation

Categorical encoding techniques transform qualitative features into numerical representations suitable for machine learning models.
Label Encoding converts categories into arbitrary integers, which is simple but may introduce unintended mathematical relationships in distance-based models. Ordinal Encoding resolves this by preserving the hierarchical order of ordinal data. For nominal data without inherent ranking, One-Hot Encoding is preferred, as it maps categories to orthogonal binary vectors; however, it risks introducing the curse of dimensionality and high sparsity if the feature cardinality is high. In such complex scenarios, advanced techniques like Target Encoding are often integrated into the pipeline.


## Feature Scaling

It brings data into same scale. By means of scaling the datas can be limit in some scale. If the type of feature is in different scale it can bring data into same 
scale and can increase interpretiblity of datas.
