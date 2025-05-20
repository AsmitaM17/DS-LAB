# Instagram Reach Analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from pathlib import Path
import os
import chardet
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def load_data(file_path):
    encoding = detect_encoding(file_path)
    try:
        df = pd.read_csv(file_path, encoding=encoding)
        print(f"Data loaded successfully with {encoding} encoding!")
        return df
    except Exception as e:
        print(f"Failed to load file: {e}")
        return None

# Configuration
DATA_PATH = Path("C:/Users/91847/Desktop/python/Instagram_reach analysis/Instagram_data.csv")
OUTPUT_DIR = Path("C:/Users/91847/Desktop/python/Instagram_reach analysis/outputs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_data(file_path):
    """Load and verify dataset"""
    try:
        df = pd.read_csv(file_path)
        print("Data loaded successfully!")
        print("\nFirst 5 rows:")
        print(df.head())
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None

def clean_data(df):
    """Clean and preprocess data"""
    # Drop duplicates
    df = df.drop_duplicates()
    
    # Fill missing values
    df = df.fillna(0)
    
    # Convert hashtags to list
    df['Hashtags'] = df['Hashtags'].apply(
        lambda x: x.split(',') if isinstance(x, str) else []
    )
    
    print("\nData cleaned!")
    return df

def save_plot(fig, filename):
    """Helper to save plots consistently"""
    path = OUTPUT_DIR / filename
    fig.savefig(path, bbox_inches='tight')
    print(f"Saved plot to {path}")

def analyze_reach_sources(df):
    """Analyze traffic sources"""
    reach_sources = df[['From Home', 'From Hashtags', 'From Explore', 'From Other']].sum()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    reach_sources.plot(kind='bar', color=['#FF9AA2', '#FFB7B2', '#FFDAC1', '#E2F0CB'], ax=ax)
    ax.set_title("Reach from Different Sources")
    ax.set_ylabel("Total Reach")
    save_plot(fig, 'reach_sources.png')
    plt.close()
    
    return reach_sources

def analyze_engagement(df):
    """Analyze engagement metrics"""
    engagement = df[['Likes', 'Comments', 'Shares', 'Saves']].sum()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    engagement.plot(kind='bar', color=['#FF9AA2', '#FFB7B2', '#FFDAC1', '#E2F0CB'], ax=ax)
    ax.set_title("Engagement Metrics")
    ax.set_ylabel("Total Count")
    save_plot(fig, 'engagement.png')
    plt.close()
    
    return engagement

def analyze_hashtags(df):
    """Generate hashtag word cloud"""
    all_hashtags = ' '.join([tag for sublist in df['Hashtags'] for tag in sublist])
    
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_hashtags)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title("Most Used Hashtags")
    save_plot(fig, 'hashtags_wordcloud.png')
    plt.close()

def analyze_correlation(df):
    """Analyze metric correlations"""
    corr_matrix = df[['Impressions', 'Likes', 'Comments', 'Shares', 'Saves', 'Profile Visits', 'Follows']].corr()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
    ax.set_title("Correlation Matrix")
    save_plot(fig, 'correlation_matrix.png')
    plt.close()
    
    return corr_matrix

def main():
    # Load and verify data
    df = load_data(DATA_PATH)
    if df is None:
        return
    
    # Clean data
    df = clean_data(df)
    
    # Run analyses
    print("\nReach Sources Analysis:")
    reach_sources = analyze_reach_sources(df)
    print(reach_sources)
    
    print("\nEngagement Analysis:")
    engagement = analyze_engagement(df)
    print(engagement)
    
    print("\nHashtag Analysis:")
    analyze_hashtags(df)
    
    print("\nCorrelation Analysis:")
    corr_matrix = analyze_correlation(df)
    print(corr_matrix)

if __name__ == "__main__":
    main() 