from models import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    correo = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    active = db.Column(db.Boolean(), default=True)
    roles_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "roles_id": self.roles_id,
            "active": self.active,
            "role": self.role.seralize()
        }
        
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()