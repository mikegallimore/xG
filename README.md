# xG

### Requirements
At minimum, a vanilla installation of Python3. If Python isn't on your machine, the simplest remedy is to install the Anaconda Distribution or, alternatively, its less-cumbersome version (Miniconda). 

Refer to <code>environment.yml</code> for the specific version of each module listed below:
<ul>
  <li>numpy</li>  
  <li>pandas</li>
  <li>pickle</li>
  <li>scikit-learn</li>
</ul>

### Data Prep
All of the shot data <a href="http://moneypuck.com/data.htm">originates from MoneyPuck</a> in the form of distinct season files, each of which received an initial treatment in Excel.

These separate files were then bound, or aggregated into one of two files that are cleaned further via <code>prep_data.py</code>:
<ul>
<li><a href="https://drive.google.com/file/d/1p1IiUqVlKlmszVOWvlHiOUYf1X3ooIks/view?usp=sharing">training_set.csv</a> (20072008, 20082009, 20092010, 20102011, 20112012, 20132014, 20142015, 20152016, 20162017)</li>
<li><a href="https://drive.google.com/file/d/1JWUNobDbNl3Lc-M6KMRjIAakINqzObh_/view?usp=sharing">testing_set.csv</a> (20172018, 20182019</li>
</ul>

### Model Training
<a href="https://drive.google.com/open?id=1rAEsvR4efPrDjyqWFCL8i1OciWfXxKs7">shots_train.csv</a> includes 64,276 goals among 987,926 unblocked regular season and playoffs shots.

Running the following scripts will train a specific type of model:
<ul>
  <li><code>xG_model_logistic-regression_train.py</code></li>
  <li><code>xG_model_gradient-boosting_train.py</code></li>
</ul>

### Model Testing
<a href="https://drive.google.com/open?id=1C5l53rmSugEvGRdRH0cKAyBzSOHlAaeE">shots_test.csv</a> includes 15,952 goals among 237,320 unblocked regular season and playoffs shots.

Running the following scripts will test a specific type of already-trained model:
<ul>
  <li><code>xG_model_logistic-regression_test.py</code></li>
  <li><code>xG_model_gradient-boosting_test.py</code></li>
</ul>
