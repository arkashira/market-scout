import json
import urllib.request
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

class DataSource(Enum):
    CRUNCHBASE = "Crunchbase"
    CLEARBIT = "Clearbit"
    INTERNAL = "Internal"

@dataclass
class CompetitorData:
    name: str
    description: str
    source: DataSource

class MarketScout:
    def __init__(self, api_keys: Dict[str, str]):
        self.api_keys = api_keys
        self.internal_data = {
            "company1": {"name": "Company 1", "description": "Description 1"},
            "company2": {"name": "Company 2", "description": "Description 2"},
        }

    def get_competitor_data(self, company_id: str) -> CompetitorData:
        try:
            # Try to fetch data from Crunchbase
            crunchbase_url = f"https://api.crunchbase.com/v4/entities/organizations/{company_id}"
            crunchbase_response = urllib.request.urlopen(crunchbase_url)
            crunchbase_data = json.loads(crunchbase_response.read())
            return CompetitorData(
                name=crunchbase_data["data"]["name"],
                description=crunchbase_data["data"]["description"],
                source=DataSource.CRUNCHBASE,
            )
        except Exception as e:
            print(f"Error fetching data from Crunchbase: {e}")

        try:
            # Try to fetch data from Clearbit
            clearbit_url = f"https://api.clearbit.com/v1/domains/find?domain={company_id}"
            clearbit_response = urllib.request.urlopen(clearbit_url)
            clearbit_data = json.loads(clearbit_response.read())
            return CompetitorData(
                name=clearbit_data["name"],
                description=clearbit_data["description"],
                source=DataSource.CLEARBIT,
            )
        except Exception as e:
            print(f"Error fetching data from Clearbit: {e}")

        # Fallback to internal dataset
        internal_data = self.internal_data.get(company_id)
        if internal_data:
            return CompetitorData(
                name=internal_data["name"],
                description=internal_data["description"],
                source=DataSource.INTERNAL,
            )

        # Return a default value if all else fails
        return CompetitorData(
            name="Unknown",
            description="Unknown",
            source=DataSource.INTERNAL,
        )

    def get_competitor_landscape(self, company_ids: List[str]) -> List[CompetitorData]:
        competitor_data = []
        for company_id in company_ids:
            competitor_data.append(self.get_competitor_data(company_id))
        return competitor_data
