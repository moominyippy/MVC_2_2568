"""Controller for Promise operations - handles business logic"""
from models.politician import Politician
from models.promise import Promise
from models.promise_update import PromiseUpdate
from datetime import datetime
from utils.constants import SORT_DESC, SORT_ASC


class PromiseController:
    """Controller class for managing promise-related business logic"""
    
    @staticmethod
    def get_all_promises(sort_order=SORT_DESC):
        """
        Get all promises sorted by announcement date
        
        Args:
            sort_order (str): 'desc' for newest first, 'asc' for oldest first
            
        Returns:
            list: List of Promise objects sorted by announcement date
        """
        promises = Promise.get_all()
        
        if sort_order == SORT_ASC:
            promises.sort(key=lambda x: x.announcement_date)
        else:
            promises.sort(key=lambda x: x.announcement_date, reverse=True)
            
        return promises
    
    @staticmethod
    def get_promise_detail(promise_id: str):
        """
        Get promise detail with related updates and politician information
        
        Args:
            promise_id (str): ID of the promise
            
        Returns:
            tuple: (Promise object, dict with 'updates' and 'politician')
                   Returns (None, None) if promise not found
        """
        promise = Promise.get_by_id(promise_id)
        if not promise:
            return None, None
        
        updates = PromiseUpdate.get_by_promise_id(promise_id)
        politician = Politician.get_by_id(promise.politician_id)
        
        return promise, {
            'updates': updates,
            'politician': politician
        }
    
    @staticmethod
    def update_progress(promise_id: str, progress_details: str):
        """
        Update promise progress with validation
        
        Args:
            promise_id (str): ID of the promise to update
            progress_details (str): Details of the progress update
            
        Returns:
            tuple: (bool, str) - (success, message)
        """
        promise = Promise.get_by_id(promise_id)
        if not promise:
            return False, "ไม่พบคำสัญญา"
        
        if not promise.can_update():
            return False, "คำสัญญานี้มีสถานะ 'เงียบหาย' ไม่สามารถอัปเดตได้"
        
        # Create update record
        update_date = datetime.now().strftime('%Y-%m-%d')
        PromiseUpdate.create(promise_id, update_date, progress_details)
        
        # Auto-update promise status if needed
        if promise.status == Promise.STATUS_NOT_STARTED:
            PromiseController._update_promise_status(promise_id, Promise.STATUS_IN_PROGRESS)
        
        return True, "อัปเดตความคืบหน้าสำเร็จ"
    
    @staticmethod
    def _update_promise_status(promise_id: str, new_status: str):
        """
        Internal method to update promise status
        
        Args:
            promise_id (str): ID of the promise
            new_status (str): New status to set
        """
        promises = Promise.get_all()
        for promise in promises:
            if promise.promise_id == promise_id:
                promise.status = new_status
                break
        Promise.save_all(promises)
    
    @staticmethod
    def get_politician_promises(politician_id: str):
        """
        Get all promises for a specific politician
        
        Args:
            politician_id (str): ID of the politician
            
        Returns:
            tuple: (Politician object, list of Promise objects)
                   Returns (None, None) if politician not found
        """
        politician = Politician.get_by_id(politician_id)
        if not politician:
            return None, None
        
        promises = Promise.get_by_politician_id(politician_id)
        return politician, promises
    
    @staticmethod
    def get_promise_counts_by_politician():
        """
        Get count of promises for each politician
        
        Returns:
            dict: Dictionary mapping politician_id to promise count
        """
        all_promises = Promise.get_all()
        promise_counts = {}
        for promise in all_promises:
            promise_counts[promise.politician_id] = promise_counts.get(promise.politician_id, 0) + 1
        return promise_counts

