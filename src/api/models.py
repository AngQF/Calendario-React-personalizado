from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CalendarAvailability(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    is_available = db.Column(db.Boolean)
    

    def serialize(self):
        return {
            "id": self.id,
            "date": self.date.strftime("%Y-%m-%d") if self.date is not None else None,
            "time": self.time.strftime("%H:%M") if self.time is not None else None,
            "is_available": self.is_available,
        }