# Complete the connection URI
import pandas as pd
import sqlalchemy

connection_uri = "postgresql://repl:password@localhost:5432/datacamp_application" 
db_engine = sqlalchemy.create_engine(connection_uri)

def print_user_comparison(user1, user2, user3):
    
    
    # Convert the movie IDs from each user to sets for easy comparison
    user1_movies = set(user1['movie_id'])
    user2_movies = set(user2['movie_id'])
    user3_movies = set(user3['movie_id'])

    # Find the overlapping movie IDs for each pair of users
    user1_user2_overlap = user1_movies.intersection(user2_movies)
    user1_user3_overlap = user1_movies.intersection(user3_movies)
    user2_user3_overlap = user2_movies.intersection(user3_movies)

    # Print the overlapping movie IDs for each pair of users
    print("User 1 and User 2 overlap:", user1_user2_overlap)
    print("User 1 and User 3 overlap:", user1_user3_overlap)
    print("User 2 and User 3 overlap:", user2_user3_overlap)


# Get user with id 4387
user1 = pd.read_sql("SELECT * FROM rating where user_id =4387", db_engine)

# Get user with id 18163
user2 = pd.read_sql("SELECT * FROM rating where user_id =18163", db_engine)
# Get user with id 8770
user3 = pd.read_sql("SELECT * FROM rating where user_id =8770", db_engine)

# Use the helper function to compare the 3 users
print_user_comparison(user1,user2, user3)