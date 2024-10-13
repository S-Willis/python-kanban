"Block Model and Controller"

"""Each Block is an instance of a card being blocked.
At simplest, a block will be user-defined with a title only.
In this case there is no blocker_id, value will be "0"

Slightly more complex, a card can be blocked by another card.
A block records that card A (blockee) is blocked by card B (blocker), 
the block title is the title of block B"""

from database import db

class Block(db.model):
    """SQLAlchemy Block Class"""
    block_id = db.Column(db.Integer, primary_key=True)
    blockee_id = db.Column(db.Integer)
    blocker_id = db.Column(db.Integer, default=0)
    title = db.Column(db.String(120), default="Blocker")

    def __repr__(self):
        """Return a string representation of a Block Instance"""
        return '<Block (%d): %s>' % (self.block_id, self.title)
    
    def json(self):
        """Return a JSON representation of a block"""
        return {
            'block_id': self.block_id,
            'title': self.title,
            'blockee_id': self.blockee_id,
            'blocker_id': self.blocker_id,
        }

