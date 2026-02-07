"""Model for Politician"""
from utils.csv_handler import read_csv, write_csv

class Politician:
    def __init__(self, politician_id: str, name: str, party: str):
        self.politician_id = politician_id
        self.name = name
        self.party = party
    
    def to_dict(self):
        return {
            'politician_id': self.politician_id,
            'name': self.name,
            'party': self.party
        }
    
    @staticmethod
    def from_dict(data: dict):
        return Politician(
            politician_id=data['politician_id'],
            name=data['name'],
            party=data['party']
        )
    
    @staticmethod
    def get_all():
        """Get all politicians from CSV"""
        data = read_csv('politicians.csv')
        return [Politician.from_dict(row) for row in data]
    
    @staticmethod
    def get_by_id(politician_id: str):
        """
        Get politician by ID (more efficient than get_all)
        
        Args:
            politician_id (str): ID of the politician
            
        Returns:
            Politician: Politician object if found, None otherwise
        """
        data = read_csv('politicians.csv')
        for row in data:
            if row.get('politician_id') == politician_id:
                return Politician.from_dict(row)
        return None
    
    @staticmethod
    def save_all(politicians: list):
        """Save all politicians to CSV"""
        data = [p.to_dict() for p in politicians]
        write_csv('politicians.csv', data, ['politician_id', 'name', 'party'])

