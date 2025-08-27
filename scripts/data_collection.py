import requests
import pandas as pd
import json
import time
from bs4 import BeautifulSoup
from youtube_transcript_api import YouTubeTranscriptApi
from tqdm import tqdm
import os

class TEDxDataCollector:
	def __init__(self):
		self.base_url = "https://www.ted.com"
		self.talks_data = []
        
	def scrape_tedx_talks_list(self, max_pages=10):
		"""Scrape TEDx talks metadata"""
		print("🔍 Scraping TEDx talks list...")
        
		for page in tqdm(range(1, max_pages + 1)):
			url = f"https://www.ted.com/talks?page={page}&q=tedx"
            
			try:
				response = requests.get(url)
				soup = BeautifulSoup(response.content, 'html.parser')
                
				# Find talk containers
				talks = soup.find_all('div', class_='talk-link')
                
				for talk in talks:
					talk_data = self.extract_talk_metadata(talk)
					if talk_data:
						self.talks_data.append(talk_data)
                        
				time.sleep(1)  # Be respectful to servers
                
			except Exception as e:
				print(f"Error scraping page {page}: {e}")
				continue
                
		return self.talks_data
    
	def extract_talk_metadata(self, talk_element):
		"""Extract metadata from a single talk"""
		try:
			title_elem = talk_element.find('h4', class_='h12')
			speaker_elem = talk_element.find('h4', class_='h12').find_next('h4')
			link_elem = talk_element.find('a')
            
			if not all([title_elem, speaker_elem, link_elem]):
				return None
                
			return {
				'title': title_elem.text.strip(),
				'speaker': speaker_elem.text.strip(),
				'url': self.base_url + link_elem['href'],
				'video_id': self.extract_video_id(link_elem['href'])
			}
		except:
			return None
    
	def extract_video_id(self, url):
		"""Extract YouTube video ID from TED URL"""
		# This is a simplified version - you'll need to implement
		# the actual extraction logic based on TED's URL structure
		return url.split('/')[-1]
    
	def get_transcript(self, video_id):
		"""Get transcript using youtube-transcript-api"""
		try:
			transcript = YouTubeTranscriptApi.get_transcript(video_id)
			full_text = ' '.join([entry['text'] for entry in transcript])
			return full_text
		except:
			return None
    
	def save_data(self, filename='tedx_talks.csv'):
		"""Save collected data to CSV"""
		df = pd.DataFrame(self.talks_data)
		df.to_csv(f'./data/raw/{filename}', index=False)
		print(f"💾 Saved {len(df)} talks to {filename}")
		return df

# Usage example
if __name__ == "__main__":
	collector = TEDxDataCollector()
	talks = collector.scrape_tedx_talks_list(max_pages=5)
	df = collector.save_data()
