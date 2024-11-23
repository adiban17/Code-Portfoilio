import requests
from bs4 import BeautifulSoup
import pprint

def get_hn_news():
    # Get the webpage
    res = requests.get('https://news.ycombinator.com/')
    soup = BeautifulSoup(res.text, 'html.parser')
    
    # Select containers
    titleline_containers = soup.select('.titleline')
    votes = soup.select('.score')
    
    def create_custom_hn(links, votes):
        hn = []
        for idx, item in enumerate(links):
            # Find the <a> tag within titleline
            link = item.find('a')
            if link:
                title = link.getText()
                href = link.get('href')
                
                # Create base dictionary
                story = {'title': title, 'link': href}
                
                # Add points if available
                if idx < len(votes):
                    points_text = votes[idx].getText()
                    try:
                        # Extract just the number from strings like "123 points"
                        points = int(points_text.split()[0])
                        story['points'] = points
                    except (ValueError, IndexError):
                        story['points'] = 0
                
                hn.append(story)
        
        return hn

    return create_custom_hn(titleline_containers, votes)

# Run the scraper
if __name__ == "__main__":
    results = get_hn_news()
    pprint.pprint(results)
print(188/346)