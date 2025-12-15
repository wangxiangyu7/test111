from app import db
from datetime import datetime

class Bookmark(db.Model):
    """Bookmark model for storing website bookmarks"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    description = db.Column(db.Text)
    tags = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Bookmark {self.title}>'

    def get_tags_list(self):
        """Return tags as a list"""
        if self.tags:
            return [tag.strip() for tag in self.tags.split(',')]
        return []

    @staticmethod
    def get_all_tags():
        """Get all unique tags from all bookmarks"""
        bookmarks = Bookmark.query.all()
        tags_set = set()
        for bookmark in bookmarks:
            tags_set.update(bookmark.get_tags_list())
        return sorted(tags_set)
