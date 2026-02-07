"""Model for PromiseUpdate"""
from utils.csv_handler import read_csv, append_csv

class PromiseUpdate:
    def __init__(self, promise_id: str, update_date: str, progress_details: str):
        self.promise_id = promise_id
        self.update_date = update_date
        self.progress_details = progress_details
    
    def to_dict(self):
        return {
            'promise_id': self.promise_id,
            'update_date': self.update_date,
            'progress_details': self.progress_details
        }
    
    @staticmethod
    def from_dict(data: dict):
        return PromiseUpdate(
            promise_id=data['promise_id'],
            update_date=data['update_date'],
            progress_details=data['progress_details']
        )
    
    @staticmethod
    def get_all():
        """Get all promise updates from CSV"""
        data = read_csv('promise_updates.csv')
        return [PromiseUpdate.from_dict(row) for row in data]
    
    @staticmethod
    def get_by_promise_id(promise_id: str):
        """Get all updates for a specific promise, sorted by date"""
        updates = PromiseUpdate.get_all()
        promise_updates = [u for u in updates if u.promise_id == promise_id]
        # Sort by update date (newest first)
        promise_updates.sort(key=lambda x: x.update_date, reverse=True)
        return promise_updates
    
    @staticmethod
    def create(promise_id: str, update_date: str, progress_details: str):
        """Create and save a new promise update"""
        update = PromiseUpdate(promise_id, update_date, progress_details)
        append_csv('promise_updates.csv', update.to_dict(), 
                  ['promise_id', 'update_date', 'progress_details'])
        return update

