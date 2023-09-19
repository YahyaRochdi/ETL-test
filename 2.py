

def extract_rating_data(db_engine):

    query = "SELECT course_id, rating FROM your_table_name"

    # Execute the SQL query and fetch data into a DataFrame
    try:
        # Execute the query and fetch the data into a DataFrame
        rating_data = pd.read_sql_query(query, db_engine)
        return rating_data
    except Exception as e:
        print("An error occurred while extracting rating data:", str(e))
        return None 
def transform_avg_rating(rating_data):
    # Group by course_id and extract average rating per course
    avg_rating = rating_data.groupby('course_id').rating.mean()
    # Return sorted average ratings per course
    sort_rating = avg_rating.sort_values(ascending=False).reset_index()
    return sort_rating

# Extract the rating data into a DataFrame    
rating_data = extract_rating_data(db_engines)

# Use transform_avg_rating on the extracted data and print results
avg_rating_data = transform_avg_rating(rating_data)
print(avg_rating_data) 