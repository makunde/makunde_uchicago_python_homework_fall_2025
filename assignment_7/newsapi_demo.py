"""NewsAPI module for fetching and displaying news articles."""

import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Colors:
    """ANSI color codes for terminal coloring."""

    GREEN = "\033[92m"
    RESET = "\033[0m"
    BOLD = "\033[1m"


class NewsAPI:
    """A class to interact with the NewsAPI.org API."""

    API_KEY = os.getenv(
        "NEWS_API_KEY"
    )  # Not sure if I had to hide it as part of the assignment but just best practice.
    BASE_URL = "https://newsapi.org/v2"
    CATEGORIES = {
        "1": "business",
        "2": "entertainment",
        "3": "general",
        "4": "health",
        "5": "science",
        "6": "sports",
        "7": "technology",
    }

    def __init__(self):
        """Initialize the NewsAPI client."""
        self.session = requests.Session()

    def _format_date(self, date_str):
        """Convert date string to readable format (Month Day, Year).

        Args:
            date_str (str): ISO 8601 formatted date string

        Returns:
            str: Formatted date string (e.g., "November 26, 2025")
        """
        try:
            formatted_date = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
            return formatted_date.strftime("%B %d, %Y")
        except:
            return date_str

    def _display_articles(self, articles):
        """Display articles in the specified format.

        Args:
            articles (list): List of article dictionaries from the API
        """
        for article in articles[:10]:
            title = article.get("title", "No Title")
            source_name = article.get("source", {}).get("name", "Unknown Source")
            published_date = self._format_date(article.get("publishedAt", ""))
            description = article.get("description", "")

            colored_title = f"{Colors.GREEN}{Colors.BOLD}{title}{Colors.RESET}"
            print(
                f"* {colored_title} - {source_name} ({published_date})\n         {description if description else ''}\n"
            )

    def get_top_headlines(self, category):
        """Fetch top headlines for a specific category.

        Args:
            category (str): Category code (1-7)

        Returns:
            bool: True if successful, False otherwise
        """
        if category not in self.CATEGORIES:
            print("Invalid category selection.")
            return False

        category_name = self.CATEGORIES[category]
        url = f"{self.BASE_URL}/top-headlines"
        params = {
            "country": "us",
            "category": category_name,
            "pageSize": 10,
            "apiKey": self.API_KEY,
        }

        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            if data.get("status") != "ok":
                print(f"API Error: {data.get('message', 'Unknown error')}")
                return False

            articles = data.get("articles", [])
            if not articles:
                print("No articles found.")
                return False

            self._display_articles(articles)
            return True
        except requests.RequestException as e:
            print(f"Error fetching headlines: {e}")
            return False

    def search_articles(self, query):
        """Search for articles based on a query.

        Args:
            query (str): Search query string

        Returns:
            bool: True if successful, False otherwise
        """
        url = f"{self.BASE_URL}/everything"
        params = {
            "q": query,
            "sortBy": "publishedAt",
            "pageSize": 10,
            "apiKey": self.API_KEY,
        }

        try:
            response = self.session.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            if data.get("status") != "ok":
                print(f"API Error: {data.get('message', 'Unknown error')}")
                return False

            articles = data.get("articles", [])
            if not articles:
                print("No articles found for that search term.")
                return False

            self._display_articles(articles)
            return True
        except requests.RequestException as e:
            print(f"Error searching articles: {e}")
            return False


class NewsApp:
    """A command-line application for browsing news headlines."""

    def __init__(self):
        """Initialize the news application."""
        self.api = NewsAPI()

    def _display_menu(self):
        """Display the main menu and get user choice."""
        return input(
            "\nPlease make a choice: [1] Top headlines [2] Search\n>> "
        ).strip()

    def _display_category_menu(self):
        """Display category selection menu and get user choice."""
        print("\nSelect which category would you like headlines for:")
        print("[1] business")
        print("[2] entertainment")
        print("[3] general")
        print("[4] health")
        print("[5] science")
        print("[6] sports")
        print("[7] technology")
        choice = input(">> ").strip()
        return choice

    def _get_more_articles(self):
        """Ask user if they want more articles.

        Returns:
            bool: True if user wants more articles, False otherwise
        """
        response = (
            input("\nWould you like to find more news articles? [y/n]\n>> ")
            .strip()
            .lower()
        )
        return response == "y"

    def run(self):
        """Run the news application main loop."""
        print("Welcome to Command Line News!")

        while True:
            choice = self._display_menu()

            if choice == "1":
                category = self._display_category_menu()
                self.api.get_top_headlines(category)
            elif choice == "2":
                print("\nEnter your search term:")
                query = input("\nEnter your search term:\n>> ").strip()
                if query:
                    self.api.search_articles(query)
                else:
                    print("Please enter a valid search term.")
            else:
                print("Invalid choice. Please enter 1 or 2.")
                continue

            if not self._get_more_articles():
                print("\nThank you for using Command Line News!")
                break
