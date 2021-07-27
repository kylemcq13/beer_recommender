# beer_recommender

Check out the app here --> https://beer-recommender-km.herokuapp.com

## Problem Statement: 
Recommend wonderful beers for a beer geek like myself. The recommender should take in a beer the user
likes and return some logical recommendations.

Three recommenders were built - a content recommender, a collaborative filter, and a hybrid of the two.

## Data Description: 
Data was obtained from Beer Advocate's beer review site. Reviewers can rate beers numerically based on 
look, smell, taste, and feel. They also leave A LOT of text reviews which have significant value.

### Scoring:
Each beer category (look, smell, taste, and feel) is rated 1-5, 1 being the worst, 5 being the best. 

### Beer Text Reviews:
Reviewers can also leave free text reviews for a beer. See below an example:

"Poured a bit lively and had to wait for it to settle very nice lacing. Slightly hazy golden straw. Floral 
notes maybe a hint of citrus. Quite smooth on the palate a touch bitter and definitely a pungent finish as 
advertised. Somewhat of a dry finish and something about the lingering taste is off. The mouth coating is 
a touch creamy."

## Content Recommender:
The beer recommender was built using a content recommender system, which looks for similarities in text in
the free text reviews. 

-Pictured Below-
If you entered Founders Brewing Company's Breakfast Stout as a beer you like, these are the beers that would
be recommended to you.

![Content Recommender Output](https://github.com/kylemcq13/beer_recommender/blob/master/images/content_rec_output.PNG "Content Recommender Example Output")

## Collaborative Filtering:
Using the surprise library, fit and tuned the data with the SVD algorithm. 

![Collaborative Filter Metrics](https://github.com/kylemcq13/beer_recommender/blob/master/images/collab_filter_metrics.PNG "Collaborative Filter Metrics")

## Hybrid Model:
This model is a content/collaborative filter hybrid. Using the highest scoring SVD model and the content 
recommender, recommendations are generated at the user level and overall score (out of 5) is predicted for 
each recommended beer. 

-Pictured Below-
If you were user 4608 and entered Cigar City's Jai Alai IPA, the below are the recommendations you would 
receive.

![hybrid reco output](https://github.com/kylemcq13/beer_recommender/blob/master/images/hybrid_rec_output.PNG "Hybrid Recommender Example Output")




