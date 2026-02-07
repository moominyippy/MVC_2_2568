"""Model for Promise"""
from utils.csv_handler import read_csv, write_csv
from datetime import datetime

class Promise:
    STATUS_NOT_STARTED = 'ยังไม่เริ่ม'
    STATUS_IN_PROGRESS = 'กำลังดำเนินการ'
    STATUS_SILENT = 'เงียบหาย'
    
    def __init__(self, promise_id: str, politician_id: str, description: str, 
                 announcement_date: str, status: str, campaign_id: str = ''):
        self.promise_id = promise_id
        self.politician_id = politician_id
        self.description = description
        self.announcement_date = announcement_date
        self.status = status
        self.campaign_id = campaign_id
    
    def to_dict(self):
        return {
            'promise_id': self.promise_id,
            'politician_id': self.politician_id,
            'description': self.description,
            'announcement_date': self.announcement_date,
            'status': self.status,
            'campaign_id': self.campaign_id
        }
    
    @staticmethod
    def from_dict(data: dict):
        return Promise(
            promise_id=data['promise_id'],
            politician_id=data['politician_id'],
            description=data['description'],
            announcement_date=data['announcement_date'],
            status=data['status'],
            campaign_id=data.get('campaign_id', '')
        )
    
    @staticmethod
    def get_all():
        """Get all promises from CSV (unsorted)"""
        data = read_csv('promises.csv')
        promises = [Promise.from_dict(row) for row in data]
        return promises
    
    @staticmethod
    def get_by_id(promise_id: str):
        """
        Get promise by ID (more efficient than get_all)
        
        Args:
            promise_id (str): ID of the promise
            
        Returns:
            Promise: Promise object if found, None otherwise
        """
        data = read_csv('promises.csv')
        for row in data:
            if row.get('promise_id') == promise_id:
                return Promise.from_dict(row)
        return None
    
    @staticmethod
    def get_by_politician_id(politician_id: str):
        """Get all promises by politician ID"""
        promises = Promise.get_all()
        return [p for p in promises if p.politician_id == politician_id]
    
    @staticmethod
    def save_all(promises: list):
        """Save all promises to CSV"""
        data = [p.to_dict() for p in promises]
        write_csv('promises.csv', data, ['promise_id', 'politician_id', 'description', 
                                         'announcement_date', 'status', 'campaign_id'])
    
    def can_update(self):
        """Check if promise can be updated (not silent)"""
        return self.status != Promise.STATUS_SILENT

