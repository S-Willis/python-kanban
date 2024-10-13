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
    cleared = db.Column(db.Boolean, default=False)

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

def all_blocks():
    """Return JSON for all blocks"""
    return [block.json() for block in Block.query.all()]

def create_block(title, **kwargs):
    """Create a new Block"""
    #TODO: Auto-pull block title from blocker card?
    db.session.add(Block(title=title, **kwargs))
    db.session.commit()

def delete_block(block_id):
    """Delete a block"""
    db.session.delete(Block.query.get(block_id))
    db.session.commit()

def clear_block(block_id):
    """Clear a block, removing it from UI but keeping it in DB"""
    block = Block.query.get(block_id)

    block.cleared = True

    db.session.commit()

def get_blocks_for_card(blockee_id):
    
    return [block.json for block in Block.query.filter(blockee_id=blockee_id).all]

def get_blocks_caused_by_card(blocker_id):
    #TODO: Return list of Blocks (Cards?) where blocker_id matches
    return [block.json for block in Block.query.filter(blocker_id=blocker_id).all]
