import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
import string

# Download required NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

class TEDxDataProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
    
    def clean_transcript(self, text):
        """Clean and preprocess transcript text"""
        if pd.isna(text):
            return ""
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove timestamps and metadata
        text = re.sub(r'\d{1,2}:\d{2}', '', text)
        text = re.sub(r'\[.*?\]', '', text)
        text = re.sub(r'\(.*?\)', '', text)
        
        # Remove URLs
        text = re.sub(r'http\S+|www.\S+', '', text)
        
        # Fix common transcription errors
        text = text.replace(' um ', ' ')
        text = text.replace(' uh ', ' ')
        text = text.replace('...', '.')
        
        return text.strip()
    
    def extract_key_topics(self, text, top_n=10):
        """Extract key topics using simple frequency analysis"""
        # Tokenize and clean
        words = word_tokenize(text.lower())
        words = [word for word in words if word not in self.stop_words 
                and word not in string.punctuation and len(word) > 3]
        
        # Count frequency
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        # Return top words
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return [word for word, freq in sorted_words[:top_n]]
    
    def chunk_text(self, text, chunk_size=500, overlap=50):
        """Split text into overlapping chunks"""
        sentences = sent_tokenize(text)
        chunks = []
        current_chunk = ""
        
        for sentence in sentences:
            if len(current_chunk) + len(sentence) < chunk_size:
                current_chunk += " " + sentence
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = sentence
        
        if current_chunk:
            chunks.append(current_chunk.strip())
        
        return chunks
    
    def process_dataset(self, input_file, output_file):
        """Process entire dataset"""
        print("🔄 Processing TEDx dataset...")
        
        # Load raw data
        df = pd.read_csv(input_file)
        
        # Clean transcripts
        df['cleaned_transcript'] = df['transcript'].apply(self.clean_transcript)
        
        # Extract topics
        df['key_topics'] = df['cleaned_transcript'].apply(self.extract_key_topics)
        
        # Add metadata
        df['word_count'] = df['cleaned_transcript'].apply(lambda x: len(x.split()))
        df['sentence_count'] = df['cleaned_transcript'].apply(lambda x: len(sent_tokenize(x)))
        
        # Create chunks for RAG
        all_chunks = []
        for idx, row in df.iterrows():
            chunks = self.chunk_text(row['cleaned_transcript'])
            for chunk_idx, chunk in enumerate(chunks):
                all_chunks.append({
                    'talk_id': idx,
                    'chunk_id': chunk_idx,
                    'title': row['title'],
                    'speaker': row['speaker'],
                    'chunk_text': chunk,
                    'key_topics': row['key_topics']
                })
        
        # Save processed data
        df.to_csv(output_file, index=False)
        
        # Save chunks separately
        chunks_df = pd.DataFrame(all_chunks)
        chunks_file = output_file.replace('.csv', '_chunks.csv')
        chunks_df.to_csv(chunks_file, index=False)
        
        print(f"✅ Processed {len(df)} talks into {len(chunks_df)} chunks")
        return df, chunks_df

# Usage
if __name__ == "__main__":
    processor = TEDxDataProcessor()
    talks_df, chunks_df = processor.process_dataset(
        './data/raw/tedx_talks.csv',
        './data/processed/tedx_talks_processed.csv'
    )
