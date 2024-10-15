def filter_high_ratings(feedback):
    filtered_feedback = {}
    for user_id, details in feedback.items():
        if details['rating'] >= 4:
            filtered_feedback[user_id] = details['rating']
    
    return filtered_feedback

def top_users_by_rating(feedback, top_n=5):
      sorted_feedback = sorted(feedback.items(), key=lambda x: x[1]['rating'], reverse=True)
    return sorted_feedback[:top_n]

def combine_feedback(*feedback_dicts):
    combined_feedback = {}
    
    for feedback in feedback_dicts:
        for user_id, details in feedback.items():
            if user_id in combined_feedback:
                # Update to the highest rating
                combined_feedback[user_id]['rating'] = max(combined_feedback[user_id]['rating'], details['rating'])
                combined_feedback[user_id]['comments'] += f"; {details['comments']}"  # Append comments
            else:
                combined_feedback[user_id] = {
                    'rating': details['rating'],
                    'comments': details['comments']
                }
    
    return combined_feedback

def ratings_above_threshold(feedback, threshold=3):
    return {user_id: details['rating'] for user_id, details in feedback.items() if details['rating'] > threshold}

feedback_data = {
    'user1': {'rating': 4, 'comments': 'Great but well done!'},
    'user4': {'rating': 3, 'comments': 'It was okay.'},
    'user5': {'rating': 4, 'comments': 'Very good!'},
    'user2': {'rating': 2, 'comments': 'Not satisfied.'},
    'user3': {'rating': 5, 'comments': 'Excellent!'},
    'user6': {'rating': 1, 'comments': 'Terrible experience.'},
    'user7': {'rating': 3, 'comments': 'Average.'},
}

filtered_users = filter_high_ratings(feedback_data)
print("Filtered Users (Rating 4 or Higher):", filtered_users)

top_users = top_users_by_rating(feedback_data)
print("Top Users by Rating:", top_users)

feedback_data_2 = {
    'user2': {'rating': 3, 'comments': 'Better than before.'},
    'user5': {'rating': 5, 'comments': 'Absolutely love it!'},
    'user8': {'rating': 4, 'comments': 'Good, but needs improvement.'},
}

combined_feedback = combine_feedback(feedback_data, feedback_data_2)
print("Combined Feedback:", combined_feedback)

ratings_above_3 = ratings_above_threshold(feedback_data)
print("Ratings Above 3:", ratings_above_3)
