import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


# Plot a histogram of avg user rating
def success_hist(df,metric):
    plt.figure(figsize=(7,4))
    sns.histplot(df[metric], bins=30)
    plt.title(f"Distribution of {metric.replace('_',' ').title()}")
    plt.xlabel(metric)
    plt.ylabel('Count')
    plt.show()
    
    
# Scatter plot comparing user ratings vs critic ratings
def rating_scatter(df, critic, user):
    plt.figure(figsize=(7,4))
    sns.scatterplot(x= critic, y=user,data =df)
    plt.title("User vs Critic Ratings")
    plt.xlabel("Critic Rating")
    plt.ylabel("User Rating")
    plt.show()
        
        
# Correlation heatmap for numerical features
def correlation(matrix):
    plt.figure(figsize=(12, 8))
    sns.heatmap(matrix, annot=True, fmt=".2f", cmap='coolwarm', center=0, linewidths=0.5)
    plt.title("Correlation Heatmap of Numeric Features")
    plt.show()
    
    
# Bar plot of game releases per year (data must already be grouped)
def rel_time():
    plt.title("Number of Games Released per Year")
    plt.xlabel("Number of Games")
    plt.ylabel("Release Year")
    plt.show()
 
 
# Line plot of average user rating by release year   
def metric_year(avg, metric):
    plt.figure(figsize = (12,10))
    sns.lineplot(x= "release_year", y= metric, data = avg, marker = 'o')
    plt.title(f"Average {metric.replace('_',' ').title()} by Release Year")
    plt.ylabel("Average Rating")
    plt.grid(True)
    plt.show()
    
    
# Line plot of average metric by release month
def metric_month(avg, metric):
    plt.figure(figsize = (8,4))
    sns.lineplot(x= "release_month", y =metric, data = avg, marker ='o')
    plt.title(f"Average {metric.replace('_',' ').title()} by Release Month")
    plt.ylabel("Average Rating")
    plt.grid(True)
    plt.show()
    
    
# Bar plot showing how many games fall into each genre count
def count_genre(df):
    counts = df['genre_count'].value_counts()
    counts.plot(kind = 'bar')
    plt.title("Distribution of Genre Count per Game")
    plt.xlabel("Number of Genres")
    plt.ylabel("Game Count")
    plt.show()
    
    
# Boxplot comparing metric (e.g. rating) across genre counts  
def compare_genre(df, metric):
    plt.figure(figsize = (14,24))
    sns.boxplot(x ='genre_count', y=metric, data=df)
    plt.title(f"{metric.replace('_',' ').title()} vs Genre Count")
    plt.show()
    

# Barplot showing average ratings per genre (top 10 only)
def avg_ratings_genre(df,genres, metric):
    # Combine genre dummy vars with target metric
    joined = pd.concat([genres, df[metric]], axis =1)
    melt = pd.melt(joined, id_vars = metric,var_name = 'genre', value_name= 'is_genre')
    melt = melt[melt['is_genre'] == 1]
    
    # Count games per genre
    genre_counts = melt['genre'].value_counts()
    valid_genres = genre_counts[genre_counts > 100].index
    melt = melt[melt['genre'].isin(valid_genres)]
    
    
    # Group by genre to compute averages
    grouped = melt.groupby('genre')[metric].mean().reset_index()
    top_10 = grouped.sort_values('avg_user_rating', ascending  = False).head(10)
    
    # Plot
    plt.figure(figsize = (6, 6))
    sns.barplot(data = top_10, x = 'genre', y='avg_user_rating')
    plt.title("Average User Ratings per Genre (Top 10)")
    plt.ylabel("Average User Ratings")
    plt.ylim(3,3.8)
    plt.xlabel("Genre")
    plt.xticks(rotation=45)
    plt.show()
    
    
# Boxplot comparing metric by platform type 
def compare_platforms(df, metric):
    df = df[df['platform_type'].isin(['multi_platform', 'pc_only'])]
    plt.figure(figsize= (6,6))
    sns.boxplot(x='platform_type', y=metric, data=df)
    plt.title(f"{metric.replace('_',' ').title()} by Platform Type")
    plt.ylabel(metric)
    plt.xlabel("Platform Type")
    plt.show()
    

# Lineplot showing how average rating varies by number of platforms a game was released on
def compare_platform_store_count(df):
    plt.figure(figsize= (6,4))
    sns.lineplot(x='platform_count', y='avg_user_rating', data=df,errorbar = None )
    sns.lineplot(x='store_count', y='avg_user_rating', data =df, errorbar= None)
    plt.legend(['Platform Count', 'Store Count'])
    plt.title(f"Average User Ratings by Platform Count")
    plt.xlabel("Platform Count")
    plt.ylabel("Average User Rating")
    plt.show()
        
        
# Histogram showing how many stores games are available on
def store_dist(stores):
    sns.histplot(stores, kde=False)
    plt.title("Distribution of Store Count")
    plt.xlabel("Store Count")
    plt.ylabel("Number of Games")
    plt.show()
    
    
# Countplot showing how many games fall into each ESRB rating category
def mature_count(df):
    df = df[df['esrb_rating']!= 'Rating Pending']
    plt.figure(figsize=(8, 4))
    sns.countplot(data=df, x='esrb_rating', order=df['esrb_rating'].value_counts().index)
    plt.title("Distribution of ESRB Ratings")
    plt.xlabel("ESRB Rating")
    plt.ylabel("Number of Games")
    plt.xticks(rotation=30)
    plt.show()
    print(df['esrb_rating'].value_counts())
    
    
# Boxplot comparing rating or metric by ESRB rating category
def mature_comp(df,metric):
    df = df[df['esrb_rating']!= 'Rating Pending']
    plt.figure(figsize= (8,5))
    sns.boxplot(x='esrb_rating', y=metric, data=df)
    plt.title(f"{metric.replace('_',' ').title()} by ESRB Rating")
    plt.ylabel(metric)
    plt.xlabel("ESRB Rating ")
    plt.show()
    
    
# Histograms for multiple engagement features
def engage_dist(df, features):
    plt.figure(figsize=(16, 4))
    for i, feat in enumerate(features):
        plt.subplot(1, len(features), i + 1)
        sns.histplot(data=df, x=feat, bins=40)
        plt.title(f"Distribution of {feat.replace('_', ' ').title()}")
    plt.tight_layout()  
    plt.show()
    
    
# Scatterplots comparing engagement features with avg user rating
def engage_plot(df, features, metric):
    plt.figure(figsize=(16, 8))
    for i, feat in enumerate(features):
        plt.subplot(1, len(features), i + 1)
        sns.scatterplot(x=feat, y=metric, data=df)
        plt.title(f"{feat.replace('_',' ').title()} vs {metric.replace('_',' ').title()}")
        plt.xscale("log")
        plt.xlabel(feat)
        plt.ylabel(metric)
    plt.tight_layout()
    plt.show()
    
    
# Histogram showing how much users and critics disagree in ratings
def gap_distr(gap):
    plt.figure(figsize=(8,4))
    sns.histplot(gap, bins=30)
    plt.title("Distribution of Rating Gap (User - Critic)")
    plt.xlabel("Rating Gap")
    plt.show()
    

# Barplot showing user ratings over time, grouped by platform type
def platform_year(df):
    plt.figure(figsize=(14, 12))
    sns.barplot(data=df, x='release_year', y='avg_user_rating', hue='platform_type', errorbar = None)
    plt.xticks(rotation=45)
    plt.title("Average User Rating Over Time by Platform Type")
    plt.ylabel("Avg User Rating")
    plt.xlabel("Release Year")
    plt.legend(title="Platform Type")
    plt.show()
    