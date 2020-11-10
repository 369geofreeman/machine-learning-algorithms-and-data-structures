from sklearn.datasets import fetch_20newsgroups_vectorized
from sklearn.naive_bayes import MultinomialNB


train_data = fetch_20newsgroups_vectorized(subset='train')
test_data = fetch_20newsgroups_vectorized(subset='test')

mnb = MultinomialNB(alpha=0.01)
mnb.fit(train_data['data'], train_data['target'])

score = mnb.score(test_data['data'], test_data['target'])

print('The score for Multinomial Naive Bayes is:', score)





