import tweepy

def get_trending_keywords(api, location_woeid=1):
    """
    Get trending keywords from Twitter for a given location (WOEID).
    Default is 1 for Worldwide trends.
    """
    trends_result = api.get_place_trends(id=location_woeid)
    trending_keywords = [trend['name'] for trend in trends_result[0]['trends']]
    return trending_keywords[:5]  # Return top 5 trending keywords
