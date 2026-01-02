"""
External API client.

Este cliente interactúa con APIs externas que necesitamos
mockear en los tests.
"""

import httpx
from dataclasses import dataclass


@dataclass
class WeatherData:
    """Weather information."""
    city: str
    temperature: float
    description: str
    humidity: int


class WeatherClient:
    """Client for weather API."""
    
    BASE_URL = "https://api.weather.example.com/v1"
    
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    async def get_current_weather(self, city: str) -> WeatherData:
        """
        Get current weather for a city.
        
        This makes a real HTTP request - mock in tests!
        """
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.BASE_URL}/current",
                params={"city": city, "key": self.api_key}
            )
            response.raise_for_status()
            data = response.json()
            
            return WeatherData(
                city=data["location"]["name"],
                temperature=data["current"]["temp_c"],
                description=data["current"]["condition"]["text"],
                humidity=data["current"]["humidity"],
            )
    
    async def get_forecast(self, city: str, days: int = 3) -> list[dict]:
        """Get weather forecast."""
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{self.BASE_URL}/forecast",
                params={"city": city, "days": days, "key": self.api_key}
            )
            response.raise_for_status()
            data = response.json()
            
            return data["forecast"]["forecastday"]


class GitHubClient:
    """Client for GitHub API."""
    
    BASE_URL = "https://api.github.com"
    
    def __init__(self, token: str | None = None):
        self.token = token
    
    def _get_headers(self) -> dict:
        """Get request headers."""
        headers = {"Accept": "application/vnd.github.v3+json"}
        if self.token:
            headers["Authorization"] = f"token {self.token}"
        return headers
    
    def get_user(self, username: str) -> dict:
        """Get GitHub user information."""
        with httpx.Client() as client:
            response = client.get(
                f"{self.BASE_URL}/users/{username}",
                headers=self._get_headers()
            )
            response.raise_for_status()
            return response.json()
    
    def get_repos(self, username: str) -> list[dict]:
        """Get user's repositories."""
        with httpx.Client() as client:
            response = client.get(
                f"{self.BASE_URL}/users/{username}/repos",
                headers=self._get_headers()
            )
            response.raise_for_status()
            return response.json()
    
    def get_repo_stats(self, owner: str, repo: str) -> dict:
        """Get repository statistics."""
        user = self.get_user(owner)
        
        with httpx.Client() as client:
            response = client.get(
                f"{self.BASE_URL}/repos/{owner}/{repo}",
                headers=self._get_headers()
            )
            response.raise_for_status()
            repo_data = response.json()
        
        return {
            "owner": user["login"],
            "owner_followers": user["followers"],
            "repo_name": repo_data["name"],
            "stars": repo_data["stargazers_count"],
            "forks": repo_data["forks_count"],
        }
