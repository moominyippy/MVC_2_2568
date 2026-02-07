"""Model for Campaign"""
from utils.csv_handler import read_csv, write_csv

class Campaign:
    def __init__(self, campaign_id: str, election_year: str, district: str):
        self.campaign_id = campaign_id
        self.election_year = election_year
        self.district = district
    
    def to_dict(self):
        return {
            'campaign_id': self.campaign_id,
            'election_year': self.election_year,
            'district': self.district
        }
    
    @staticmethod
    def from_dict(data: dict):
        return Campaign(
            campaign_id=data['campaign_id'],
            election_year=data['election_year'],
            district=data['district']
        )
    
    @staticmethod
    def get_all():
        """Get all campaigns from CSV"""
        data = read_csv('campaigns.csv')
        return [Campaign.from_dict(row) for row in data]
    
    @staticmethod
    def get_by_id(campaign_id: str):
        """
        Get campaign by ID (more efficient than get_all)
        
        Args:
            campaign_id (str): ID of the campaign
            
        Returns:
            Campaign: Campaign object if found, None otherwise
        """
        data = read_csv('campaigns.csv')
        for row in data:
            if row.get('campaign_id') == campaign_id:
                return Campaign.from_dict(row)
        return None
    
    @staticmethod
    def save_all(campaigns: list):
        """Save all campaigns to CSV"""
        data = [c.to_dict() for c in campaigns]
        write_csv('campaigns.csv', data, ['campaign_id', 'election_year', 'district'])

